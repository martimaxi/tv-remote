FROM python:3.11-alpine

RUN apk add --no-cache android-tools

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY server.py .
COPY index.html .

EXPOSE 5000

CMD ["python", "server.py"]