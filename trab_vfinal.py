import sys
entrada_lista = sys.stdin.readlines()

#comando no terminal: windows: python trab1_vfinal.py / linux: cat python3 trab1_vfinal.py

e = entrada_lista[2].split("=")
n = int(e[1])

L_arestas = [] * (len(entrada_lista) - 4)
#preenchendo a L_arestas:
for j in range(len(entrada_lista) -4):
  L_arestas.append(entrada_lista[j+4])


#L_arestas de string p/ inteiros:
L_aux1 = []*(2*len(L_arestas))
for k in range(len(L_arestas)):
  aux1 = L_arestas[k].replace("\n","")
  aux2 = aux1.split(" ")
  L_aux1.append(int(aux2[0]))
  L_aux1.append(int(aux2[1]))


# L_arestas como lista de listas:
L_arestas_int = []*(len(L_arestas))
for i in range(0, len(L_aux1), 2):
  linha_a = []*1
  linha_a.append(L_aux1[i])
  linha_a.append(L_aux1[i+1])
  L_arestas_int.append(linha_a)



#preenchendo a L_adj:
L_adj = [[] for _ in range(n)]
for u,v in L_arestas_int:
  L_adj[u-1].append(v)
  L_adj[v-1].append(u)



def visitar(v, L_adj, visitados, componente):
    visitados[v-1] = True
    componente.append(v)
    if len(L_adj[v-1]) != 0:
        for u in L_adj[v-1]:
            if not visitados[u-1]:
                visitar(u, L_adj, visitados, componente)

def achar_componentes(L_adj):
    visitados = []*n
    for a in range(n):
        visitados.append(False)
    componentes = []
    for v in range(n):
        if visitados[v] == False:
            componente = []
            visitar(v+1, L_adj, visitados, componente)
            componentes.append(sorted(componente))
    return componentes

def print_comps(componentes):
    
    for i in range(len(componentes)):
        for j in range(len(componentes[i])):
            if j != len(componentes[i]) - 1:
                print (componentes[i][j], end = " ")
            else:
                print (componentes[i][j], end = '')
        print('\n', end = '')

            


componentes = achar_componentes(L_adj)
print_comps(componentes)


    

