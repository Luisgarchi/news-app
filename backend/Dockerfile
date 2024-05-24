# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for the port
ENV PORT=5000

# Expose the port the app runs on
EXPOSE 5000

# Start the app
CMD ["python3", "app.py"]