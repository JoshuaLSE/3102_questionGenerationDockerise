FROM python:3.10

WORKDIR /qGen

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN --network='ict3102_default'

COPY . .
CMD ["python","./main.py"]