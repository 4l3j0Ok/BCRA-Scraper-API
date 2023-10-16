FROM python:3.11.4-alpine as dependencies

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --user -r ./requirements.txt

FROM python:3.11.4-alpine as builder
WORKDIR /app
COPY ./src /app/src
COPY --from=dependencies /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8080
CMD ["python", "/app/src/main.py"]
