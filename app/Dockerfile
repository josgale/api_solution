FROM python:latest

COPY .env /app/.env

WORKDIR /app

RUN pip3 install --upgrade pip && \
    pip3 install Flask mysql-connector-python requests python-dotenv

COPY . /app

ENV PYTHONPATH=/app

CMD ["python", "user_api.py"]






