# ww

```
docker build -t wymoon2690/www:linux/amd64 .
```

```
docker push wymoon2690/www:0.6.demo
```

```
sudo docker run -d -p 80:5000 --name korean-flask wymoon2690/korean-flask
```
docker buildx build --platform linux/arm/v7 -t wymoon2690/www:0.6.demo --push .
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -twymoon2690/www:0.6.demo --push .

docker buildx create --name builder
docker buildx use builder
docker buildx inspect --bootstrap
docker buildx build --platform linux/amd64,linux/arm64/v8 -t wymoon2690/korean-flask --push .

docker-compose build
docker-compose up -d --scale core-app=4 --no-recreate

docker-compose -f build
docker-compose -f docker-compose.yml up -d --scale core-app=4 --no-recreate

docker container stop korean-flask
docker container rm korean-flask

docker container stop korean-flask && docker container rm korean-flask
docker pull wymoon2690/korean-flask
docker run -d -p 80:5000 --name korean-flask wymoon2690/korean-flask

esptool.py --port COM4 --chip esp32 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
esptool.py --port COM4 --chip esp32 --baud 460800 write_flash -z 0x1000




docker buildx build --platform linux/amd64,linux/arm64/v8 -t wymoon2690/korean-flask:fastapi --push .
docker run -d -p 800:80 --name korean-flask wymoon2690/korean-flask:fastapi


docker build --tag fastapi:0.1 .
docker run --rm -p 8080:80 fastapi:0.1