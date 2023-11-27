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

    def disponibilidade(self,meio_transporte):
        tempo_minimo=sys.maxsize
        id_condutor_min_tempo=None
        for condutor in self.dict_estafetas.values():
            if(condutor.meio_de_transporte==meio_transporte):
                if(condutor.tempo_disponivel==None):
                    return 0 ,condutor.id
                elif (condutor.tempo_disponivel<tempo_minimo):
                    tempo_minimo=condutor.tempo_disponivel
                    id_condutor_min_tempo=condutor.id
        return tempo_minimo, id_condutor_min_tempo
    
    def atualiza_tempo_estafeta(self,id_estafeta,tempo):
        self.dict_estafetas[id_estafeta].atualiza_tempo_disponivel(tempo)

    def atualiza_estado(self):
        time.sleep(2)

        self.tempo_virtual+=1
        for estafeta in self.dict_estafetas.values():
            if estafeta.tempo_transporte!=0:
                estafeta.tempo_transporte-=1
                estafeta.tempo_que_percorreu+=1

                tempo=0
                while(tempo<estafeta.tempo_que_percorreu):
                    pass
                    #falta ver onde o mano esta

