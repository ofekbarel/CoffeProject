FROM python:3.8-slim  

WORKDIR /app

RUN pip install flask flask_login flask_sqlalchemy bcrypt psycopg2

COPY . .  

EXPOSE 5000  

CMD ["python3", "main.py"]
