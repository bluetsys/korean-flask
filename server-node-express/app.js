const express = require("express");
const os = require("os");

const app = express();

app.get("/", (req, res) => {
    res.send("Hello World");
});

app.get("/health", (req, res) => {
    res.send(os.hostname());
});

const HOST = process.argv[2];
const PORT = process.argv[3];

app.listen(PORT, HOST, () => {
    console.log(`Running on http://${HOST}:${PORT}`);
});