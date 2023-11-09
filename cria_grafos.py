import networkx as nx
import matplotlib.pyplot as plt
import sys

def cria_grafo_nao_orientado():
    # Criar um grafo não orientado
    G = nx.Graph()

    # Adicionar freguesias de Braga como nós ao grafo
    freguesias_braga = ['São Vicente', 'São Vítor', 'São João do Souto', 'Maximinos',
                    'Santa Tecla', 'Cividade', 'Nogueiró', 'Fraião',
                    'Gualtar', 'São Pedro', 'São José de São Lázaro', 'Lomar',
                    'Real', 'Este', 'São Lourenço', 'São Tiago', 'Merelim São Pedro',
                    'Merelim São Paio', 'Espinho', 'Padim da Graça']

    G.add_nodes_from(freguesias_braga)

    # Adicionar arestas com distâncias fictícias entre as freguesias
    arestas = [('São Vicente', 'São Vítor', {'distancia': 2}),
            ('São Vicente', 'São João do Souto', {'distancia': 3}),
            ('São Vítor', 'Maximinos', {'distancia': 4}),
            ('São João do Souto', 'Maximinos', {'distancia': 5}),
            ('Santa Tecla', 'Cividade', {'distancia': 6}),
            ('Nogueiró', 'Fraião', {'distancia': 7}),
            ('Gualtar', 'São Pedro', {'distancia': 8}),
            ('São José de São Lázaro', 'Lomar', {'distancia': 9}),
            ('Real', 'Este', {'distancia': 10}),
            ('São Lourenço', 'São Tiago', {'distancia': 11}),
            ('Merelim São Pedro', 'Merelim São Paio', {'distancia': 12}),
            ('Espinho', 'Padim da Graça', {'distancia': 13}),
            ('São Vítor', 'São Vicente', {'distancia': 2}),
            ('São João do Souto', 'São Vicente', {'distancia': 3}),
            ('Maximinos', 'São Vítor', {'distancia': 4}),
            ('Maximinos', 'São João do Souto', {'distancia': 5}),
            ('Cividade', 'Santa Tecla', {'distancia': 6}),
            ('Fraião', 'Nogueiró', {'distancia': 7}),
            ('São Pedro', 'Gualtar', {'distancia': 8}),
            ('Lomar', 'São José de São Lázaro', {'distancia': 9}),
            ('Este', 'Real', {'distancia': 10}),
            ('São Tiago', 'São Lourenço', {'distancia': 11}),
            ('Merelim São Paio', 'Merelim São Pedro', {'distancia': 12}),
            ('Padim da Graça', 'Espinho', {'distancia': 13})
    ]

    G.add_edges_from(arestas)
    return G