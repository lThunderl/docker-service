import docker
import httpx
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяет запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"],  # Позволяет все методы
    allow_headers=["*"],  # Позволяет все заголовки
)


RELATED_SERVICES = os.getenv("RELATED_SERVICES", "").split(",")

@app.get("/")
async def read_root():
    ServiceName = []
    if RELATED_SERVICES and RELATED_SERVICES[0]:
        async with httpx.AsyncClient() as client:
            for service_url in RELATED_SERVICES:
                service_url = service_url.strip()  # Удаление пробелов
                try:
                    response = await client.get(service_url)
                    data = response.json()
                    ServiceName.append({"Service Name: " : data.get('Service_Name', 'Not found'), "Service_Version: ": data.get('Service_Version', 'Not found'), "Service Id: ":  data.get('id', 'Not found'), "Service URL: " : service_url})
                    print(data)
                except:
                    print("Error")
    else: print("No Services")

    return print(ServiceName)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)