# Crie uma função para selecionar o curso desejado em uma trilha profissional
def seleciona_curso():
  curso = int(input("Selecione o curso desejado: 1 - Análise de dados | 2 - Inteligência artificial | 3 - Python para não programadores: "))
  return curso

# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def percorre_niveis(curso_selecionado):
  trilha = {1: {'titulo': 'Análise de dados', 'total_niveis': 3}, 
            2: {'titulo': 'Inteligência artificial', 'total_niveis': 5},
            3: {'titulo': 'Python para não programadores', 'total_niveis': 7}}
  curso_atual = trilha[curso_selecionado]['titulo']
  nivel_atual = 1
  nivel_final = trilha[curso_selecionado]['total_niveis']
  print(f"Você selecionou o curso {curso_atual}")

  while nivel_atual <= nivel_final:
    print(f"Você finalizou no nível {nivel_atual} do {curso_atual}")
    nivel_atual += 1
  else:
    print(f"você finalizou o curso {curso_atual}")
 
# Execute as funções
curso_escolhido = seleciona_curso()
percorre_niveis(curso_escolhido)


        