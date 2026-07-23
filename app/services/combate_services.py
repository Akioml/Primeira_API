import random


from app.services.personagem_services import obter_personagem_por_id


def atacar(id_atacante: int, id_alvo: int):
    atacante = obter_personagem_por_id(id_atacante)
    alvo = obter_personagem_por_id(id_alvo)

    if atacante is None or alvo is None:
        return None 

    if not atacante.esta_vivo:
        return {"Mensagem":f"{atacante.nome} está morto e não pode atacar."}
    
    if not alvo.esta_vivo:
            return {"Mensagem":f"{alvo.nome} está morto e não pode atacar."}
    
    dano_final = atacante.dano 

    numero_sortedeado = random.randint(1,100)

    foi_critico = numero_sortedeado <= atacante.chance_critico

    if foi_critico:
          dano_final  *= 2

        
    alvo.receber_dano(dano_final)


    if alvo.vida == 0:
        return {
            "mensagem": (
                f"{atacante.nome} atacou {alvo.nome}, "
                f"causou {dano_final} de dano e o derrotou."
            ),
            "atacante": atacante.nome,
            "alvo": alvo.nome,
            "dano_causado": dano_final,
            "golpe_critico": foi_critico,
            "vida_restante": alvo.vida,
            "alvo_derrotado": True
        }

   
    return {
        "mensagem": (
            f"{atacante.nome} atacou {alvo.nome}, "
            f"causando {dano_final} de dano."
        ),
        "atacante": atacante.nome,
        "alvo": alvo.nome,
        "dano_causado": dano_final,
        "golpe_critico": foi_critico,
        "vida_restante": alvo.vida,
        "alvo_derrotado": False
    }


def curar(id_personagem: int, quantidade: int):
      personagem = obter_personagem_por_id(id_personagem)
      cura = quantidade

      if personagem is None:
            return None
      
      if personagem.vida <= 0:
            return {"Mensagem":f"{personagem.nome} está morto e não pode ser curado!."}
      
      if personagem.vida == personagem.vida_maxima:
           return {"Mensagem":f"{personagem.nome} está com a vida cheia e não pode ser currado Pontos de vida: {personagem.vida_maxima}!"}

      vida_antes = personagem.vida
      
      personagem.vida += cura

      personagem.curar(cura)

      vida_restaurada = personagem.vida - vida_antes
            
      return {
        "mensagem": (
            f"{personagem.nome} restaurou"
            f"{vida_restaurada} ponto de vida"
        ),
        "personagem": personagem.nome,
        "cura_solicitada": cura,
        "vida_restaurada": vida_restaurada,
        "vida_restante": personagem.vida,
        "vida_maxima": personagem.vida_maxima,
        "alvo_derrotado": not personagem.esta_vivo()
      }


      
      
      
      




