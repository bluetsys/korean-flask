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