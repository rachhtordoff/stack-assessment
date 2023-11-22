FROM python:3.10

WORKDIR /src/main

COPY . .

pip3 install flake8

CMD ["python", "/src/main.py"]
