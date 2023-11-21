import networkx as nx
import matplotlib.pyplot as plt
from Tubo import Tubo

class Condensador:
    dashed_graph = nx.Graph()
    lined_graph = nx.Graph()
    circuitos = []
    tubos = {}
    def __init__(self, Tipo, Ntub, Nfilas, Nsegmentos, tubos_en_baja, segmentos_en_baja, alta_velocidad, baja_velocidad) -> None:
        #Tipo de sistema (S o I) 
        self.Tipo = Tipo

        #Número de tubos por fila
        self.Ntub = Ntub

        #Números de filas
        self.Nfilas = Nfilas

        #Números de segmentos
        self.Nsegmentos = Nsegmentos

        #Tubos en zona de baja velocidad
        self.tubos_en_baja = tubos_en_baja
        
        #segmentos en zono de baja velocidad
        self.segmentos_en_baja = segmentos_en_baja

        self.alta_velocidad = alta_velocidad
        
        self.baja_velocidad = baja_velocidad
        
        if Tipo == "I":
            self.diseñarEnLinea()
            # self.diseñarCircuito()
        elif Tipo == "S":
            self.diseñarEscalonado()
            # self.diseñarCircuito()
        else:
            print("Ingrese un tipo válido")
        

    def diseñarEnLinea(self):
        G = nx.Graph()
        filas = self.Nfilas
        segmentos = self.Nsegmentos
        count = 1
        Ntub = self.Ntub
        for fila in range (1, filas+1):
            for tubo in range(1, Ntub+1):
                G.add_node(count, pos=(fila, tubo))
                condicion1 = tubo < self.tubos_en_baja[0]
                condicion2 = tubo > Ntub - self.tubos_en_baja[1]
                if tubo <= self.tubos_en_baja[0] or tubo > Ntub - self.tubos_en_baja[1]:
                    # self.tubos[count] = Tubo(segmentos, self.baja_velocidad, self.alta_velocidad, segmentos)
                    self.tubos[count] = "baja_velocidad"
                else:
                    # self.tubos[count] = "alta_velocidad"
                    self.tubos[count] = Tubo(segmentos, self.baja_velocidad, self.alta_velocidad, self.segmentos_en_baja)
                count+=1
        self.graph = G
        self.showSimpleGraph()
    
    def diseñarEscalonado(self):
        G = nx.Graph()
        Ntub_non, Ntub_par = self.Ntub
        if Ntub_non == Ntub_par:
            posTub = int(
                input("""El programa considera que la entrada del aire está 
                a la izquierda, la primera fila de tubos que recibe
                el aire está desfasada hacia arriba o hacia abajo?\n 
                Arriba [1]\n
                Abajo [2]"""
                )
            )
        else:
            posTub = 1 if Ntub_non > Ntub_par else 2
        
        self.posTub = posTub
        
        filas = self.Nfilas

        segmentos = self.Nsegmentos
        
        count =  1
        for fila in range(1, filas+1):
            par = fila%2 == 0
            Ntub = Ntub_par if par else Ntub_non
            
            if not par:
                begin = posTub
                tubos_en_baja = self.tubos_en_baja[1]
            else:
                begin = 1 if posTub == 2 else 2
                tubos_en_baja = self.tubos_en_baja[0]
            
            end = (Ntub)*2 + begin
            count_velocidad = 1
            for tubo in range(begin, end, 2):
                G.add_node(count, pos=(fila, tubo))
                if count_velocidad <= tubos_en_baja[0] or count_velocidad > Ntub - tubos_en_baja[1]:
                    # self.tubos[count] = Tubo(segmentos, self.baja_velocidad, self.alta_velocidad, segmentos)
                    self.tubos[count] = "baja_velocidad"
                else:
                    # self.tubos[count] = "alta_velocidad"
                    self.tubos[count] = Tubo(segmentos, self.baja_velocidad, self.alta_velocidad, self.segmentos_en_baja)
                count_velocidad+=1
                count+=1
            
        self.graph = G
        self.showSimpleGraph()
    
    def showSimpleGraph(self):
        G = self.graph
        pos=nx.get_node_attributes( G, "pos" )
        nx.draw( G, pos, with_labels=True )
        plt.xlim( 0, 100 )
        plt.ylim( 100, 0 )
        plt.axis( "equal" )
        plt.show()
    
    def diseñarCircuito(self):
        A = self.lined_graph
        B = self.dashed_graph
        G = self.graph
        tipo = ""
        dashed = 1
        while tipo != "exit":
            tipo = input("Ingrese el tipo de unión: \n continua (c) o directa (d)")
            try:
                p1 = int(input("Ingrese el primer punto de la unión: "))
                p2 = int(input("Ingrese el segundo punto de la unión: "))
            except:
                print("Ingrese números válidos")
                continue
            
            diff = 1 if p1 - p2 < 0 else -1
            if tipo == "continua" or tipo == "c":
                for n in range(p1, p2, diff):
                    if dashed:
                        B.add_node(n, pos=G.nodes[n]['pos'])
                        B.add_node(n+diff, pos=G.nodes[n+diff]['pos'])
                        B.add_edge(n, n+diff)
                        dashed = 0
                    else: 
                        A.add_node(n, pos=G.nodes[n]['pos'])
                        A.add_node(n+diff, pos=G.nodes[n+diff]['pos'])
                        A.add_edge(n, n+diff)
                        dashed = 1
            elif tipo == "directa" or tipo == "d":
                if dashed:
                    B.add_node(p1, pos=G.nodes[p1]['pos'])
                    B.add_node(p2, pos=G.nodes[p2]['pos'])
                    B.add_edge(p1, p2)
                    dashed = 0
                else:
                    A.add_node(p1, pos=G.nodes[p1]['pos'])
                    A.add_node(p2, pos=G.nodes[p2]['pos'])
                    A.add_edge(p1, p2)
                    dashed = 1
            else:
                print("Ingrese un tipo válido de unión (directa (d) o continua (c))")
                continue
        
        self.showCircuits()
    
    def showCircuits(self):
        A = self.lined_graph
        B = self.dashed_graph
        G = self.graph

        pos=nx.get_node_attributes(G, "pos")

        nx.draw(B,pos, style=["--"], with_labels=True)
        nx.draw(A,pos, style=["-"], with_labels=True)
        nx.draw(G,pos, style=["-"], with_labels=True)

        plt.xlim( 0, 100 )
        plt.ylim( 100, 0 )
        plt.axis( "equal" )
        plt.show()


