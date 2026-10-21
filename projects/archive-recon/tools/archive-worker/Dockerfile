FROM python:3.12-slim-bookworm
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu tesseract-ocr-rus tesseract-ocr-osd \
      rclone ca-certificates \
 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir pymupdf==1.28.2
COPY worker.py /app/worker.py
ENV PYTHONUNBUFFERED=1 OMP_THREAD_LIMIT=1 HOME=/tmp
USER 1000:1000
HEALTHCHECK --interval=60s --timeout=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=5)"
CMD ["python", "/app/worker.py"]
