FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000/tcp

CMD ["gunicorn", "--workers", "2", "agblimp.wsgi:application", "--bind", "0.0.0.0:8000"]
