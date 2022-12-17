FROM python

RUN apt update -y -qq
RUN apt upgrade -y -qq

RUN pip3 install konlpy
RUN git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git

RUN bash ./Mecab-ko-for-Google-Colab/install_mecab-ko_on_colab_light_220429.sh