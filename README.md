# ww

```
docker build -t wymoon2690/www:0.6.demo .
```

```
docker push wymoon2690/www:0.6.demo
```

```
sudo docker run -d -p 5000:5000 --name www wymoon2690/www:0.6.demo
```
docker buildx build --platform linux/arm/v7 -twymoon2690/www:0.6.demo --push .
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -twymoon2690/www:0.6.demo --push .