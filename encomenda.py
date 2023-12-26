class Encomenda:
    gera_ids = 1

    def __init__(self, peso, volume, tempo):
        self.id = Encomenda.gera_ids
        Encomenda.gera_ids += 1
        self.peso = peso
        self.volume = volume
        self.tempo = tempo

        #Entrega da encomenda
        self.id_estafeta = None
        self.tempo_previsto=0 #Tempo calculado para a viagem
        self.tempo_transporte=0 #Tempo de viagem que ainda falta fazer
        self.tempo_que_percorreu=0 #tempo que passou desde o inicio da viagem
        self.caminho=[]
        self.ultimo_local_passou="Armazem"
        self.velocidades_medias=[]
        self.chegou_ao_destino = False
        self.destino = None
        
    def __str__(self):
        return f"ID: {self.id}, Peso: {self.peso}, Volume: {self.volume}, Tempo máximo: {self.tempo}, Id do Estafeta: {self.id_estafeta},\nEncomenda Entregue: {self.chegou_ao_destino}, Último Local: {self.ultimo_local_passou}, Caminho: {self.caminho},\n Tempo de Transporte Previsto: {self.tempo_previsto}, Tempo total decorrido: {self.tempo_que_percorreu}, Tempo que ainda falta percorrer: {self.tempo_transporte}\n"

    def calcula_preco(self, meio_transporte):
        pass

    def atualiza_encomenda_inicio(self,tempo,velocidades_medias,caminho,id_estafeta):
        self.id_estafeta = id_estafeta
        self.ultimo_local_passou="Armazem"
        self.tempo_transporte=tempo
        self.tempo_previsto=tempo
        self.tempo_que_percorreu=0
        self.caminho=caminho
        self.velocidades_medias=velocidades_medias
        self.chegou_ao_destino=False
        self.destino = caminho[int((len(caminho)-1)/2)]

    def atualiza_encomenda_meio(self,posicao):
        if self.tempo_transporte!=0:
            self.tempo_que_percorreu+=1
            self.tempo_transporte-=1
            self.ultimo_local_passou=posicao
            if self.chegou_ao_destino == False and posicao==self.destino:
                print("A encomenda chegou ao destino")
                print(self.destino)
                self.destino = "Armazem"
                self.chegou_ao_destino = True
                if (atraso:= self.tempo_que_percorreu-(self.tempo_previsto/2)) > 0:
                    return atraso
                else:
                    return 0
            
        else:
            self.ultimo_local_passou="Armazem"
            return -2

        return -1

