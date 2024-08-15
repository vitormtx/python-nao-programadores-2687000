# Declare 4 variáveis do tipo numérica
a = 1
b = 1
c = 2
d = 3

# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if a>c:
  print(f"A condição foi cumprida pois {a} é maior que {c}.")
else:
  print(f"Acondição não foi cumprida pois {c} é maior que {a}.")

# Insira outras condições na estrutura condicional usando o elif
if a>c:
  print(f"A condição foi cumprida pois {a} é maior que {c}.")
elif (b==d):
  print(f"A condição foi cumprida pois {b} é igual a {d}.")
else:
  print(f"As condições não foram cumpridas pois {c} é maior que {a} e {b} é diferente de {d}.")

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (a>c or a==d) :
  print(f"A condição foi cumprida pois {a} é maior que {c} ou {a} é igual a {d}.")
elif (b==d and d>c):
  print(f"A condição foi cumprida pois {b} é igual a {d} e {d} é maior que {c}.")
else:
  print(f"As condições não foram cumpridas.")

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if (a!=c):
  print(f"A condição foi cumprida pois {a} é diferente de {c}.")
if (d>c):
  print(f"A condição foi cumprida pois {d} é maior que {c}.")
