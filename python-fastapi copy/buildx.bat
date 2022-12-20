docker buildx build --platform linux/amd64,linux/arm64/v8 -t wymoon2690/korean-fastapi --push .
docker run -it -p 8002:80 --name korean-fastapi wymoon2690/korean-fastapi