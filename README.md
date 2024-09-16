# Componente - Api-Admiradores
 MicroService para Cruid de admiradores

## 1. Objetivo
Post, Put, Gets e Delete de Admiradores

## 3. Referência Técnica
- Esta API foi desenvolvida em **Phyton** faz uso do seu próprio **Dockerfile** e de seu próprio Repositório em **SQLLite**, ORM **Sqlalchemy**, o banco com sua respectiva tabela será gerado automaticamente;

## 4. Subindo o componente Api-Admiradores
### 4.1
- Abrir um novo terminal na pasta do projeto (onde se encontra o arquivo Dockerfile).
### 4.3 - Executar os comandos abaixo
   ```sh
   docker build -t api-admiradores .
   docker run -d -p 8383:8383 api-admiradores
   ```
- Feito isso a documentação do componente **Api-Admiradores** é disponibilizada em `localhost:8383`.
