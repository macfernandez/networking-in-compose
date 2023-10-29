import os
import typer
from typing import Optional

import uvicorn
from fastapi import FastAPI

from app import converters


PORT = os.getenv("BACKEND_PORT")

server_app = typer.Typer()

server = FastAPI()
server.include_router(converters.router)


@server_app.command()
def run_server(
    host: Optional[str] = "0.0.0.0",
    port: Optional[int] = PORT
):
    uvicorn.run(server, host=host, port=port)


server_app()
