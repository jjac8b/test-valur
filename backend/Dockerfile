FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/
COPY manage.py /app/
COPY tmptest/ /app/tmptest

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 3000
# Collect static files
RUN python manage.py collectstatic --noinput
WORKDIR /app/

# Run the Django application on the specific port (8000 by default)
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]