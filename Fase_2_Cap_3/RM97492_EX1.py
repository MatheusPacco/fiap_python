# 1.1 Receber o tipo de assinatura do usuário 
# 1.2 Receber o faturamento anual do usuário 
# 1.3 Calcular e exibir, com base no faturamento e na tabela de porcentagem, o valor bônus 
# que usuário terá que lhe pagar. 

# Tabela de Assinatura e bônus de faturamento 
# Basic - 30%
# Silver - 20% 
# Gold - 10%
# Platinum - 5%


tipos_assinatura = ["BASIC", "SILVER", "GOLD", "PLATINUM"] 
bonus_faturamento = [0.30, 0.20, 0.10, 0.05]
 
assinatura_valida = 0


while assinatura_valida == 0: 
    print("Digite qual é a sua Assinatura na plataforma")
    assinatura = input().upper()

    for tipo in range(len(tipos_assinatura)):
        if  assinatura == tipos_assinatura[tipo]:
            
            tipo_assinatura_usuario = assinatura
            bonus_faturamento_user = bonus_faturamento[tipo] 
            
            # Para sair do laço de repetição while
            assinatura_valida = 1  
            
    if assinatura_valida == 0: 
        print("Digite um tipo de assinatura válido")
                   
print(assinatura)

print("Digite o seu faturamento anual R$:")
faturamento_anul = float(input(""))

valor_bonus_assinatura = faturamento_anul * bonus_faturamento_user
print(f"Você terá que pagar R${valor_bonus_assinatura: .2f}")