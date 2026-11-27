FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Install minimal cloud runtime dependencies
RUN pip install --no-cache-dir "fastapi>=0.110.0" "uvicorn>=0.29.0" "pydantic>=2.6.0"

# Copy pre-built KB, servers, ETL, and eval scripts
COPY kb/ ./kb/
COPY servers/ ./servers/
COPY etl/ ./etl/
COPY configs/ ./configs/
COPY eval/ ./eval/

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import os, urllib.request; urllib.request.urlopen(f'http://127.0.0.1:{os.environ.get(\"PORT\", \"8080\")}/health')"

CMD ["sh", "-c", "uvicorn servers.rest_api:app --host 0.0.0.0 --port ${PORT:-8080}"]
