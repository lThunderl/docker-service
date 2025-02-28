from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import uvicorn
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяет запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"],  # Позволяет все методы
    allow_headers=["*"],  # Позволяет все заголовки
)


SERVICE_NAME = os.getenv("SERVICE_NAME", "Default")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "0")
RELATED_SERVICES = os.getenv("RELATED_SERVICES", "").split(",")
SERVICE_PORT = os.getenv("PORT", "8000")
id = os.getenv("id", "0")

@app.get("/")
async def read_root():
    related_info = []
    if RELATED_SERVICES and RELATED_SERVICES[0]:
        async with httpx.AsyncClient() as client:
            for service_url in RELATED_SERVICES:
                service_url = service_url.strip()  # Удаление пробелов
                try:
                    response = await client.get(service_url)
                    related_info.append(response.json()) 
                except:
                    related_info = f"Error fetching {service_url}"
    else: related_info = f"No Related Services"

    data = { 
        "id" : id,
        "Service_Name" : SERVICE_NAME,
        "Service_Version" : SERVICE_VERSION,
        "Port" : SERVICE_PORT,
        "Related_Services" :related_info
    }
    
    return JSONResponse(content = data)  
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)