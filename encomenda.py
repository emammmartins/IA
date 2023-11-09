class Encomenda:
    gera_ids = 1

    def __init__(self, peso, volume, tempo):
        self.id = Encomenda.gera_ids
        Encomenda.gera_ids += 1
        self.peso = peso
        self.volume = volume
        self.tempo = tempo
        
    def __str__(self):
        return f"ID: {self.id}, Peso: {self.peso}, Volume: {self.volume}, Tempo: {self.tempo}"

    def calcula_preco(self, meio_transporte):
        pass

