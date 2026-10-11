import http from 'http';
import fs from 'fs';
import { WebSocketServer } from 'ws';

const PORT = 3001;

const server = http.createServer((req, res) => {
  fs.readFile("./public/index.html", (err, data) => {
    if (err) {
      res.writeHead(500, { "Content-Type": "text/plain" });
      res.end("Error loading index.html");
      return;
    }
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(data);
  });
});

const wss = new WebSocketServer({ server });

wss.on("connection", (socket, req) => {
  const username = new URL(req.url, "http://localhost").searchParams.get(
    "username",
  );

  const joinPayload = JSON.stringify({
    type: "system",
    text: `${username} joined`,
  });
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(joinPayload);
    }
  });

  socket.on("message", (data) => {
    try {
      const { username, text } = JSON.parse(data.toString());
      const chatPayload = JSON.stringify({ type: "chat", username, text });
      wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(chatPayload);
        }
      });
    } catch (err) {
      console.error("Invalid message received:", err.message);
    }
  });

  socket.on("close", () => {
    const leavePayload = JSON.stringify({
      type: "system",
      text: `${username} left`,
    });
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(leavePayload);
      }
    });
  });
});

server.listen(PORT, () => {
  console.log(`Chat server running at http://localhost:${PORT}`);
});