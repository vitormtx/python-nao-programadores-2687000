# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir 
# na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
lista_cursos = ['Análise de dados', 'Phyton para não programadores', 'Inteligência artificial', 'Pirâmide de testes', 
          'Arquiterura de software']
print(lista_cursos)
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso1 = 'Análise de dados'
print(curso1)
curso2 = 'Noções de Power BI'
print(curso2)
curso3 = 'Phyton para não programadores'
print(curso3)

# 3. Crie um dicionário vazio para armazenar a nota do curso
nota_cursos = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
if curso1 in lista_cursos:
  nota_curso1 = input(f"Dê a nota para o curso {curso1}: ")
  nota_cursos[curso1] = int(nota_curso1)
if curso2 in lista_cursos:
  nota_curso2 = input(f"Dê a nota para o curso {curso2}: ")
  nota_cursos[curso2] = int(nota_curso2)
if curso3 in lista_cursos:
  nota_curso3 = input(f"Dê a nota para o curso {curso3}: ")
  nota_cursos[curso3] = int(nota_curso3) 
else:
  print("Cursos não encontrados.")
  
print(nota_cursos)
