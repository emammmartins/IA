import sys
import time

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

    def add_encomenda(self, encomenda_id, encomenda_data):
        self.dict_encomendas[encomenda_id] = encomenda_data

    def remove_encomenda(self, encomenda_id):
        if encomenda_id in self.dict_encomendas:
            del self.dict_encomendas[encomenda_id]
        else:
            print(f"Encomenda com ID {encomenda_id} não encontrada.")

    def disponibilidade(self, meio_transporte):
        tempo_minimo = float('inf')
        id_condutor_min_tempo = None

        for condutor in self.estafetas:
            if condutor.meio_de_transporte == meio_transporte:
                if condutor.tempo_transporte == 0:
                    return 0, condutor.id
                elif condutor.tempo_transporte < tempo_minimo:
                    tempo_minimo = condutor.tempo_transporte
                    id_condutor_min_tempo = condutor.id

        return tempo_minimo, id_condutor_min_tempo
    
    def atualiza_estafeta(self,id_estafeta,tempo,velocida,caminho):
        print(caminho)
        self.dict_estafetas[id_estafeta].atualiza_estafeta(tempo,velocida,caminho)

    def atualiza_estado(self,grafo):
        time.sleep(2)
        self.tempo_virtual+=1

        for estafeta in self.dict_estafetas.values():
            if estafeta.tempo_transporte!=0:
                estafeta.tempo_transporte-=1
                estafeta.tempo_que_percorreu+=1

                tempo_acumulado=0
                posicao=0
                while(tempo_acumulado<estafeta.tempo_que_percorreu and posicao + 1 < len(estafeta.caminho)):
                    distancia=grafo[posicao][posicao+1]['weight']
                    tempo_aresta=(distancia/velocidade)*60
                    tempo_acumulado+=tempo_aresta
                    posicao+=posicao+1
                estafeta.ultimo_local_passou = estafeta.caminho[posicao] if posicao < len(estafeta.caminho) else None
                

