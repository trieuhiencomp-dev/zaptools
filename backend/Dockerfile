FROM python:3.11-slim

# Install system dependencies for PDF processing
RUN apt-get update && apt-get install -y \
    poppler-utils \
    libpoppler-cpp-dev \
    tesseract-ocr \
    libreoffice \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8080

# Run the application
CMD exec gunicorn --bind :$PORT --timeout 300 --workers 2 app:app
