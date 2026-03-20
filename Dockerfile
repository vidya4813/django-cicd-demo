FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy code
COPY . .

# Install Django
RUN pip install django

# Expose port
EXPOSE 8000

# Run server
CMD ["python", "-m", "django", "urls", "runserver", "0.0.0.0:8000"]