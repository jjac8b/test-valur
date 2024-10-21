FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
COPY manage.py /app/
COPY tmptest/ /app/tmptest

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 3000
RUN python manage.py collectstatic --noinput
WORKDIR /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]