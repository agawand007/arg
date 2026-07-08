# Use official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
