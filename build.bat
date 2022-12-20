docker build -t wymoon2690/dotnet-webapi ./server-dotnet-webapi/.
docker push wymoon2690/dotnet-webapi

docker build -t wymoon2690/python-django ./server-python-django/.
docker push wymoon2690/python-django

docker build -t wymoon2690/python-fastapi ./server-python-fastapi/.
docker push wymoon2690/python-fastapi

docker build -t wymoon2690/python-flask ./server-python-flask/.
docker push wymoon2690/python-flask