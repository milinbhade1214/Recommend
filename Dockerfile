# Use official python image
FROM python:3.10-slim

# Set working Dir
WORKDIR /app

# Copy requirements and install  dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code 
COPY . .

# Add start script
COPY start.sh .
RUN chmod +x start.sh


# Expose port for FASTAPI
EXPOSE 8000


# Command to run FASTAPI app
CMD ["./start.sh"]