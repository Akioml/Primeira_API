from app.schemas.personagem_schema import PersonagemSchema
from app.services.personagem_services import criar_personagem
from app.services.combate_services import atacar
from app.services.personagem_services import obter_personagem_por_id

personagem01 = PersonagemSchema(
    nome="Arthur",
    raca="Humano",
    classe="Guerreiro",
    idade=30,
    vida=0,
    dano=25,
    mana=10
)

personagem02 = PersonagemSchema(
    nome="Merlin",
    raca="Humano",
    classe="Mago",
    idade=60,
    vida=25,
    dano=15,
    mana=100
)

criar_personagem(personagem01)
criar_personagem(personagem02)


resultado = atacar(1,2)

print(resultado)

personagem_encontrado = obter_personagem_por_id(1)

print(type(personagem_encontrado))
print(personagem_encontrado.nome)
print(personagem_encontrado.vida)