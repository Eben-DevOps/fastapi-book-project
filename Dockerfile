# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Expose the internal FastAPI port
EXPOSE 8000

# Run the application (update the module path)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
