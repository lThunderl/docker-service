from fastapi import FastAPI
import os
import uvicorn
import httpx

app = FastAPI()

SERVICE_NAME = os.getenv("SERVICE_NAME", "Default")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "0")
RELATED_SERVICES = os.getenv("RELATED_SERVICES", "").split(",")
SERVICE_PORT = os.getenv("PORT", "8000")


@app.get("/")
async def read_root():
    related_info = ""
    if RELATED_SERVICES and RELATED_SERVICES[0]:
        async with httpx.AsyncClient() as client:
            for service_url in RELATED_SERVICES:
                service_url = service_url.strip()  # Удаление пробелов
                try:
                    response = await client.get(service_url)
                    related_info += f"{response.text}"
                except httpx.RequestError:
                    related_info += f"Error fetching {service_url}"
    else: related_info += f"There are no related services"
    related_info = related_info.split(",")
    data = { 
        "Service_Name" : SERVICE_NAME,
        "Service_Version" : SERVICE_VERSION,
        "Port" : SERVICE_PORT,
        "Related_Services" : related_info
    }
    
    return data  
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)