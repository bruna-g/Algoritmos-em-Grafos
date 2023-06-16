import sys
entrada_lista = sys.stdin.readlines()

#type 0.in | python trab1.py

#entrada_lista = entrada.split("\n")
e = entrada_lista[2].split("=")
n = int(e[1])

L_arestas = [] * (len(entrada_lista) - 4)
#preenchendo a L_arestas:
for j in range(len(entrada_lista) -4):
  L_arestas.append(entrada_lista[j+4])

L_arestas_int = []*(len(L_arestas))

# for k in range(len(L_arestas)):
#   aux = L_arestas[k]
#   linha_a = []*2
#   linha_a.append(aux[0])
#   linha_a.append(aux[2])
#   L_arestas_int.append(linha_a)

for k in range(len(L_arestas)):
  aux = L_arestas[k].replace("\n","")
  linha_a = []*1
  linha_a.append(aux)
  L_arestas_int.append(linha_a)




print(L_arestas)
print(L_arestas_int)

# L_adj = [] * n
# #preenchendo a L_adj:
# for i in range(n):
#   L_adj[i] = 

