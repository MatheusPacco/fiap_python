# Senha composta por LIBERDADE + fatorial do minutos marcados no computador
# 1.1 Soliciar a quantidade de minutos atual
# 1.2 Realizar o fatorial dos minutos
# 1.3 Exibir para o usuário a senha correta!

print("Digite os minutos atuais:")
minuto_atual = int(input(""))
fatorial = 1

if minuto_atual == 0: 
    # Fatorial de 0 é um
    print("A senha é LIBERDADE1")
else:
    for minuto in range(1, minuto_atual + 1, 1):
        fatorial *= minuto

print(f"A senha é: \nLIBERDADE{fatorial}")