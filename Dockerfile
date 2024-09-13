FROM python:3.10-slim

WORKDIR /app

COPY requerimentos.txt .

RUN pip install --no-cache-dir -r requerimentos.txt

COPY . .

EXPOSE 8383

VOLUME ["/app/database"]

CMD ["flask", "run", "--host=0.0.0.0","--port=8383"]


#docker stop $(docker ps -q --filter "publish=8383")
#docker build -t api-admiradores .
#docker run -d -p 8383:8383 api-admiradores
#funciona com a porta 8080, 8181, 5000 tentar outras (nao funcionou com a 6000 por exemplo, considera insegura)
