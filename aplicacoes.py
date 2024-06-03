import time

lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0]

for i in range(1, len(lista)):
    if lista [i] > maior_numero:
        maior_numero = lista[i]
print("O maior número da lista é:", maior_numero)

# Exemplo 2 
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2:", maior)

# Exemplo 3:
ultima_lista = my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
        mel = i
print("Maior valor 3:", mel)

# Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Elemento encontrado no índice:", i)
else:
    print("NÃO ENCONTRADO!")     
# Conferidor de aposta em loteria
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
   if numero in apostados:
        acertos += 1

print(acertos)

# Remoção de números repetidos em uma lista
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original:", lista)

# Listas de apoio
vistos = []

# Iterar pela lista original de trás para frente
for i in range(len(lista) - 1, -1, -1):
    # Se o número já está na lista "vistos", removê-lo da lista original
    if lista[i] in vistos:
        del lista[i]
    else:
        # Caso contrário, adicionar à lista "vistos"
        vistos.append(lista[i])
# Exibir a lista original modificada
print("Lista modificada:", lista)


# Listas avançadas
# 2D - listas aninhadas bidimensionais
tabela = [[":("], ":)",[":|", ";-;"], [";-;", ":|", ":)", ":("], [":|", ":)", ";-;", ":("]]
print(tabela[2][1])
print(tabela)

#3D - Matriz trimidensional
cubo = [[1,2,3], [2,3,1], [3,2,1]],
[[4,5,6], [5,6,4], [6,5,4]],
[[7,8,9], [8,9,7], [9,8,7]]
print(cubo)
print(cubo[1][0])
print(cubo[1][0][2])
time.sleep(3)