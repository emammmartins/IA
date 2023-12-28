class Health_Planet:
    def __init__(self):
        self.dict_estafetas = {}  # Mapa de estafetas com ID como chave
        self.dict_encomendas = {}  # Mapa de encomendas com ID como chave
        self.tempo_virtual=0

    def add_estafeta(self, estafeta_id, estafeta_data):
        self.dict_estafetas[estafeta_id] = estafeta_data

    def remove_estafeta(self, estafeta_id):
        if estafeta_id in self.dict_estafetas.keys():
            del self.dict_estafetas[estafeta_id]
        else:
            print(f"Estafeta com ID {estafeta_id} não encontrado.")

    def ver_estafetas(self):
        for estafeta in self.dict_estafetas.values():
            print(estafeta)

    def existe_estafeta(self,id):
        if id in self.dict_estafetas.keys():
            return True
        return False

    def add_encomenda(self, encomenda_id, encomenda_data):
        self.dict_encomendas[encomenda_id] = encomenda_data

    def remove_encomenda(self, encomenda_id):
        if encomenda_id in self.dict_encomendas:
            del self.dict_encomendas[encomenda_id]
        else:
            print(f"Encomenda com ID {encomenda_id} não encontrada.")

    def ver_encomendas(self):
        for encomenda in self.dict_encomendas.values():
            print(encomenda)

    def ver_fila_estafeta(self, id_estafeta):
        self.dict_estafetas[id_estafeta].ver_encomendas_em_fila()

    def disponibilidade(self, meio_transporte):
        tempo_minimo_eletrico = float('inf')
        id_condutor_min_tempo_eletrico = None

        tempo_minimo_sem_ser_eletrico = float('inf')
        id_condutor_min_tempo_sem_ser_eletrico = None

        for condutor in self.dict_estafetas.values():
            if condutor.meio_de_transporte == meio_transporte:
                tempo_ate_disponivel = condutor.calcula_tempo_ate_disponivel()
                if tempo_ate_disponivel < tempo_minimo_eletrico and condutor.eletrico==True:
                    tempo_minimo_eletrico = tempo_ate_disponivel
                    id_condutor_min_tempo_eletrico = condutor.id
                elif(tempo_ate_disponivel < tempo_minimo_sem_ser_eletrico and condutor.eletrico==False):
                    tempo_minimo_sem_ser_eletrico=tempo_ate_disponivel
                    id_condutor_min_tempo_sem_ser_eletrico=condutor.id

        return tempo_minimo_eletrico, id_condutor_min_tempo_eletrico, tempo_minimo_sem_ser_eletrico, id_condutor_min_tempo_sem_ser_eletrico
    
    def atualiza_inicial(self,id_estafeta,tempo,velocidades_medias,caminho,id_encomenda,veiculo,eletrico,distancia):
        encomenda = self.dict_encomendas.get(id_encomenda)
        if encomenda is not None:
            encomenda.atualiza_encomenda_inicio(tempo,velocidades_medias,caminho,id_estafeta,veiculo,eletrico,distancia)
            self.dict_estafetas[id_estafeta].atualiza_estafeta_inicio(encomenda)

    def atualiza_estado(self,grafo,grafo_cortadas):
        self.tempo_virtual+=1
        for estafeta in self.dict_estafetas.values():
            if estafeta.encomenda_atual is not None:
                ultimo_lugar = estafeta.encomenda_atual.get_posicao(grafo,grafo_cortadas)
                estafeta.atualiza_estafeta_meio(ultimo_lugar)
            else:
                estafeta.comecar_nova_encomenda()
                

