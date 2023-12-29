import threading
import algoritmos_procura as ap
import cria_grafos as cg
import health_planet as hp
import estafeta as es
import encomenda as en
import povoar as p
import threading
import time
import networkx as nx
def atualiza_encomendas(encomenda,meio_de_transporte,grafo,meteorologia,altura_do_dia):

    caminho_antigo=encomenda.caminho
    primeira_ocorrencia = caminho_antigo.index(encomenda.ultimo_local_passou)
    if(encomenda.destino!="Armazem"):
        caminho_antigo = caminho_antigo[:primeira_ocorrencia]
        path1,_ = ap.dijkstra(grafo,encomenda.ultimo_local_passou,encomenda.destino)
        path2,_=ap.dijkstra(grafo,encomenda.destino,"Armazem")
        path=caminho_antigo+path1
        path=trajeto_completo_estafeta(path,path2)
    else:
        segunda_ocorrencia = caminho_antigo.index(encomenda.ultimo_local_passou, primeira_ocorrencia + 1)
        caminho_antigo = caminho_antigo[:segunda_ocorrencia + 1]
        path1,_=ap.dijkstra(grafo,encomenda.ultimo_local_passou,"Armazem")
        path=caminho_antigo+path1

    if meio_de_transporte==1:
        tempo, vel_medias=altera_velocidade(meteorologia,altura_do_dia,path, 10-(0.6*encomenda.peso), grafo)
    elif meio_de_transporte==2:
        tempo, vel_medias=altera_velocidade(meteorologia,altura_do_dia,path, 35-(0.5*encomenda.peso), grafo)
    else:
        tempo, vel_medias=altera_velocidade(meteorologia,altura_do_dia,path, 50-(0.1*encomenda.peso), grafo)
    return tempo, vel_medias, path

def trajeto_completo_estafeta(lista1,lista2):
    lista_concatenada = lista1 + lista2[1:]
    return lista_concatenada

def altera_velocidade(meteorologia,altura_do_dia,path, vel, grafo):
    tempo = 0
    vel_medias = []

    if meteorologia == 1:
        pass
    elif meteorologia == 2:
        vel -= vel * 0.04
    elif meteorologia == 3:
        vel -= vel * 0.08
    elif meteorologia == 4:
        vel -= vel * 0.12
    elif meteorologia == 5:
        vel -= vel * 0.16

    if altura_do_dia == 1:
        pass
    elif altura_do_dia == 2:
        vel -= vel * 0.04

    posicao = 0
    while posicao + 1 < len(path):
        vel_aresta = vel
        distancia = grafo[path[posicao]][path[posicao + 1]]['weight']

        if grafo[path[posicao]][path[posicao + 1]]['estrada'] == "terra":
            vel_aresta -= vel_aresta * 0.1
        elif grafo[path[posicao]][path[posicao + 1]]['estrada'] == "paralelo":
            vel_aresta -= vel_aresta * 0.05

        vel_aresta -= vel_aresta * (grafo[path[posicao]][path[posicao + 1]]['transito'])

        tempo += int(((distancia / vel_aresta) * 60) + 0.5)
        vel_medias.append(vel_aresta)
        posicao += 1
        
    return tempo/2, vel_medias

def verifica_disponibilidade (transporte, tempo_transporte, velocidades_medias, tempo_pretendido,health_planet,caminho,queremosEletrico,id_encomenda,distancia):
    tempo_disponivel_eletrico, estafeta_disponivel_eletrico, tempo_disponivel_sem_ser_eletrico, estafeta_disponivel_eletrico_sem_ser_eletrico = health_planet.disponibilidade(transporte)

    tempo_necessario_eletrico = (tempo_disponivel_eletrico + tempo_transporte)
    tempo_necessario_sem_ser_eletrico = (tempo_disponivel_sem_ser_eletrico + tempo_transporte) 


    if(queremosEletrico==True):
        if (tempo_pretendido >= tempo_necessario_eletrico):
            health_planet.atualiza_inicial(estafeta_disponivel_eletrico,2*tempo_transporte,velocidades_medias,caminho,id_encomenda,transporte,True,distancia) 
            return tempo_necessario_eletrico
        elif(tempo_pretendido >= tempo_necessario_sem_ser_eletrico):
            health_planet.atualiza_inicial(estafeta_disponivel_eletrico_sem_ser_eletrico,2*tempo_transporte,velocidades_medias,caminho,id_encomenda,transporte,False,distancia) 
            return tempo_necessario_sem_ser_eletrico
        return -1
    else:
        if(tempo_pretendido >= tempo_necessario_sem_ser_eletrico):
            health_planet.atualiza_inicial(estafeta_disponivel_eletrico_sem_ser_eletrico,2*tempo_transporte,velocidades_medias,caminho,id_encomenda,transporte,False,distancia) 
            return tempo_necessario_sem_ser_eletrico
        elif(tempo_pretendido >= tempo_necessario_eletrico,distancia):
            health_planet.atualiza_inicial(estafeta_disponivel_eletrico,2*tempo_transporte,velocidades_medias,caminho,id_encomenda,transporte,True) 
            return tempo_necessario_eletrico
        return -1

