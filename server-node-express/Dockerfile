FROM node

WORKDIR /app
COPY . /app

RUN npm install

EXPOSE 8015
ENTRYPOINT ["node", "app.js", "0.0.0.0", "8015"]