FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local

RUN apt-get update && apt-get install -y --no-install-recommends curl

RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY /app ./app

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
