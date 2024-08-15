# Crie uma lista
lista = [1,'a',2,'b',3,'c',4,'d',5,'e',6,'f']

# Crie um for loop para imprimir cada elemento dessa lista
for elemento in lista:
  print(elemento)

# Crie um objeto iterável utilizando a função range()
objit = range(10)
print(objit)
print(list(objit))

# Use esse objeto iterável para criar um for loop que imprima na tela a frase 
# "Estou aprendendo uma linguagem de programação."
for indice in objit:
  print(f"{indice} - Estou aprendendo uma linguagem de programação.")