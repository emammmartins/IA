import algoritmos_procura as ap
import cria_grafos as cg
import health_planet as hp
import estafeta as es
import encomenda as en

#Esta função deverá verificar se existem estafetas desse meio de transporte (1, 2 ou 3) no sistema,
#escolher o que demora menos tempo a estar disponível e retornar esse tempo e o id do estafeta
def disponibilidade(transporte):
    return 2, id
    #return sys.maxint quando não for possível

def verifica_disponibilidade (transporte, tempo_transporte, tempo_pretendido):
    tempo_disponivel, estafeta_disponivel = disponibilidade(transporte)
    tempo_necessario = (tempo_disponivel + tempo_transporte)
    if (tempo_pretendido >= tempo_necessario):
        #criar função que aumenta tempo_transporte (+margem) para o estafeta
        return tempo_necessario
    return -1

def calculos(dist,tempo, peso, path):
    tempo_bicicleta=int(((dist/(10-(0.6*peso)))*60)+0.5) #0.5 para arredondar primeiro
    tempo_moto=int(((dist/(35-(0.5*peso)))*60)+0.5)
    tempo_carro=int(((dist/(50-(0.1*peso)))*60)+0.5)

    if (peso<=5 and tempo_bicicleta<tempo and (tempo := verifica_disponibilidade (1, tempo_bicicleta, tempo))!= -1):
        print(f"Demora {tempo_bicicleta} minutos a realizar a sua entrega de bicicleta pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo} minutos")
    elif(peso<=20 and tempo_moto<tempo  and (tempo := verifica_disponibilidade (2, tempo_moto, tempo))!= -1):
        print(f"Demora {tempo_moto} minutos a realizar a sua entrega de moto pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo} minutos")
    elif(tempo_carro<tempo and (tempo := verifica_disponibilidade (3, tempo_carro, tempo))!= -1):
        print(f"Demora {tempo_carro} minutos a realizar a sua entrega de carro pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo} minutos")
    else:
        print("Nao é possivel entregar a encomenda no tempo pretendido")


def main():
    health_planet = hp.Health_Planet()
    grafo = cg.cria_grafo()

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
                                        calculos (dist, tempo, peso, path)
                                    except:
                                        print("O destino selecionado não existe")

                                elif (opcao==2):
                                    try:
                                        path,dist = ap.iterative_deepening_dfs(grafo,"Armazem",terra)
                                        calculos(dist,tempo,peso,path)
                                    except ValueError as e:
                                        print(f"Erro: {e}")
                                        print("O destino selecionado não existe")

                                elif (opcao==3):
                                    try:
                                        path, dist = ap.procura_em_profundidade(grafo, "Armazem", terra)
                                        calculos (dist, tempo, peso, path)
                                    except:
                                        print("O destino selecionado não existe")

                                elif (opcao==4):
                                    try:
                                        path, dist = ap.bidirectional_search(grafo, "Armazem", terra)
                                        calculos(dist, tempo, peso, path)
                                    except :
                                        print("O destino selecionado não existe")

                                elif (opcao==5):
                                    try:
                                        path, dist = ap.bfs(grafo, "Armazem", terra)
                                        calculos(dist, tempo, peso, path)
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

        except ValueError:
            print("Introduza um valor válido")
            i=-2
    

if __name__ == "__main__":
    main()
