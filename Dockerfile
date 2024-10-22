# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /epsiburada

# Install dependencies
COPY requirements.txt /epsiburada/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /epsiburada/