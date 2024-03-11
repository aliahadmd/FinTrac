# Use an official Python runtime as a parent image
FROM python:3.12.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /fintrac

# Install dependencies
COPY requirements.txt /fintrac/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /fintrac/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD gunicorn main.wsgi:application --bind 0.0.0.0:8086