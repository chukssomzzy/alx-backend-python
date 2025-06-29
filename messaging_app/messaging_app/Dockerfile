# Use official Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in container
WORKDIR /app

# Install dependencies
COPY Requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files to container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Start the Django app (adjust this if you use a custom entrypoint)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
