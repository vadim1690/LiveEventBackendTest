# Use a Python base image with dlib and face-recognition pre-installed
FROM nicokrieg/python-dlib-face-recognition:python3.9-slim

# Set up your working directory
WORKDIR /app

# Copy your app files to the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Set the command to run your FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
