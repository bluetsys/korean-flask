const http = require('http');
const os = require("os");

const app = require('http');

// app.get("/", (req, res) => {
//     res.send("Hello World");
// });

// app.get("/health", (req, res) => {
//     res.send(os.hostname());
// });

const HOST = process.argv[2];
const PORT = process.argv[3];

console.log(`Running on http://${HOST}:${PORT}`);

http.createServer((req, res) => {
  console.log(req.url)
  if( req.url ==='/')
  {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World');
  }
}).listen(PORT);