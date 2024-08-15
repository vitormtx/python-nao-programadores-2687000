# Crie uma lista apenas com elementos numéricos
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] # o numero seguinte é igual à soma dos dois anteriores
print (fibonacci)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = [1, -1, 3.14, 5/2, 'trabalho', True, False, [1,2,3,4], ['c', 'c++', 'python', 'sql'], fibonacci]
print (lista_mista)

# Imprima na tela apenas os 5 primeiros elementos da lista
print (lista_mista [0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print (lista_mista [0:-1:2])

# Remova da lista o último item
compr = len(lista_mista)
print(compr) #comprimento da lista

#Maneira 1:
lista_mista.pop()
print(lista_mista)

compr = len(lista_mista) #novo comprimento da lista após o pop
print(compr)

#Maneira 2:
lista_mista.remove(lista_mista[compr-1])
print(lista_mista)

compr = len(lista_mista) #novo comprimento da lista após o remove
print(compr)


# Insira na lista um novo item
lista_mista.append('Novo item')
print(lista_mista)

# Remova da lista um item específico
lista_mista.remove(3.14)
print(lista_mista)