## --------------------------------------------------------------
## Base Image
## --------------------------------------------------------------
FROM python:3.12-slim


## --------------------------------------------------------------
## Environment settings
## --------------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


## --------------------------------------------------------------
## Working directory
## --------------------------------------------------------------
WORKDIR /app


# Install essential system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


# Copy project files into the container
COPY . .


# Install Python dependencies in editable mode
RUN pip install --no-cache-dir -e .


# Expose Streamlit’s default port
EXPOSE 8501


# Launch the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
