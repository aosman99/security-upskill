# Base image: official slim Python (smaller than full image)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list first (layer caching: only re-installs if this changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and the log file into the image
COPY log_analyzer.py .
COPY access.log .

# Default command to run when the container starts
CMD ["python", "log_analyzer.py"]
