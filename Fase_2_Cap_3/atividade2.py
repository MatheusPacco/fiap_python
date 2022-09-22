array_dias_semana = [];  
print("Hellou world")

total_dias_semana = 5 
range_dias_semana = range(total_dias_semana)

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


def ExibindoVotos(voto_por_dia): 
    for dia in range_dias_semana:
        print("O dia {} º, recebeu {} votos".format(DiasDaSemana(dia), voto_por_dia[dia]))

for index in range_dias_semana:
    # print(index)
    print("Digite quantos votos o {} º dia recebeu".format(DiasDaSemana(index)))
    array_dias_semana.append(int(input("")))

    # Exibindo os dias e seus respectivos votos
    if index == 4: 
        ExibindoVotos(array_dias_semana)

