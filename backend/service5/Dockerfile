FROM python:3.12.9-alpine3.21
WORKDIR /service5
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py ./
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]