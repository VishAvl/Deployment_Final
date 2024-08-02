# Use the official Python 3.9 slim image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Install Streamlit
RUN pip3 install streamlit

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run Streamlit app when the container launches
CMD ["streamlit", "run", "app.py"]

