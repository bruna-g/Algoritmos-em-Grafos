import sys
entrada_lista = sys.stdin.readlines()

#type 0.in | python trab1_v7.py

#entrada_lista = entrada.split("\n")
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

print(L_arestas_int)

#preenchendo a L_adj:
L_adj = [[] for _ in range(n)]
for u,v in L_arestas_int:
  L_adj[u-1].append(v)
  L_adj[v-1].append(u)



visitados = []*n
for a in range(n):
  visitados.append(False)



'''componentes = []
def visitar(L_adj):
  componente = []
  for v in L_adj:
    visitados[L_adj.index(v)] = True
    componente.append(L_adj.index(v)+1)
    vizinhos = L_adj[L_adj.index(v)]
    if len(vizinhos) != 0:
        for i in vizinhos:
            if visitados[i-1] == False:
                componente.append(i+1)
                visitados[i-1] = True
                visitados[L_adj.index(v)] = True
            # else:
            #     visitados[i-1] = True
       
  componentes.append(componente)

def visitar(p):
   componente = []
   visitados[p] = True
   componente.append(p-1)'''


componentes = []

def viz(vizinhos, componente):
    if len(vizinhos) != 0:
        for i in vizinhos:
            if visitados[i-1] == False:
                componente.append(i+1)
                visitados[i-1] = True
                viz(vizinhos, componente)
    return componente
            # else:
            #     visitados[i-1] = True


def visitar(L_adj):
  componente = []
  for v in L_adj:
    visitados[L_adj.index(v)] = True
    componente.append(L_adj.index(v)+1)
    vizinhos = L_adj[L_adj.index(v)]
    viz(vizinhos, componente)
       
  componentes.append(componente)



# componentes = []
# def visitar(L_adj):
#   componente = []
#   for v in L_adj:
#     if visitados[L_adj.index(v)] == False:
#         componente.append(L_adj.index(v)+1)
#         vizinhos = L_adj[L_adj.index(v)]
#         for i in vizinhos:
#             if visitados[i-1] == False:
#                 componente.append(i+1)
#             else:
#                 visitados[i-1] = True
#     else:
#         visitados[L_adj.index(v)] == True
    
       
#   componentes.append(componente)

visitar(L_adj)

print(componentes)
print(visitados)

    



