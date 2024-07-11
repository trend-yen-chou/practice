FROM python:3.11.1-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV HOST=0.0.0.0
ENV PORT=8000

RUN mkdir "/usr/ordersystem"
WORKDIR /usr/ordersystem
COPY . /usr/ordersystem/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD uvicorn webapp.application:app --host ${HOST} --port ${PORT}
