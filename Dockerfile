FROM python:3.10-slim

WORKDIR /app

COPY requerimentos.txt .

RUN pip install --no-cache-dir -r requerimentos.txt

COPY . .

EXPOSE 8383

VOLUME ["/app/database"]

CMD ["flask", "run", "--host=0.0.0.0","--port=8383"]


#docker build -t api-admiradores .
#docker run -d -v admiradores_volume:/app/database -p 8383:8383 api-admiradores


