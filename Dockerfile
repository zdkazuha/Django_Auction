FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN python3.14 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3.14", "./manage.py", "runserver", "0.0.0.0:8000"]