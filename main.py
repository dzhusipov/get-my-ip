from fastapi import FastAPI
import socket
import uvicorn

app = FastAPI()


@app.get("/get-my-ip")
async def get_my_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return {
        "hostname": hostname,
        "ip": ip
    }


@app.get("/")
async def root():
    return {
        "author": "DAsm",
        "version": "0.0.1"
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

