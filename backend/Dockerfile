# Backend Dockerfile for Python Voice Agent
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY . .

# Remove local .env file that conflicts with Docker environment
RUN rm -f .env.local

# Download AI models (turn detector)
RUN uv run agent.py download-files

# Create assets directory if it doesn't exist
RUN mkdir -p assets

# Expose port (not directly used but good for documentation)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:7880')" || exit 1

# Run the agent
CMD ["uv", "run", "agent.py", "dev"]