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

L_adj = [] * n
# #preenchendo a L_adj:


for m in range(n):
  for p in range(len(L_arestas_int)):
    for q in range(2):
      if (L_arestas_int[p][q] == (m+1)):
        linha_aux = []
        linha_aux.append(L_arestas_int[p][q-1])
        L_adj.insert(m, linha_aux)
        # print(linha_aux)
        # L_adj.insert(9, L_arestas_int[p][q-1])
      # else:
      #   L_adj.insert(m, " ")
  

    
print(L_adj)



