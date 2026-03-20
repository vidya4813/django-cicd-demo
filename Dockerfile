FROM python:3.10-slim

WORKDIR /app

COPY . .

# Upgrade pip and install Django (and other dependencies if needed)
RUN pip install --upgrade pip
RUN pip install django

# Expose Django default port
EXPOSE 8000

# Run Django development server on all interfaces
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]