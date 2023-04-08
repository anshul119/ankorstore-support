# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the environment variable for the Flask app
ENV FLASK_APP=server.py

# Expose the port that the server will run on
EXPOSE 5000

# Start the server
CMD ["flask", "run", "--host=0.0.0.0"]