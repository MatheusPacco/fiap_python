array_dias_semana = []

total_dias_semana = 5 
range_dias_semana = range(total_dias_semana)

maior_valor_votos = 0 
dia_mais_votado = 0  

empate = 0

# Função transformando os valores em dias da semana
def DiasDaSemana(dia):
    if dia == 0:
        return "Segunda-Feira"
    if dia == 1:
        return "Terça-Feira" 
    if dia == 2:
        return "Quarta-Feira"
    if dia == 3:
        return "Quinta-Feira"
    if dia == 4:
        return "Sexta-Feira"

# Pedindo informações para o usuário sobre a quantidade de votos por seu respectivo dia 
for index in range_dias_semana:
    print("Digite quantos votos o {} º dia recebeu".format(DiasDaSemana(index)))
    array_dias_semana.append(int(input("")))
    
    # Validando o dia que adquiriu maior quantidade de votos
    if array_dias_semana[index] > maior_valor_votos:
        dia_mais_votado = index
        maior_valor_votos = array_dias_semana[index]

# Validando se não houve empate
for dias in range_dias_semana:
    if maior_valor_votos == array_dias_semana[dias] and dia_mais_votado != dias: 
        empate = 1

# Exibindo o dia escolhido 
if empate == 1:
    print("HOUVE EMPATE NA VOTAÇÃO")
else: 
    print("O dia da semana escolhido foi {}".format(DiasDaSemana(dia_mais_votado)))

print("Tabela de votos com base nos dias da semana \n")

# Exibindo os dias e seus respectivos votos
for dia in range(len(array_dias_semana)): 
    print("{} recebeu {} votos".format(DiasDaSemana(dia), array_dias_semana[dia]))
