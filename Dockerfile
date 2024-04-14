# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the Chrome version as an environment variable
ENV CHROME_VERSION=123.0.6312.105

# Set working directory
WORKDIR /app

# Install dependencies required for Google Chrome and ChromeDriver installation
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y wget gnupg2 software-properties-common unzip && \
    rm -rf /var/lib/apt/lists/*

# Add Google Chrome repository and key
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list'

# Install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable && rm -rf /var/lib/apt/lists/*

# Check the version of Google Chrome
RUN google-chrome --version

# Download and install ChromeDriver matching the specified Chrome version
RUN wget -q --continue -P /chromedriver "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip /chromedriver/chromedriver* -d /usr/local/bin/ \
    && rm -rf /chromedriver

# Copy the requirements file and install Python packages from it
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python scripts and the start script to the container
COPY m12_utilization.py /app/m12_utilization.py
COPY matsya_utilization.py /app/matsya_utilization.py
COPY start_scripts.sh /app/start_scripts.sh

# Give execution permissions to the Python scripts and the start script
RUN chmod +x /app/m12_utilization.py /app/matsya_utilization.py /app/start_scripts.sh

# Update start_scripts.sh to call the scripts in the current directory
# Note: Ensure the start_scripts.sh script references the correct path
# For example:
# #!/bin/bash
# python /app/m12_utilization.py
# python /app/matsya_utilization.py

# Set the start script as the entry point
ENTRYPOINT ["/app/start_scripts.sh"]
