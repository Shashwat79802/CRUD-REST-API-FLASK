# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]