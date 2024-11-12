# Use a standard Python 3.9 slim image
FROM python:3.9-slim

# Set up your working directory
WORKDIR /app

# Install system dependencies for pyodbc and dlib
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    unixodbc-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-all-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port for the FastAPI app
EXPOSE 8000

# Set the command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
