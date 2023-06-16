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

#tent 1 lista de listas de arestas
# L_arestas_int = []*(len(L_arestas))
# for k in range(len(L_arestas)):
#   aux = L_arestas[k].replace("\n","")
#   linha_a = []*1
#   linha_a.append(aux)
#   L_arestas_int.append(linha_a)


#L_arestas de string p/ inteiros:
L_aux1 = []*(2*len(L_arestas))
for k in range(len(L_arestas)):
  aux1 = L_arestas[k].replace("\n","")
  aux2 = aux1.split(" ")
  L_aux1.append(int(aux2[0]))
  L_aux1.append(int(aux2[1]))



# L_arestas_int.append(L_aux)
# L_aux = L_arestas[k].split(" ")



print(L_aux1)
# print(L_arestas_int)

# L_adj = [] * n
# #preenchendo a L_adj:
# for i in range(n):
#   L_adj[i] = 

