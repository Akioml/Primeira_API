from pydantic import BaseModel

class PersonagemSchema(BaseModel):
    nome: str
    raca: str
    classe: str
    idade: int
    vida: int
    dano: int
    mana: int
    chance_critico: int