def calculos(dist,meteorologia,altura_do_dia,tempo_pedido, peso, path,health_planet,grafo,id_encomenda):

    tempo, velocidades_medias = altera_velocidade(meteorologia,altura_do_dia,path,10-(0.6*peso), grafo)
    if (peso<=5 and tempo<tempo_pedido and (tempo_necessario := verifica_disponibilidade (1, tempo, velocidades_medias, tempo_pedido,health_planet,path,False,id_encomenda,dist))!= -1):
        print(f"Demora {tempo} minutos a realizar a sua entrega de bicicleta pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo_necessario} minutos")

    else:
        tempo, velocidades_medias = altera_velocidade(meteorologia,altura_do_dia,path,35-(0.5*peso), grafo)
        if(peso<=20 and tempo<tempo_pedido  and (tempo_necessario := verifica_disponibilidade (2, tempo, velocidades_medias, tempo_pedido,health_planet,path,True,id_encomenda,dist))!= -1):
            print(f"Demora {tempo} minutos a realizar a sua entrega de moto pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo_necessario} minutos")
        else:
            tempo, velocidades_medias = altera_velocidade(meteorologia,altura_do_dia,path,50-(0.1*peso), grafo)
            if (tempo<tempo_pedido and (tempo_necessario := verifica_disponibilidade (3, tempo, velocidades_medias, tempo_pedido,health_planet,path,True,id_encomenda,dist))!= -1):
                print(f"Demora {tempo} minutos a realizar a sua entrega de carro pelo seguinte percurso: {path}, mas só é possível entregar daqui a {tempo_necessario} minutos")
            else:
                print("Nao é possivel entregar a encomenda no tempo pretendido")

def avanca_tempo_virtual(health_planet, grafo, encerrar_thread,lock,grafo_cortadas):
    while not encerrar_thread.is_set():
        time.sleep(1) 
        with lock:
            health_planet.atualiza_estado(grafo,grafo_cortadas) 

    
