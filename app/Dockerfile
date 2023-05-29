FROM python:latest

# Copy the .env file to the Docker image
COPY .env /app/.env

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip3 install --upgrade pip && \
    pip3 install Flask mysql-connector-python requests python-dotenv

# Copy the rest of the application files to the Docker image
COPY . /app

# Set the environment variable to load .env file during runtime
ENV PYTHONPATH=/app

# Start the application and load environment variables from .env
CMD ["python", "-c", "from dotenv import load_dotenv; import os; load_dotenv(); os.system('python user_api.py')"]






