# Multi-stage or optimized production Dockerfile for Calculator CI/CD Demo
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and test suite
COPY app/ ./app/
COPY tests/ ./tests/
COPY build.sh .

# Create a secure, non-privileged user to run the application
RUN useradd -u 1001 -m devopsuser && \
    chown -R devopsuser:devopsuser /app

USER devopsuser

# Expose default health-check / demo execution command
ENTRYPOINT ["python", "app/calculator.py"]
CMD ["--demo"]
