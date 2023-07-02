# Use the official Python image as the base image
FROM python:alpine3.9

#Copy the content of the project directory to the working directory
COPY . /app

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
# COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
# COPY . .

#Specify the flask environment port
ENV PORT 5000

# Expose port 5000 for the Flask application
EXPOSE 5000

#Set the directive to specify the executable that will run when the container is initiated
ENTRYPOINT [ "python3" ]

# Run the Flask application
CMD ["app.py"]
