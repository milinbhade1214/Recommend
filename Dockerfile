# Use official python image
FROM python:3.10-slim

# Set working Dir
WORKDIR /app

# Copy requirements and install  dependencies
COPY requirements.txt .

# Copy rest of the code 
COPY . .

# Expose port for FASTAPI
EXPOSE 8000

# Command to run FASTAPI app
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]