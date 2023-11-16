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

        G.nodes['Armazem']['heuristica'] = {'SãoVicente': 5.8, 'Gualtar': 3, "Este":2,"SãoVitor":5.2,"SãoJoãoDoSouto":6,"Tenões":4.8,"Espinho":5.9,"SãoLázaro":7,"Lamaçães":6.4,"Nogueiró":5.9,"Fraião":7.5}
        G.nodes['SãoVicente']['heuristica']={"Gualtar":2.5,"SãoVitor":2,"Este":4.5,"SãoJoãoDoSouto":1.5,"Tenões":3.7,"SãoVicente":3.6,"Nogueiró":5.4,"Lamaçães":4.4,"Fraião":5,"SãoLázara":3.1}
        G.nodes['Gualtar']['heuristica']={"SãoVitor":2.4,"SãoJoãoDoSouto":3.2,"Este":2,"Tenões":2,"Espinho":4.5,"Nogueiró":3.7,"Lamaçães":3.5,"Faião":4.5,"SãoLázaro":3.7}
        G.nodes['SãoVitor']['heuristica']={"SãoJoãoDoSouto":1.9,"Tenões":2.2,"Espinho":2.2,"Nogueiró":3.5,"Lamaçães":2.5,"Fraião":3,"SãoLázaro":1.5,"Este":3.5}
        G.nodes['SãoJoãoDoSouto']['heuristica']={"SãoLázaro":2,"Fraião":4,"Lamaçães":3.6,"Nogueiró":5,"Espinho":6.6,"Tenões":3.5,"Este":4.6}
        G.nodes['SãoLázaro']['heuristica']={"Tenões":2.9,"Este":4.3,"Espinho":5.5,"Nogueiró":3.6,"Lamaçães":2.2,"Fraião":1.9}
        G.nodes[]


        return G