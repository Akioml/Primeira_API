class Personagem():
    def __init__(self,
        id: int,
        nome: str,
        raca: str,
        classe: str,
        idade: int,
        dano: int,
        vida:int,
        mana:int,
        chance_critico:int,
        vida_maxima:int
        ):

        self.id = id
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.idade = idade
        self.dano = dano
        self.vida_maxima = vida_maxima
        self.vida = vida
        self.mana = mana
        self.chance_critico = chance_critico

    def receber_dano(self,dano:int):

        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0
    
    def curar(self,cura:int):

        self.vida += cura

        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima


    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "raca": self.raca,
            "classe": self.classe,
            "idade": self.idade,
            "dano": self.dano,
            "vida": self.vida,
            "vida_maxima":self.vida_maxima,
            "mana": self.mana,
            "chance_critico": self.chance_critico
        }


        