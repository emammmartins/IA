import networkx as nx

def cria_grafo():

        # Criar um grafo valorado
        G = nx.Graph()

        # Adicionar nós ao grafo
        G.add_node("Armazem", label="Armazem")  # O nó "C" tem o nome "C"
        G.add_node("Gualtar", label="Gualtar")  # O nó "C" tem o nome "C"
        G.add_node("Este", label="Este")  # O nó "C" tem o nome "C"
        G.add_node("Espinho", label="Espinho")  # O nó "C" tem o nome "C"
        G.add_node("Tenões", label="Tenões")  # O nó "C" tem o nome "C"
        G.add_node("Nogueiró", label="Nogueiró")  # O nó "C" tem o nome "C"
        G.add_node("Lamaçães", label="Lamaçães")  # O nó "C" tem o nome "C"
        G.add_node("SãoVitor", label="SãoVitor")  # O nó "B" tem o nome "B"
        G.add_node("SãoJoãoDoSouto", label="SãoJoãoDoSouto")  # O nó "C" tem o nome "C"
        G.add_node("SãoVicente", label="SãoVicente")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Dume", label="Dume")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Frossos", label="Frossos")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Real", label="Real")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Semelhe", label="Semelhe")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Sé", label="Sé")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Cividade", label="Cividade")  # O nó "C" tem o nome "C"
        G.add_node("Maximinos", label="Maximinos")  # O nó "C" tem o nome "C"
        G.add_node("Ferreiros", label="Ferreiros")  # O nó "São Vicente" tem o nome "A"
        G.add_node("Gondizalves", label="Gondizalves")  # O nó "B" tem o nome "B"
        G.add_node("Lomar", label="Lomar")  # O nó "B" tem o nome "B"
        G.add_node("Arcos", label="Arcos")  # O nó "B" tem o nome "B"
        G.add_node("Nogueira", label="Nogueira")  # O nó "C" tem o nome "C"
        G.add_node("Fraião", label="Fraião")  # O nó "C" tem o nome "C"
        G.add_node("SãoLázaro", label="SãoLázaro")  # O nó "B" tem o nome "B"



        # Adicionar arestas valoradas ao grafo
        G.add_edge("Armazem", "Gualtar", weight=6)
        G.add_edge("Gualtar", "SãoVitor", weight=4)
        G.add_edge("Gualtar", "Tenões", weight=4)
        G.add_edge("Gualtar", "Este", weight=4)
        G.add_edge("Este", "Espinho", weight=5)
        G.add_edge("Este", "Tenões", weight=2)
        G.add_edge("Espinho", "Nogueiró", weight=4)
        G.add_edge("Tenões", "Nogueiró", weight=2)
        G.add_edge("Nogueiró", "SãoVitor", weight=8)
        G.add_edge("Lamaçães", "Nogueiró", weight=2)
        G.add_edge("Lamaçães", "Fraião", weight=1)
        G.add_edge("Fraião", "Nogueira", weight=2)
        G.add_edge("Tenões", "SãoVitor", weight=4)
        G.add_edge("SãoVitor", "Fraião", weight=6)
        G.add_edge("SãoVitor", "Lamaçães", weight=4)
        G.add_edge("SãoVicente", "SãoVitor", weight=4)
        G.add_edge("Fraião", "SãoLázaro", weight=4)
        G.add_edge("SãoLázaro", "Cividade", weight=2)
        G.add_edge("SãoJoãoDoSouto", "Cividade", weight=1)
        G.add_edge("SãoJoãoDoSouto", "SãoVicente", weight=3)
        G.add_edge("Sé", "SãoVicente", weight=2)
        G.add_edge("Sé", "SãoJoãoDoSouto", weight=1)
        G.add_edge("Sé", "Cividade", weight=1)
        G.add_edge("Cividade", "Maximinos", weight=2)
        G.add_edge("Maximinos", "Sé", weight=3)
        G.add_edge("Sé", "Real", weight=2)
        G.add_edge("Real", "Frossos", weight=2)
        G.add_edge("Real", "SãoVicente", weight=4)
        G.add_edge("Real", "Dume", weight=4)
        G.add_edge("Dume", "SãoVicente", weight=4)
        G.add_edge("Dume", "Frossos", weight=4)
        G.add_edge("Frossos", "Semelhe", weight=8)
        G.add_edge("Semelhe", "Gondizalves", weight=2)
        G.add_edge("Gondizalves", "Ferreiros", weight=4)
        G.add_edge("Ferreiros", "Maximinos", weight=4)
        G.add_edge("Maximinos", "Gondizalves", weight=2)
        G.add_edge("Ferreiros", "Lomar", weight=3)
        G.add_edge("Maximinos", "Lomar", weight=4)
        G.add_edge("Lomar", "Arcos", weight=3)
        G.add_edge("Nogueira", "Arcos", weight=6)
        G.add_edge("Nogueira", "Lomar", weight=8)
        G.add_edge("Lomar", "SãoLázaro", weight=6)

        G.nodes['Armazem']['heuristica'] = {'Armazem':0, 'SãoVicente':9.1, 'Gualtar':5.8, "Este":6.8,"SãoVitor":10,"SãoJoãoDoSouto":11.5,"Tenões":9,"Espinho":11.4,"SãoLázaro":11,"Lamaçães":12.4,"Nogueiró":11.8,"Fraião":14.9}
        G.nodes['SãoVicente']['heuristica']={'Armazem':9.1, 'SãoVicente':0, "Gualtar":4.7,"Este":8.3,"SãoVitor":3.6,"SãoJoãoDoSouto":2.8,"Tenões":7.2,"Espinho":13,"SãoLázaro":6,"Lamaçães":8.3,"Nogueiró":10.2,"Fraião":9.6}
        G.nodes['Gualtar']['heuristica']= {'Armazem':5.8, 'SãoVicente':4.7, "Gualtar":0,"Este":3.6,"SãoVitor":4,"SãoJoãoDoSouto":5.9,"Tenões":3.8,"Espinho":8.5,"SãoLázaro":7.1,"Lamaçães":6.6,"Nogueiró":6.7,"Fraião":8.8}
        G.nodes['Este']['heuristica']= {'Armazem':6.8, 'SãoVicente':8.3, "Gualtar":3.6,"Este":0,"SãoVitor":6.6,"SãoJoãoDoSouto":9,"Tenões":2.8,"Espinho":4.8,"SãoLázaro":8.4,"Lamaçães":6,"Nogueiró":4.4,"Fraião":8}
        G.nodes['SãoVitor']['heuristica']= {'Armazem':10, 'SãoVicente':3.6, "Gualtar":4,"Este":6.6,"SãoVitor":0,"SãoJoãoDoSouto":2.4,"Tenões":4,"Espinho":10.1,"SãoLázaro":2.8,"Lamaçães":4.6,"Nogueiró":6.8,"Fraião":6}
        G.nodes['SãoJoãoDoSouto']['heuristica']= {'Armazem':11.5, 'SãoVicente':2.8, "Gualtar":5.9,"Este":9,"SãoVitor":2.4,"SãoJoãoDoSouto":0,"Tenões":6.6,"Espinho":12.7,"SãoLázaro":3.7,"Lamaçães":6.9,"Nogueiró":9.4,"Fraião":7.5}
        G.nodes['Tenões']['heuristica']= {'Armazem':9, 'SãoVicente':7.2, "Gualtar":3.8,"Este":2.8,"SãoVitor":4,"SãoJoãoDoSouto":6.6,"Tenões":0,"Espinho":5.8,"SãoLázaro":5.2,"Lamaçães":2.8,"Nogueiró":2.7,"Fraião":5}
        G.nodes['Espinho']['heuristica']= {'Armazem':11.4, 'SãoVicente':13, "Gualtar":8.5,"Este":4.8,"SãoVitor":10.1,"SãoJoãoDoSouto":12.7,"Tenões":5.8,"Espinho":0,"SãoLázaro":10.7,"Lamaçães":6.8,"Nogueiró":3.8,"Fraião":8.5}
        G.nodes['SãoLázaro']['heuristica']= {'Armazem':11, 'SãoVicente':6, "Gualtar":7.1,"Este":8.4,"SãoVitor":2.8,"SãoJoãoDoSouto":3.7,"Tenões":5.2,"Espinho":10.7,"SãoLázaro":0,"Lamaçães":3.8,"Nogueiró":7,"Fraião":3.6}
        G.nodes['Lamaçães']['heuristica']= {'Armazem':12.4, 'SãoVicente':8.3, "Gualtar":6.6,"Este":6,"SãoVitor":4.6,"SãoJoãoDoSouto":6.9,"Tenões":2.8,"Espinho":6.8,"SãoLázaro":3.8,"Lamaçães":0,"Nogueiró":2.8,"Fraião":1.7}
        G.nodes['Nogueiró']['heuristica']= {'Armazem':11.8, 'SãoVicente':10.2, "Gualtar":6.7,"Este":4.4,"SãoVitor":6.8,"SãoJoãoDoSouto":9.4,"Tenões":2.7,"Espinho":3.8,"SãoLázaro":7,"Lamaçães":2.8,"Nogueiró":0,"Fraião":4.6}
        G.nodes['Fraião']['heuristica']= {'Armazem':14.9, 'SãoVicente':9.6, "Gualtar":8.8,"Este":8,"SãoVitor":6,"SãoJoãoDoSouto":7.5,"Tenões":5,"Espinho":8.5,"SãoLázaro":3.6,"Lamaçães":1.7,"Nogueiró":4.6,"Fraião":0}
        

        return G