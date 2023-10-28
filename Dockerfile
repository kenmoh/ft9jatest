FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port
EXPOSE 8000

# Copy the project code into the container
COPY . .

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]