class Estafeta:
    gera_ids=1
    def __init__(self,nome,meio_de_transporte):
        self.id=Estafeta.gera_ids
        Estafeta.gera_ids+=1
        self.nome=nome
        self.meio_de_transporte=meio_de_transporte

        #Cenas para o avancar no tempo
        self.tempo_transporte=0
        self.tempo_que_percorreu=0
        self.caminho=[]
        self.ultimo_local_passou=None
        self.velocidade_media=0


    def __str__(self):
        meio_transporte = ""
        if self.meio_de_transporte == 1:
            meio_transporte = "Bicicleta"
        elif self.meio_de_transporte == 2:
            meio_transporte = "Moto"
        elif self.meio_de_transporte == 3:
            meio_transporte = "Carro"

        return f"ID: {self.id}, Nome: {self.nome}, Meio de Transporte: {meio_transporte}\n Último Local: {self.ultimo_local_passou}, Tempo de Transporte Restante: {self.tempo_transporte}, Tempo Percorrido: {self.tempo_que_percorreu}, Caminho: {self.caminho} "
    
    def atualiza_estafeta_inicio(self,tempo,velocida,caminho):
        self.tempo_transporte=tempo
        self.tempo_que_percorreu=0
        self.caminho=caminho
        self.ultimo_local_passou=None
        self.velocidade_media=velocida

