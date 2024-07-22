# Use NVIDIA's CUDA base image with Python
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Install Python and other dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TF_ENABLE_ONEDNN_OPTS=0

# Set the working directory
WORKDIR /summary

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app using gunicorn and uvicorn
CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "mlapi:app"]
