# Stage 1: Build dependencies
FROM python:3.12-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.12-slim

WORKDIR /app

COPY --from=build /install /usr/local
COPY . .

ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

EXPOSE 5000

# Use Gunicorn for production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
