# Use the official Python base image with a specific version
FROM python:3.9.7-alpine

RUN adduser -D spind

RUN apk add --update --no-cache postgresql-dev libffi-dev openssl-dev musl-dev make g++ gcc cargo gdal-dev geos-dev

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

# Install any dependencies specified in requirements.txt
RUN cd /tmp/ && pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY --chown=spind:spind . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

USER spind

# Define the command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "StudentResultManagementSystem.wsgi:application"]