from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.personagem_schema import PersonagemSchema

from app.services.personagem_services import (
    listar_personagens,
    criar_personagem,
    obter_personagem_por_id,
    atualizar_personagem,
    deletar_personagem, 
)

from app.services.combate_services import (
    atacar,
    curar
)

router = APIRouter(
    prefix="/personagens",
    tags=["personagens"]
)

@router.get("/")
def get_personagens():
    return listar_personagens()

@router.post("/")
def post_personagem(personagem: PersonagemSchema):
    return criar_personagem(personagem)

@router.get("/status")
def status_servidor():
    return {"status": "Servidor funcionando"}

@router.get("/{id}")
def get_id_personagem(id: int):
    personagem = obter_personagem_por_id(id)

    if personagem is None:
        raise HTTPException(status_code=404, detail="Personagem não existe")

    return personagem.to_dict()


@router.put("/{id}")
def atualizar(id: int, personagem: PersonagemSchema):
    personagem_atualizado = atualizar_personagem(id,personagem)

    if personagem_atualizado is None:
        raise HTTPException(status_code=404, detail="Personagem não existe")
    
    return personagem_atualizado

@router.delete("/{id}")
def deletar(id: int):
    personagem_para_deletar = deletar_personagem(id)

    if personagem_para_deletar is None:
        raise HTTPException(status_code=404, detail="Personagem não existe")
    
    return personagem_para_deletar

@router.post("/{id_atacante}/atacar/{id_alvo}")
def atacar_personagem(id_atacante:int, id_alvo:int):
    resultado = atacar(id_atacante ,id_alvo)

    if resultado is None:
        raise HTTPException(status_code = 404, detail = "Atacante ou alvo não encontrado."  )    
    
    return resultado

@router.post("/{id_personagem}/curar/{quantidade}")
def curar_personagem(id_personagem:int,quantidade:int):
    resultado = curar(id_personagem, quantidade)

    if resultado is None:
        raise HTTPException(status_code = 404, detail = "Personagem não encontrado.")
    
    return resultado