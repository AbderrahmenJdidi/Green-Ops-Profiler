# 1. lightweight base image with Python
FROM python:3.9-slim

# 2. the working directory inside the container
WORKDIR /app

# 3. Install system-level dependencies (needed for hardware monitoring)
# We need 'gcc' and 'python3-dev' for some AI packages to compile correctly
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy and install Python dependencies
# We do this before copying the code to leverage "Docker Layer Caching"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project code
COPY . .

# 6. Define the command to run your tool
CMD ["python", "main.py"]