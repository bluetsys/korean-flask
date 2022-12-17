FROM openjdk-11-jdk
FROM python

RUN pip3 install konlpy
RUN pip3 install -U flask

RUN git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
WORKDIR /Mecab-ko-for-Google-Colab
RUN bash ./install_mecab-ko_on_colab_light_220429.sh

COPY . /app

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]