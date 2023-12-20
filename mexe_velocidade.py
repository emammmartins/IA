import cria_grafos as cg

def altera_velocidade(path, vel, grafo):
    tempo = 0
    vel_medias = []

    meteorologia = int(input("Condicoes meteorológicas (1-sol, 2-vento, 3-chuva, 4-nevoeiro, 5-tempestade): "))
    if meteorologia == 1:
        pass
    elif meteorologia == 2:
        vel -= vel * 0.02
    elif meteorologia == 3:
        vel -= vel * 0.04
    elif meteorologia == 4:
        vel -= vel * 0.06
    elif meteorologia == 5:
        vel -= vel * 0.08
    else:
        return

    altura_dia = int(input("Altura do dia: (1-Dia, 2-Noite): "))
    if altura_dia == 1:
        pass
    elif altura_dia == 2:
        vel -= vel * 0.04
    else:
        return

    posicao = 0
    while posicao + 1 < len(path):
        vel_aresta = vel
        distancia = grafo[path[posicao]][path[posicao + 1]]['weight']

        if grafo[path[posicao]][path[posicao + 1]]['estrada'] == "terra":
            vel_aresta -= vel_aresta * 0.03
        elif grafo[path[posicao]][path[posicao + 1]]['estrada'] == "paralelo":
            vel_aresta -= vel_aresta * 0.05

        vel_aresta -= vel_aresta * (grafo[path[posicao]][path[posicao + 1]]['transito'])

        tempo += int(((distancia / vel_aresta) * 60) + 0.5)
        vel_medias.append(vel)
        posicao += 1

    return tempo, vel_medias

def main():
    grafo = cg.cria_grafo()
    tempo, velocidades = altera_velocidade(34, ["Armazem", "Gualtar", "Este", "Espinho"], 45, grafo)
    print("Tempo estimado:", tempo, "minutos")
    print("Velocidades médias:", velocidades)

if __name__ == "__main__":
    main()
