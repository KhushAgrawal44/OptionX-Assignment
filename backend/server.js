const WebSocket = require("ws");
const redis = require("redis");

const wss = new WebSocket.Server({ port: 8080 });

wss.on("connection", (ws) => {
  (async () => {
    const client = redis.createClient();

    const subscriber = client.duplicate();

    await subscriber.connect();

    await subscriber.subscribe("stock_channel", (message) => {
      ws.send(message);
    });
  })();

  ws.on("close", () => {
    console.log("Client disconnected");
  });
});
