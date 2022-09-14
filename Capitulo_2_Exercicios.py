from re import I
from socket import INADDR_ALLHOSTS_GROUP
from traceback import print_tb
from xml.dom import InuseAttributeErr


# 1 - Informar seus batimentos cardiacos
# 1.1 -Informar a idade

# 2 - Com base na tabela de BTM ideal para cada idade, realizar as seguintes comparaçõs
# 2.1 - O BTM está acima da faixa adequada
# 2.2 - O BTM está abaixo da faixa adequada 
# 2.3 - O BTM está dentro da faixa adequada 

# 3.1 - Até 2 anos a faixa adequada é de 120 a 140
# 3.2 -  De 8 a até 17 anos a faixa adequada é de 80 a 100
# 3.3 - É considerado adulto sedentario aquele com 70 a 80 
# 3.4 - E idosos estão dentro da faixa de 50 a 60 


print("Informe os seus batimentos cardíacos")
btm = int(input("BTM: ")); 

print("Digite a sua idade, para que possamos mensurar a faixa adequada dos seus batimentos cardíacos")

idade = int(input("IDADE: ")); 

if idade <= 2:
    if btm >= 120 and btm <= 140:
        print("Está dentro da faixa adequada") 
    if btm > 140:  
        print("Está acima da faixa adequada")
    if btm < 120:
        print("Está a baixo da faixa adequada")
else:
    if idade >= 8 and idade <= 64: 
        if btm >= 80 and btm <= 100:
            print("Está dentro da faixa adequada")
        if btm >= 70 and btm <= 80:
            print("Você é um adulto sedentario")
        if btm > 100:
            print("Está acima da faixa adequada")
        if btm < 70:
            print("Está abaixo da faixa adequada")
    else: 
        if btm >= 50 and btm <= 60:
            print("Seu batimento está dentro da faixa adequada") 
        if btm > 60:
            print("Seu batimento está acima da faixa adequada")
        if btm < 50:
            print("Seu batimento está abaixo da faixa adequada")
# O pthon exige encadeamento com tab para manter a legibilidade