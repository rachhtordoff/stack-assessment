FROM python:3.10

WORKDIR /src/main

COPY . .

CMD ["python", "/src/main.py"]
