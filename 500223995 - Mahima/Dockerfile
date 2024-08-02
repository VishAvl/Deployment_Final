FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# Upgrade pip
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["flask", "run", "--host=0.0.0.0"]

