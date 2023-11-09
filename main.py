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
                if(i>0 and i<2):
                    peso=float(input("Introduza o peso da encomenda:"))
                    if (peso>0 and peso<100):
                        try:
                            terra=input("Para onde deseja encomandar:")
                            if (i==1):
                                G=cg.cria_grafo_nao_orientado()
                                dist, path = ap.dijkstra(G, 'Armazem', terra)
                            if (peso<5):
                                tempo=dist*(10-(0.6*peso))
                            elif(peso<20):
                                tempo=dist*(35-(0.5*peso))
                            elif(peso<50):
                                tempo=dist*(50-(0.1*peso))
                            print(f"Demora {tempo} minutos a sua entrega pelo seguinte percurso: {path}")
                        except:
                            print("Erro no local")
                    else:
                        print("Peso impossivel")
                else:
                    print("Introduza um dos valores permitidos!")
        except ValueError:
            print("Introduza um valor válido")
            i=-2
    

if __name__ == "__main__":
    main()