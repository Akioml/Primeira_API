from app.database import fake_database
from app.models.personagem import Personagem
from app.schemas.personagem_schema import PersonagemSchema

def listar_personagens():
    return fake_database.personagens

def criar_personagem(personagem):

    novo_personagem = Personagem(
        id=fake_database.proximo_id,
        nome=personagem.nome,
        raca=personagem.raca,
        classe=personagem.classe,
        idade=personagem.idade,
        dano=personagem.dano,
        vida=personagem.vida,
        vida_maxima=personagem.vida,
        mana=personagem.mana,
        chance_critico=personagem.chance_critico
    )

    fake_database.personagens.append(novo_personagem)
    fake_database.proximo_id = fake_database.proximo_id + 1
    

    return novo_personagem

def obter_personagem_por_id(id: int):
    for personagem in fake_database.personagens:
        if personagem.id == id:
            return personagem
        
    return None
        
def atualizar_personagem(id: int, dados:PersonagemSchema):
    for personagem in fake_database.personagens:
        if personagem.id == id:
            personagem.nome = dados.nome
            personagem.raca = dados.raca
            personagem.classe = dados.classe
            personagem.idade =  dados.idade
            personagem.dano =   dados.dano
            personagem.vida =   dados.vida
            personagem.vida_maxima = dados.vida,
            personagem.mana =   dados.mana
            personagem.chance_critico = dados.chance_critico

            return personagem
        
    return None 

def deletar_personagem(id: int):
    for personagem in fake_database.personagens:
        if personagem.id == id:
            fake_database.personagens.remove(personagem)

            return personagem
        
    return None 