def main():
    health_planet = hp.Health_Planet()
    p.povoa_estafetas(health_planet)
    grafo = cg.cria_grafo()
    grafo_cortadas = nx.Graph()

    lock = threading.Lock()

    encerrar_thread = threading.Event()  # Criando um evento para encerrar a thread
    thread = threading.Thread(target=avanca_tempo_virtual, args=(health_planet, grafo, encerrar_thread,lock,grafo_cortadas))
    thread.start()

    meteorologia=1
    altura_do_dia=1

    i=-2
    while(i!=0):
            print("\n------MENU-----")
            print("0-Sair")
            print("1-Adicionar estafeta")
            print("2-Visualizar estafetas")
            print("3-Remover estafeta")
            print("4-Atrasar estafeta")
            print("5-Alterar Meteorologia")
            print("6-Alterar altura do dia")
            print("7-Visualizar encomendas")
            print("8-Visualizar fila de encomendas estafeta")
            print("9-Cortar estrada")
            print("10-Repor estrada")
            print("11-Realizar encomenda")
        

        #try:
            i=int(input("Introduza uma das opções: "))
            if (i!=0):
                if (i==1):
                    nome = input("Introduza o nome do estafeta: ")
                    meio_de_transporte = int(input("Indique o número do tipo de veículo \n1-Bicicleta\n2-Moto\n3-Carro:\n"))
                    eletrico = int(input("O veiculo é eletrico (1-Sim, 2-Nao)"))
                    if (meio_de_transporte>0 and meio_de_transporte<4):
                        if(eletrico==1 or eletrico==2):
                            if eletrico==1:
                                estafeta = es.Estafeta(nome, meio_de_transporte,True)
                                health_planet.add_estafeta(estafeta.id, estafeta)
                            else:
                                estafeta = es.Estafeta(nome, meio_de_transporte,False)
                                health_planet.add_estafeta(estafeta.id, estafeta)
                            print(f"O estafeta {nome} foi adicionado com sucesso")
                        else:
                            print("Valor inválido")
                    else:
                        print("Valor inválido")
                        
                elif(i==2):
                    with lock:
                        health_planet.ver_estafetas()

                elif(i==3):
                    id=int(input("Introduza o id do estafeta: "))
                    try:
                        health_planet.remove_estafeta(id)
                        print("Estafeta removido com sucesso")
                    except:
                        print("Não foi possível remover o estafeta")

                elif(i==4):
                    try:
                        id = int(input("Indique o id do estafeta que se encontra atrasado: "))
                        if not health_planet.existe_estafeta(id):
                            print("O estafeta não existe")
                        else:
                            atraso = int(input("Indique o tempo de atraso do estafeta: "))
                            health_planet.dict_estafetas.get(id).aumenta_pausa(atraso)
                    except:
                        print("Não foi possível registar o atraso do estafeta")

                elif(i==5):
                    try:
                        met = int(input("Condicoes meteorológicas (1-sol, 2-vento, 3-chuva, 4-nevoeiro, 5-tempestade): "))
                        if(met>0 and met<6):
                            meteorologia=met
                        else:
                            print("Valor nao é válido")
                    except:
                        print("Introduza um valor inteiro")
                elif(i==6):
                    try:
                        altura_dia = int(input("Altura do dia: (1-Dia, 2-Noite): "))
                        if (altura_dia==1 or altura_dia==2):
                            altura_do_dia=altura_dia
                        else:
                            print("Valor invalido")
                    except:
                        print("Introduza um valor inteiro")
                
                elif(i==7):
                    with lock:
                        health_planet.ver_encomendas()

                elif(i==8):
                    try:
                        id = int(input("Indique o id do estafeta de que pretende ver a fila de encomendas em espera: "))
                        if not health_planet.existe_estafeta(id):
                            print("O estafeta não existe")
                        else:
                            health_planet.ver_fila_estafeta(id)
                    except:
                        print("Não foi possível apresentar o solicitado")

                elif(i==9):
                    try:
                        cg.str_arestas_grafo(grafo)
                        id = int(input("Introduza a estrada que vai ser cortada:"))
                        cg.mover_aresta_entre_grafos(id,grafo,grafo_cortadas)
                        encerrar_thread.set()
                        
                        #O que temos de atualizar no estafeta
                        for estafeta in health_planet.dict_estafetas.values():
                            #..........................Atualizar encomenda atual.........................................
                            if(estafeta.encomenda_atual!=None):
                                tempo,vel_medias,path=atualiza_encomendas(estafeta.encomenda_atual,estafeta.meio_de_transporte,grafo,meteorologia,altura_do_dia)

                                estafeta.encomenda_atual.velocidades_medias=vel_medias
                                estafeta.encomenda_atual.tempo_transporte=tempo
                                estafeta.encomenda_atual.caminho=path

                                #............................Atualizar encomendas em fila.................................
                                if(not estafeta.fila_encomendas.empty):
                                    tamanho_da_fila = estafeta.fila_encomendas.qsize()

                                    for i in range(tamanho_da_fila):
                                        elemento = estafeta.fila_encomendas.get()
                                        tempo,vel_medias,path=atualiza_encomendas(elemento,estafeta.meio_de_transporte,grafo,meteorologia,altura_do_dia)

                                        elemento.velocidades_medias=vel_medias
                                        elemento.tempo_transporte=tempo
                                        elemento.caminho=path
                                        
                                        estafeta.fila_encomendas.put()

                        #Para voltar a correr a thread
                        encerrar_thread.clear()
                    except:
                        print("Introduziu um valor invalido")
                elif(i==10):
                    try:
                        cg.str_arestas_grafo(grafo_cortadas)
                        id = int(input("Introduza a estrada que vai ser reposta:"))
                        cg.mover_aresta_entre_grafos(id,grafo_cortadas,grafo)
                        encerrar_thread.set()
                        
                        #O que temos de atualizar no estafeta
                        for estafeta in health_planet.dict_estafetas.values():
                            #..........................Atualizar encomenda atual.........................................
                            if(estafeta.encomenda_atual!=None):
                                tempo,vel_medias,path=atualiza_encomendas(estafeta.encomenda_atual,estafeta.meio_de_transporte,grafo,meteorologia,altura_do_dia)

                                estafeta.encomenda_atual.velocidades_medias=vel_medias
                                estafeta.encomenda_atual.tempo_transporte=tempo
                                estafeta.encomenda_atual.caminho=path

                                #............................Atualizar encomendas em fila.................................
                                if(not estafeta.fila_encomendas.empty):
                                    tamanho_da_fila = estafeta.fila_encomendas.qsize()

                                    for i in range(tamanho_da_fila):
                                        elemento = estafeta.fila_encomendas.get()
                                        tempo,vel_medias,path=atualiza_encomendas(elemento,estafeta.meio_de_transporte,grafo,meteorologia,altura_do_dia)

                                        elemento.velocidades_medias=vel_medias
                                        elemento.tempo_transporte=tempo
                                        elemento.caminho=path
                                        
                                        estafeta.fila_encomendas.put()

                        #Para voltar a correr a thread
                        encerrar_thread.clear()
                    except:
                        print("Introduziu um valor invalido")

























                elif(i==11):
                    print("\n------ALGORITMO-----")
                    print("1-Dijkstra")
                    print("2-Interativo")
                    print("3-Procura em profundidade(DFS)")
                    print("4-Procura Bidirecional")
                    print("5-Procura em largura(BFS)")
                    print("6-Procura Gulosa")
                    print("7-Procura A*")

                    #try:
                    opcao=int(input("Introduza uma das opcoes:"))
                    volume=int(input("\nIntroduza o volume da encomenda:"))
                    peso=float(input("\nIntroduza o peso da encomenda em Kg:"))
                    tempo=int(input("\nQual o tempo máximo em minutos:"))
                    terra=input("\nPara onde deseja encomendar:")

                        #try:
                    encomenda=en.Encomenda(peso,volume, tempo)
                    health_planet.add_encomenda(encomenda.id,encomenda)
                    if (peso>0 and peso<=100):
                        #.....................Varios algoritmos.................
                        if (opcao==1):
                            try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos (dist,meteorologia,altura_do_dia, tempo, peso, path,health_planet,grafo,encomenda.id)
                            except:
                                print("O destino selecionado não existe")

                        elif (opcao==2):
                            try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos(dist,meteorologia,altura_do_dia,tempo,peso,path,health_planet,grafo,encomenda.id)
                            except:
                                print("O destino selecionado não existe")

                        elif (opcao==3):
                            try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos (dist,meteorologia,altura_do_dia, tempo, peso, path,health_planet,grafo,encomenda.id)
                            except:
                                print("O destino selecionado não existe")

                        elif (opcao==4):
                            try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos (dist,meteorologia,altura_do_dia, tempo, peso, path,health_planet,grafo,encomenda.id)
                            except :
                                print("O destino selecionado não existe")

                        elif (opcao==5):
                            try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos (dist,meteorologia,altura_do_dia, tempo, peso, path,health_planet,grafo,encomenda.id)
                            except :
                                print("O destino selecionado não existe")

                        elif (opcao==6):
                            try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos (dist,meteorologia,altura_do_dia, tempo, peso, path,health_planet,grafo,encomenda.id)
                            except :
                                print("O destino selecionado não existe")

                        elif (opcao==7):
                            #try:
                                path1,dist = ap.dijkstra(grafo,"Armazem",terra)
                                path2,_=ap.dijkstra(grafo,terra,"Armazem")
                                path=trajeto_completo_estafeta(path1,path2)
                                calculos (dist,meteorologia,altura_do_dia, tempo, peso, path,health_planet,grafo,encomenda.id)
                            #except :
                            #    print("O destino selecionado não existe")

                        else:
                            print("O algoritmo escolhido não é válido")
                        #........................................................                                
                    else:
                            print("Peso impossivel")
                        #except :
                        #        print("Não foi possível registar a encomenda")
                    #except :
                    #    print("Os valores introduzidos sao inválidos")
                else:
                    print ("Introduza um valor válido")
            else:
                    encerrar_thread.set()
        #except ValueError:
        #    print("Introduza um valor válido")
        #    i=-2

if __name__ == "__main__":
    main()
