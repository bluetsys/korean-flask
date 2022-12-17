FROM python

RUN pip3 install python-mecab-ko

COPY . /app
WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]