FROM python:3.12.2-slim

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "--host=0.0.0.0", "--port=80"]