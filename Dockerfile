# Use Python 3.12 with platform specification
FROM --platform=linux/amd64 python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_ALLOWED_HOSTS="*"

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "romplinarena.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120", "--workers", "3", "--keep-alive", "5", "--max-requests", "1000"]
