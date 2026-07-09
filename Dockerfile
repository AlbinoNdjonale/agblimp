FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000/tcp

CMD sh -c "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn --workers 2 --bind 0.0.0.0:8000 --log-level debug agblimp.wsgi:application"

# CMD ["gunicorn", "--workers", "2", "agblimp.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "debug"]
