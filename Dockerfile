FROM openjdk:21-jdk
FROM python

RUN pip3 install konlpy
RUN pip3 install -U flask

COPY . /app
WORKDIR /app

RUN bash ./install_mecab.sh

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]