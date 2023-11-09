import algoritmos_procura as ap
import cria_grafos as cg

def main():
    print("Bem vindo à Health Planet")
    
    i=-2
    while(i!=0):
        print("------MENU-----")
        print("0-Sair")
        print("1-Dijkstra")
        try:
            i=int(input("Introduza uma das opcoes:"))
            if (i!=0):
                try: 
                    volume=int(input("Introduza o volume da encomenda:"))
                    try:
                        tempo=int(input("Qual o tempo maximo:"))
                        if(i>0 and i<2):
                            peso=float(input("Introduza o peso da encomenda:"))
                            if (peso>0 and peso<=100):
                                try:
                                    terra=input("Para onde deseja encomandar:")
                                    #.....................Varios algoritmos.................
                                    if (i==1):
                                        G=cg.cria_grafo()
                                        dist, path = ap.dijkstra(G,"Armazem",terra)
                                    #........................................................
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
                                        
                                
                                except:
                                    print("Erro no local")
                            else:
                                print("Peso acima do permitido")
                        else:
                            print("Introduza um dos valores permitidos!")
                    except ValueError:
                        print("Tempo incorreto")
                        i=-2
                except ValueError:
                    print("Introduza o volume corretamente")
                    i=-2
        except ValueError:
            print("Introduza um valor válido")
            i=-2
    

if __name__ == "__main__":
    main()