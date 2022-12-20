FROM wymoon2690/python-mecab-ko

WORKDIR /app
COPY . ./app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]