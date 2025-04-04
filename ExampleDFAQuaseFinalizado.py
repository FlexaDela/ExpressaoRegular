#sigma = {a, b} # mesma coisa que palavra é composta por letras a e b


import graphviz

# Magnifica Geringosa para Montagem de Automatos Finitos Deterministicos (MGMAFD)
# Integrantes: 
# Lua Euriqui
# Mateus Flexa
# Vitor Augusto

class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q # conjunto de estados
        self.Sigma = Sigma # conjunto de simbolos
        self.delta = delta  # função de transição como um dicionário
        self.q0 = q0 # estado inicial
        self.F = F # conjunto de estados finais

    def __repr__(self):
        return f"DFA({self.Q}, \n\t{self.Sigma}, \n\t{self.delta}, \n\t{self.q0}, \n\t{self.F})"
    
  
    def run(self, palavra): # w é uma palavra inserida no metodo
        palavraSalva = palavra
        estadoAtual = self.q0 # estadoAtual representa o estado atual, no caso comeca pelo estado inicial
        
        estadosApresentados = [] # 0, 0, 1, 0, 2 etc
        caminhosApresentados = [] # a, b, a, a, b etc
        
        while palavra!="" : # enquanto palavra for diferente de nada, entao operacao abaixo ocorre
            
            estadosApresentados.append(estadoAtual)
            caminhosApresentados.append(palavra[0])
            estadoAtual = self.delta[(estadoAtual, palavra[0])]                                                                             # estadoAtual recebe novo estado presente em delta, em que estadoAtual é o estado atual e w[0] é a letra inicial 
            
            
    
            palavra = palavra[1:] # palavra consome outras letras/simbolo do seu alfabeto
            if palavra =="":
                estadosApresentados.append(estadoAtual)
        
        print("Estados percorridos: ", estadosApresentados)
        print("Simbolos: ", caminhosApresentados)

        return print(f"{palavraSalva} = ", (estadoAtual in self.F))                                                                                 # retorna boleano que indica se estadoAtual(estado atual) cehgou em algum estado final 
    
    #MATEUS - FAZER ITERACAO OU REMOVER ESSA PARTE
        """
        printarEstado = estadosApresentados[0]
        printarCaminho = caminhosApresentados[0]
        
        for estado in estadosApresentados:
            if printarCaminho[:0]:
                print(f"{printarEstado} - finalizado")
            else:
                print(f"{printarEstado} - {printarCaminho}")
            printarCaminho = caminhosApresentados[+1]
            printarEstado = estadosApresentados[+1]
        """
        ########

    #fazer grafo?
    def apresentarGrafo(self):
            # 1. CRIAR GRAFO
            grafoAFD = graphviz.Digraph(comment='Meu Grafo')
            grafoAFD.attr(rankdir="LR", center="true", size = "10" )

            # 2. CRIAR NÓS (estados)
            estadosTotais = self.Q
            print("estados totais: ", estadosTotais)
            for estados in estadosTotais:
                print("estados: ", estados)
                grafoAFD.node(str(estados)) #-> precisar ser string                
                
            # 3. CRIAR ARESTAS (caminhos dos simbolos)
            transicoes = self.delta
            for (origem, simbolo), destino in transicoes.items(): #EXEMPLO: (0 -> origem, "a"->simbolo/nome do caminho): 0 ->destino
                print(origem, simbolo, destino)
                grafoAFD.edge(str(origem), str(destino), label=simbolo)

            # 4. INDICAR q0 (estado inicial)
            estadoInicial = self.q0
            grafoAFD.node("vazio", fontcolor="none", shape="none") # poe um no e retira forma e cor da fonte
            grafoAFD.edge("vazio", str(estadoInicial), arrowhead="empty", arrowsize="3") # faz o no fantasma apontar pra pro q0

            # 5. INDICAR qF`s FINALIZAR 
            estadosFinais = self.F
            for estados in estadosFinais:
                grafoAFD.node(str(estados), shape="doublecircle")
        
            grafoAFD.render('meu_grafo', format='png', cleanup=True)
            grafoAFD.view()

#Configuração de linguagem
D0 = DFA({0,1,2}, # ESTADOS 
         {"a", "b"}, # Sigma - alfabeto/simbolos 
         {(0, "b"):0, (0, "a"):1, # delta - transicao de estados (estadoInicial, "simbolo/caminho"): novoEstado
          (1, "a"):1, (1, "b"):2,
          (2, "a"):1, (2, "b"):0},
          0, # estado inicial
          {1,2}) # conjunto de estados finais

#True
#MATEUS - FAZER INPUT
D0.run("ababba") # inserir palavra

D0.mostraOGrafoAi()

"""
True:
aa
ab
abbba
bbaa
baba
ababba

False:
aaaaabb
abbb
ababb
"""

# referencia: 
#   Automata & Python (Long Version) - Computerphile
#       https://www.youtube.com/watch?v=oHVHkkah3MY&list=PL8d3io7QbejCKbx9Kyp8tPL1x1HbxB1km&index=7
#       
#   Graphviz 
#       https://graphviz.readthedocs.io/en/stable/manual.html#
#       https://graphviz.org/about/
#
#


