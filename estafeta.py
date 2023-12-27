from queue import Queue

class Estafeta:
    gera_ids=1
    def __init__(self,nome,meio_de_transporte,eletrico):
        self.id=Estafeta.gera_ids
        Estafeta.gera_ids+=1
        self.nome=nome
        self.meio_de_transporte=meio_de_transporte
        self.eletrico=eletrico
        self.soma_classificacoes = 0
        self.n_viagens = 0

        #Guarda as encomendas que estão em espera
        self.fila_encomendas = Queue()  # Mapa de encomendas com ID como chave

        #Cenas para o avancar no tempo
        self.pausa=0
        self.encomenda_atual = None


    def __str__(self):
        meio_transporte = ""
        if self.meio_de_transporte == 1:
            meio_transporte = "Bicicleta"
        elif self.meio_de_transporte == 2:
            meio_transporte = "Moto"
        elif self.meio_de_transporte == 3:
            meio_transporte = "Carro"

        return f"ID: {self.id}, Nome: {self.nome}, Meio de Transporte: {meio_transporte}, Elétrico: {self.eletrico}, Classificação: {self.calcula_classificacao()}\n Encomenda: {self.encomenda_atual}"
    

    #Calculos
    def calcula_classificacao(self):
        if self.n_viagens == 0:
            return 5.0
        else:
            return self.soma_classificacoes/self.n_viagens

    def calcula_tempo_ate_disponivel(self):
        tempo_acumulado = 0
        tempo_acumulado += self.pausa
        copia_fila = list(self.fila_encomendas.queue)
        for encomenda in copia_fila:
            tempo_acumulado += encomenda.tempo_previsto
            tempo_acumulado += 2 #Margem por entrega
        if self.encomenda_atual is not None:
            tempo_acumulado += self.encomenda_atual.tempo_transporte
            tempo_acumulado += 2 #Margem entrega atual
        return tempo_acumulado
    
    #Queue
    def push_encomenda(self, encomenda):
        self.fila_encomendas.put(encomenda)

    def pop_encomenda(self):
        if not self.fila_encomendas.empty():
            encomenda = self.fila_encomendas.get()
            return encomenda
        else:
            return None

    def ver_encomendas_em_fila(self):
        copia_fila = list(self.fila_encomendas.queue)
        for encomenda in copia_fila:
            print(encomenda)

    #Tempo
    def aumenta_pausa(self, atraso):
        self.pausa += atraso

    def atualiza_estafeta_inicio(self,encomenda):
        if self.encomenda_atual is None:
            self.encomenda_atual = encomenda
        else:
            self.push_encomenda(encomenda)

    def atualiza_estafeta_meio(self,posicao):
        if self.pausa>0:
            self.pausa-=1
            self.encomenda_atual.tempo_que_percorreu+=1
        else:
            if (atraso:=self.encomenda_atual.atualiza_encomenda_meio(posicao))>=0:
                #print (f'atraso {atraso}')
                if atraso > 0:
                    self.n_viagens+=1
                    atraso = atraso-5 #Tolerância de 5 minutos para atrasos
                    if atraso<0:
                        atraso=0
                    classificacao = 5-(atraso*0.1)
                    if classificacao<0:
                        classificacao=0
                    self.soma_classificacoes+=classificacao
                else:
                    #print("Sem atraso")
                    self.n_viagens+=1
                    self.soma_classificacoes+=5
            elif atraso==-2:
                self.encomenda_atual = None

    def comecar_nova_encomenda (self):
        if self.pausa>0:
            self.pausa-=1
        self.encomenda_atual = self.pop_encomenda()
