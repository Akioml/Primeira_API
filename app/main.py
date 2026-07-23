from fastapi import FastAPI

from app.routers import personagem

app = FastAPI(
    title="RPG API",
    description="API para gerenciamento de personagens e combate de um RPG",
    version="1.0.0"
)

app.include_router(personagem.router)

@app.get("/")
def home():
    return {"mensagem": "API do RPG"}