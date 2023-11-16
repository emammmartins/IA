class Estafeta:
    gera_ids=1
    def __init__(self,nome,meio_de_transporte):
        self.id=Estafeta.gera_ids
        Estafeta.gera_ids+=1
        self.nome=nome
        self.meio_de_transporte=meio_de_transporte
        self.tempo_disponivel=None

    def __str__(self):
        if(self.meio_de_transporte==1):
            transporte="Bicicleta"
        elif(self.meio_de_transporte==2):
            transporte="Moto"
        elif(self.meio_de_transporte==3):
            transporte="Carro"
        return f"ID: {self.id}, Nome: {self.nome}, Meio de Transporte: {transporte}"
    
    def atualiza_tempo_disponivel(self,tempo):
        if(self.tempo_disponivel==None):
            self.tempo_disponivel=tempo
        else:
            self.tempo_disponivel+=tempo

