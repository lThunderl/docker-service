import docker
import httpx
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяет запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"],  # Позволяет все методы
    allow_headers=["*"],  # Позволяет все заголовки
)


CONTAINERS_INFO = os.getenv("RELATED_SERVICES", "").split(",")

@app.get("/")
async def read_root():
    ServicesInfo = []
    async with httpx.AsyncClient() as client:
        for service_url in CONTAINERS_INFO:
            service_url = service_url.strip()  # Удаление пробелов
            try:
                response = await client.get(service_url)
                data = response.json()
                ServicesInfo.append({"Service Name: " : data.get('Service_Name', 'Not found'),
                                    "Service_Version: ": data.get('Service_Version', 'Not found'),
                                    "Service Id: ":  data.get('id', 'Not found'),
                                    "Service URL: " : service_url})
                print(data)
            except:
                print("Can't get ServicesInfo")
    try:
        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            if (container.status == "running"):
                ServicesInfo.append({"Is Running: " : "Yes"})
            else:
                ServicesInfo.append({"Is Running: " : "No"})
    except:
        print("Can't get Running containers info")    

        
    return print(ServicesInfo)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)