FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy requirements lebih dulu agar proses build lebih cepat jika ada cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh folder proyek Anda ke dalam kontainer Docker
COPY . /app/

# Jalankan server Django di dalam Docker pada port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]