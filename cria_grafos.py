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

        G.nodes['Armazem']['heuristica'] = {'SãoVicente': 11.6, 'Gualtar': 6, "Este":4,"SãoVitor":10.4,"SãoJoãoDoSouto":12,"Tenões":9.6,"Espinho":11.8,"SãoLázaro":14,"Lamaçães":12.8,"Nogueiró":11.8,"Fraião":15}
        G.nodes['SãoVicente']['heuristica']={"Gualtar":5,"SãoVitor":4,"Este":9,"SãoJoãoDoSouto":3,"Tenões":7.4,"SãoVicente":7.2,"Nogueiró":10.8,"Lamaçães":8.8,"Fraião":10,"SãoLázara":6.2}
        G.nodes['Gualtar']['heuristica']={"SãoVitor":4.8,"SãoJoãoDoSouto":6.4,"Este":4,"Tenões":4,"Espinho":9,"Nogueiró":7.4,"Lamaçães":7,"Faião":9,"SãoLázaro":7.4}
        G.nodes['SãoVitor']['heuristica']={"SãoJoãoDoSouto":3.8,"Tenões":4.4,"Espinho":4.4,"Nogueiró":7,"Lamaçães":5,"Fraião":6,"SãoLázaro":3,"Este":7}
        G.nodes['SãoJoãoDoSouto']['heuristica']={"SãoLázaro":4,"Fraião":8,"Lamaçães":7.2,"Nogueiró":10,"Espinho":13.2,"Tenões":7,"Este":9.2}
        G.nodes['SãoLázaro']['heuristica']={"Tenões":5.8,"Este":8.6,"Espinho":11,"Nogueiró":7.2,"Lamaçães":4.4,"Fraião":3.8}


        return G