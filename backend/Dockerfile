FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set build arguments
ARG API_PORT
ARG FRONTEND_PORT
ARG DJANGO_SECRET
ARG DEBUG

# Set environment variables for Django settings
ENV FRONTEND_PORT=${FRONTEND_PORT}
ENV DJANGO_SECRET=${DJANGO_SECRET}
ENV DEBUG=${DEBUG}

WORKDIR /app

COPY requirements.txt /app/
COPY manage.py /app/
COPY api/ /app/api

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000
RUN python manage.py collectstatic --noinput
WORKDIR /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Using 8000 port