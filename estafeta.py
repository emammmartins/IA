class Estafeta:
    gera_ids=1
    def __init__(self,nome,meio_de_transporte):
        self.id=Estafeta.gera_ids
        Estafeta.gera_ids+=1
        self.nome=nome
        self.meio_de_transporte=meio_de_transporte
        self.soma_classificacoes = 0
        self.n_viagens = 0

        #Cenas para o avancar no tempo
        self.pausa=0
        self.tempo_previsto=0
        self.tempo_transporte=0
        self.tempo_que_percorreu=0
        self.caminho=[]
        self.ultimo_local_passou="Armazem"
        self.velocidades_medias=[]
        self.chegou_ao_destino = False
        self.destino = None


    def __str__(self):
        meio_transporte = ""
        if self.meio_de_transporte == 1:
            meio_transporte = "Bicicleta"
        elif self.meio_de_transporte == 2:
            meio_transporte = "Moto"
        elif self.meio_de_transporte == 3:
            meio_transporte = "Carro"

        return f"ID: {self.id}, Nome: {self.nome}, Meio de Transporte: {meio_transporte}\n Último Local: {self.ultimo_local_passou}, Tempo de Transporte Previsto: {self.tempo_previsto}, Tempo Percorrido: {self.tempo_que_percorreu}, Caminho: {self.caminho},\nEncomenda Entregue: {self.chegou_ao_destino}, Classificação: {self.calcula_classificacao()}\n "
    

    def calcula_classificacao(self):
        if self.n_viagens == 0:
            return 5.0
        else:
            return self.soma_classificacoes/self.n_viagens


    def aumenta_pausa(self, atraso):
        self.pausa += atraso

    def atualiza_estafeta_inicio(self,tempo,velocidades_medias,caminho):
        self.ultimo_local_passou="Armazem"
        self.tempo_transporte=tempo
        self.tempo_previsto=tempo
        self.tempo_que_percorreu=0
        self.caminho=caminho
        self.velocidades_medias=velocidades_medias
        self.chegou_ao_destino=False
        self.destino = caminho[int((len(caminho)-1)/2)]

    def atualiza_estafeta_meio(self,posicao):
        if self.pausa>0:
            self.pausa-=1
        else:
            if self.tempo_transporte!=0:
                self.tempo_que_percorreu+=1
                self.tempo_transporte-=1
                self.ultimo_local_passou=posicao
                if self.chegou_ao_destino == False and posicao==self.destino:
                    print("A encomenda chegou ao destino")
                    print(self.destino)
                    self.destino = "Armazem"
                    self.chegou_ao_destino = True
                    #Alterar estado da encomenda
                    if atraso:= self.tempo_que_percorreu-(self.tempo_previsto/2) > 0:
                        self.n_viagens+=1
                        atraso = atraso-5 #Tolerância de 5 minutos para atrasos
                        if atraso<0:
                            atraso=0
                        classificacao = 5-(atraso*0.1)
                        if classificacao<0:
                            classificacao=0
                        self.soma_classificacoes+=classificacao
                    else:
                        self.n_viagens+=1
                        self.soma_classificacoes+=5

            else:
                self.ultimo_local_passou="Armazem"
                self.tempo_que_percorreu=0
                self.tempo_transporte=0
                self.tempo_previsto=0
                self.caminho=[]
                self.velocidades_medias=[]
        


