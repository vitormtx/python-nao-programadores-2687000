# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Qual é o seu nome? ')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Quantos dias de estudo você dedica por semana? ')

# 3. Crie uma variável chamada "total_horas" e, usando o método input(), solicite a média de horas estudada por dia;
total_horas = input('Quantas horas em média você estuda por dia? ')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Qual é o título do curso? ')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais 
# e o curso.
horas_por_semana = int(total_horas)*int(total_dias)
#Maneira 1
print('Olá',nome,', você dedica',total_dias,'dias por semana aos estudos, estuda em média',horas_por_semana,'horas por semana e está cursando',curso,'.') 
#Maneira 2 (melhor!)
print(f'Olá {nome}, você dedica {total_dias} dias por semana aos estudos, estuda em média {horas_por_semana} horas por semana e está cursando {curso}.') 
