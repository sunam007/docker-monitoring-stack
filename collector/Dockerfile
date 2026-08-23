# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose port 6000 for the API
EXPOSE 6000

# Run the Flask app when the container starts
CMD ["python3", "app.py"]