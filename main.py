
from fastapi import FastAPI, WebSocket
from typing import List
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

html = ""
with open('index.html', 'r') as f:
    html = f.read()

@app.get("/")
async def get():
    return HTMLResponse(html)


class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_text(data)


manager = ConnectionManager()


@app.websocket("/ws/{client_name}")
async def websocket_endpoint(websocket: WebSocket, client_name: str):
    await manager.connect(websocket)
    while True:
        data = await websocket.receive_text()
        time = datetime.datetime.now().strftime("%X")
        await manager.broadcast(f"{time} - {client_name}:   {data}")