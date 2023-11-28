import algoritmos_procura as ap
import cria_grafos as cg
import health_planet as hp
import estafeta as es
import encomenda as en
import povoar as p
import threading
import time


def verifica_disponibilidade (transporte, tempo_transporte, tempo_pretendido,health_planet,velocidade,caminho):
    tempo_disponivel, estafeta_disponivel = health_planet.disponibilidade(transporte)
    tempo_necessario = (tempo_disponivel + tempo_transporte)
    if (tempo_pretendido >= tempo_necessario):
        health_planet.atualiza_estafeta_inicio(estafeta_disponivel,2*tempo_transporte,velocidade,caminho) #:::::::::::::::::::::MARGEM:::::::::::::
        return tempo_necessario
    return -1

def calculos(dist,tempo, peso, path,health_planet):
    tempo_bicicleta=int(((dist/(10-(0.6*peso)))*60)+0.5) #0.5 para arredondar primeiro
    tempo_moto=int(((dist/(35-(0.5*peso)))*60)+0.5)
    tempo_carro=int(((dist/(50-(0.1*peso)))*60)+0.5)
    if (peso<=5 and tempo_bicicleta<tempo and (tempo := verifica_disponibilidade (1, tempo_bicicleta, tempo,health_planet,10-(0.6*peso),path)!= -1)):
        print(f"Demora {tempo_bicicleta} minutos a realizar a sua entrega de bicicleta pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo} minutos")
    elif(peso<=20 and tempo_moto<tempo  and (tempo := verifica_disponibilidade (2, tempo_moto, tempo,health_planet,35-(0.5*peso),path))!= -1):
        print(f"Demora {tempo_moto} minutos a realizar a sua entrega de moto pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo} minutos")
    elif(tempo_carro<tempo and (tempo := verifica_disponibilidade (3, tempo_carro, tempo,health_planet,dist/50-(0.1*peso),path)!= -1)):
        print(f"Demora {tempo_carro} minutos a realizar a sua entrega de carro pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo} minutos")
    else:
        print("Nao é possivel entregar a encomenda no tempo pretendido")

def avanca_tempo_virtual(health_planet, grafo, encerrar_thread):
    while not encerrar_thread.is_set():
        time.sleep(2)
        health_planet.atualiza_estado(grafo)
    
def main():
    health_planet = hp.Health_Planet()
    p.povoa_estafetas(health_planet)
    grafo = cg.cria_grafo()

    encerrar_thread = threading.Event()  # Criando um evento para encerrar a thread
    thread = threading.Thread(target=avanca_tempo_virtual, args=(health_planet, grafo, encerrar_thread))
    thread.start()

    i=-2
    while(i!=0):
        print("\n------MENU-----")
        print("0-Sair")
        print("1-Adicionar estafeta")
        print("2-Visualizar estafetas")
        print("3-Remover estafeta")
        print("4-Realizar encomenda")

        try:
            i=int(input("Introduza uma das opções: "))
            if (i!=0):
                if (i==1):
                    nome = input("Introduza o nome do estafeta: ")
                    meio_de_transporte = int(input("Indique o número do tipo de veículo \n1-Bicicleta\n2-Moto\n3-Carro:\n"))
                    if (meio_de_transporte>0 and meio_de_transporte<4):
                        estafeta = es.Estafeta(nome, meio_de_transporte)
                        health_planet.add_estafeta(estafeta.id, estafeta)
                        print(f"O estafeta {nome} foi adicionado com sucesso")
                    else:
                        print("Valor inválido")
                        
                elif(i==2):
                    health_planet.ver_estafetas()

                elif(i==3):
                    id=int(input("Introduza o id do estafeta: "))
                    try:
                        health_planet.remove_estafeta(id)
                        print("Estafeta removido com sucesso")
                    except:
                        print("Não foi possível remover o estafeta")

                elif(i==4):
                    print("\n------ALGORITMO-----")
                    print("1-Dijkstra")
                    print("2-Interativo")
                    print("3-Procura em profundidade(DFS)")
                    print("4-Procura Bidirecional")
                    print("5-Procura em largura(BFS)")
                    print("6-Procura Gulosa")
                    print("7-Procura A*")

                    try:
                        opcao=int(input("Introduza uma das opcoes:"))
                        volume=int(input("\nIntroduza o volume da encomenda:"))
                        peso=float(input("\nIntroduza o peso da encomenda em Kg:"))
                        tempo=int(input("\nQual o tempo máximo em minutos:"))
                        terra=input("\nPara onde deseja encomendar:")

                        try:
                            encomenda=en.Encomenda(peso,volume, tempo)
                            health_planet.add_encomenda(encomenda.id,encomenda)
                            if (peso>0 and peso<=100):
                                #.....................Varios algoritmos.................
                                if (opcao==1):
                                    try:
                                        dist, path = ap.dijkstra(grafo,"Armazem",terra)
                                        calculos (dist, tempo, peso, path,health_planet)
                                    except:
                                        print("O destino selecionado não existe")

                                elif (opcao==2):
                                    try:
                                        path,dist = ap.iterative_deepening_dfs(grafo,"Armazem",terra)
                                        calculos(dist,tempo,peso,path,health_planet)
                                    except ValueError as e:
                                        print(f"Erro: {e}")
                                        print("O destino selecionado não existe")

                                elif (opcao==3):
                                    try:
                                        path, dist = ap.procura_em_profundidade(grafo, "Armazem", terra)
                                        calculos (dist, tempo, peso, path,health_planet)
                                    except:
                                        print("O destino selecionado não existe")

                                elif (opcao==4):
                                    try:
                                        path, dist = ap.bidirectional_search(grafo, "Armazem", terra)
                                        calculos(dist, tempo, peso, path,health_planet)
                                    except :
                                        print("O destino selecionado não existe")

                                elif (opcao==5):
                                    try:
                                        path, dist = ap.bfs(grafo, "Armazem", terra)
                                        calculos(dist, tempo, peso, path,health_planet)
                                    except :
                                        print("O destino selecionado não existe")

                                elif (opcao==6):
                                    try:
                                        path, dist = ap.greedy_shortest_path(grafo, "Armazem", terra)
                                        calculos(dist, tempo, peso, path,health_planet)
                                    except :
                                        print("O destino selecionado não existe")

                                elif (opcao==7):
                                    try:
                                        path, dist = ap.algoritmoAEstrela(grafo, "Armazem", terra)
                                        calculos(dist, tempo, peso, path,health_planet)
                                    except :
                                        print("O destino selecionado não existe")

                                else:
                                    print("O algoritmo escolhido não é válido")
                                #........................................................                                
                            else:
                                    print("Peso impossivel")
                        except :
                            print("Não foi possível registar a encomenda")
                    except :
                        print("Os valores introduzidos sao inválidos")
                else:
                    print ("Introduza um valor válido")
            else:
                encerrar_thread.set()
        except ValueError:
            print("Introduza um valor válido")
            i=-2

if __name__ == "__main__":
    main()
