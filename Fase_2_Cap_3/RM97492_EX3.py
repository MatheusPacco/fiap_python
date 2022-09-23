# Turmas compostas por 50 alunos
# 1.1 Digitar as primeiras 25 notas dos alunos com número ímpar na chamada 
# 2.1 Digitar as primeiras 25 notas dos alunos com número par na chamada
# 3.1 O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
# 3.2 Calcular a média dos 25 alunos ímpares e 25 pares
# 3.3 Exibir conjunto recebeu maior média e qual é essa média. 

# 4.1 Padrão exigido, para CADA UMA das NOTAS:
# 4.1.1 VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
# 4.1.2 POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.


total_alunos = 10
media_alunos_impares = 0 
media_alunos_pares = 0

nota_alunos_impares = 0 
nota_alunos_pares = 0

# Inserindo a nota dos alunos de número ímpar na chamada 
for numero_chamada in range(1, total_alunos + 1, 2): 
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    print("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(numero_chamada))
    nota_alunos_impares += int(input())
    
    
# Calculando a média dos alunos ímpares 
media_alunos_impares = nota_alunos_impares / 5 

print(f"A nota média dos alunos ímpares é de {media_alunos_impares: .1f}")

print("\n")

# Inserindo a nota dos alunos de número par na chamada 
for numero_chamada in range(2, total_alunos + 1, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    print("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(numero_chamada))
    nota_alunos_pares += int(input())
 
# Calculando a média dos alunos pares 
media_alunos_pares = nota_alunos_pares / 5 

print(f"A nota média dos alunos pares é de {media_alunos_pares: .1f}")

print("\n")

if media_alunos_impares > media_alunos_pares:
    print("Os alunos de número ÍMPAR tiveram uma nota média maior que a dos alunos de número PAR")
elif media_alunos_pares > media_alunos_impares: 
    print("Os alunos de número PAR tiveram uma nota média maior que a dos alunos de número ÍMPAR")
elif media_alunos_impares == media_alunos_pares:
    print("Os dois conjuntos de alunos atingiram a mesma média de nota")