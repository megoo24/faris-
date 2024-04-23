# Use an official Python runtime as a parent image
FROM python:alpine3.7

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies required for Python packages that have C extensions
RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev \
    && apk add --no-cache libstdc++

# Copy the Python script into the container
COPY script.py .

# Copy the text file into the container
COPY random_paragraphs.txt .

# Install necessary Python packages
RUN pip install --upgrade pip \
    && pip install nltk

# Download NLTK data
RUN python -m nltk.downloader stopwords \
    && python -m nltk.downloader punkt

# Clean up the unnecessary packages
RUN apk del .build-deps

# Command to run the Python script
CMD ["python", "script.py"]
