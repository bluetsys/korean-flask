FROM openjdk-11-jdk
FROM python

RUN pip3 install konlpy
RUN git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git

RUN bash ./Mecab-ko-for-Google-Colab/install_mecab-ko_on_colab_light_220429.sh

RUN pip3 install -U flask
RUN git clone https://github.com/bluetsys/korean-flask.git

WORKDIR /korean-flask

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]