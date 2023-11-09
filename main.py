import algoritmos_procura as ap
import cria_grafos as cg
import health_planet as hp
import estafeta as es
import encomenda as en


def calculos(dist,tempo, peso, path):
    tempo_bicicleta=int(((dist/(10-(0.6*peso)))*60)+0.5) #0.5 para arredondar primeiro
    tempo_moto=int(((dist/(35-(0.5*peso)))*60)+0.5)
    tempo_carro=int(((dist/(50-(0.1*peso)))*60)+0.5)

    if (peso<=5 and tempo_bicicleta<tempo):
        print(f"Demora {tempo_bicicleta} minutos a sua entrega pelo seguinte percurso: {path}")
    elif(peso<=20 and tempo_moto<tempo):
        print(f"Demora {tempo_moto} minutos a sua entrega pelo seguinte percurso: {path}")
    elif(tempo_carro<tempo):
        print(f"Demora {tempo_carro} minutos a sua entrega pelo seguinte percurso: {path}")
    else:
        print("Nao é possivel entregar a encomenda no tempo pretendido")


def main():
    health_planet = hp.Health_Planet()
    grafo = cg.cria_grafo()

    i=-2
    while(i!=0):
        print("------MENU-----")
        print("0-Sair")
        print("1-Adicionar estafeta")
        print("2-Visualizar estafetas")
        print("3-Remover estafeta")
        print("4-Realizar encomenda")

        try:
            i=int(input("Introduza uma das opções: "))
            if (i!=0):
                if i == 1:
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
                    print("------ALGORITMO-----")
                    print("1-Dijkstra")
                    try:
                        j=int(input("Introduza uma das opcoes:"))
                        volume=int(input("Introduza o volume da encomenda:"))
                        peso=float(input("Introduza o peso da encomenda em Kg:"))
                        tempo=int(input("Qual o tempo maximo em minutos:"))
                        terra=input("Para onde deseja encomandar:")

                        try:
                            encomenda=en.Encomenda(peso,volume, tempo)
                            health_planet.add_encomenda(encomenda.id,encomenda)

                            if (peso>0 and peso<=100):
                                #.....................Varios algoritmos.................
                                if (j==1):
                                    try:
                                        dist, path = ap.dijkstra(grafo,"Armazem",terra)
                                        calculos (dist, tempo, peso, path)
                                    except:
                                        print("A terra não existe")
                                else:
                                    print("O algoritmo escolhido não é válido")

                                #........................................................

                                
                            else:
                                    print("Peso impossivel")
                        except:
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
