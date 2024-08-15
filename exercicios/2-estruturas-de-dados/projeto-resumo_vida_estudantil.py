# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados 
# em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no 
# LinkedIn Learning separados por virgula em ordem cronológica
nome = input('Qual é o seu nome? ')
ano_LinkedIn = input('Em que ano conheceu o LinkedIn? ')
ano_atual = input('Qual é o ano atual? ')
cursos = input('Liste os cursos realizados por você no LinkedIn Learning em ordem cronológica separados por vírgula:\n')

# 2. Armazene esses dados em um dicionário
resumo_vida_estudantil = {'Nome': nome,
                          'Início no LinkedIn':ano_LinkedIn,
                          'Ano atual':ano_atual,
                          'Lista de cursos':cursos}

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcorridos, 
# total de cursos realizados e (apenas) o primeiro e último curso.
print("Resumo da vida estudantil:")
print(f"Nome: {resumo_vida_estudantil['Nome']}")
print(f"Ano em que conheceu o LinkedIn: {resumo_vida_estudantil['Início no LinkedIn']}")
anos_transcorridos = int(resumo_vida_estudantil['Ano atual']) - int(resumo_vida_estudantil['Início no LinkedIn']) #Calculo dos anos transcorridos
print(f"Anos transcorridos: {anos_transcorridos}")
cursos = cursos.split(', ') #Transformando string em lista
resumo_vida_estudantil['Lista de cursos'] = cursos #Armazenandoa lista no lugar da atring no dicionário
compr_lista = len(resumo_vida_estudantil['Lista de cursos'])
print(f"Total de cursos realizados: {compr_lista}")
print(f"Primeiro curso: {(resumo_vida_estudantil['Lista de cursos'])[0]}")
print(f"Último curso: {(resumo_vida_estudantil['Lista de cursos'])[-1]}")