FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# COPY FIRST (important fix)
COPY requirements.txt .

# NOW install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of project
COPY . .

CMD ["python", "src/main.py"]