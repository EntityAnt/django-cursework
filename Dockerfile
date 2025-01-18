FROM python:3.12-slim

WORKDIR /app


RUN apt-get update && \
    apt-get install -y gcc libpq-dev nginx && \
    apt-get install nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip install gunicorn

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000