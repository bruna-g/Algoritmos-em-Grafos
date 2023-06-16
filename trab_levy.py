import sys
dados = sys.stdin.readlines()
#dados = input("\n")
#d1 = dados.split("\\n")
dk = dados[2].split("=")
n = int(dk[1])
lista_arestas = [] * (len(dados)-4)
lista_vertices = [] * n
lista_grafo = [[] for _ in range(n)]
for k in range (n):
  lista_vertices.append(k+1)
for i in range (len(dados)-4):
  lista_arestas.append(dados[i+4])
  lista_arestas[i] = lista_arestas[i].split(" ")

for y in range(len(lista_arestas)):
  p1 = lista_arestas[y][0]
  p1 = int(p1)
  p2 = lista_arestas[y][1]
  p2 = int(p2)
  lista_grafo[p1-1].append(p2)
  lista_grafo[p1-1].sort()
  lista_grafo[p2-1].append(p1)
  lista_grafo[p2-1].sort()


def visitar(v, lista_grafo, visitados, componente):
  visitados[v-1] = 1
  componente.append(v)
  u = lista_grafo[v-1]
  if len(u) != 0:
    for t in u:
      if not visitados[t-1]:
        visitar(t, lista_grafo, visitados, componente)
  
def achar_componentes(lista_grafo):
  visitados = [0 for i in range(n)]
  componentes = []
  for v in range(n):
    if not visitados[v]:
      visitados
      componente = []
      visitar(v+1, lista_grafo,visitados, componente)
      componentes.append(sorted(componente))
  return componentes
  
def printarComponentes(componentes):
    saida = ""
    for c in componentes:
        saida += " ".join(map(str, c)) + '\n'
    print(saida, end="")

componentes = achar_componentes(lista_grafo)
printarComponentes(componentes)


"""for i in lista_grafo[lista_vertices[0]-1]:
    if i != None:
      for j in i:
        if j in lista_vertices:
          print(type(j))
          lista_oficial.append(lista_vertices[0])
          lista_vertices.pop(0)
          lista_vertices.insert(0,j)

print(lista_oficial)"""
"""while len(lista_vertices)!=0: 
  if lista_grafo[lista_vertices[0]-1] != []:
    for i in lista_grafo[lista_vertices[0]-1]:
        print(i)
        if i in lista_vertices:
          print("aqui2")
          lista_oficial.append(lista_vertices[0])
          lista_vertices.pop(0)
          lista_vertices.remove(i)
          lista_vertices.insert(0,i)
        else:
          lista_oficial.append(lista_vertices[0])
          lista_vertices.pop(0)
  else:
    lista_oficial.append(lista_vertices[0])
    lista_vertices.pop(0)
  print(lista_oficial)
  print(lista_vertices)


  
[lista_vertices[0]-1]
while len(lista_vertices) != 0:
  for i in lista_grafo:
    if i != None:
      for j in i:
        k.extend(lista_grafo[j-1])
        print(j)
      i.extend(k)
    lista_vertices.pop(0)
    """
  
  
  