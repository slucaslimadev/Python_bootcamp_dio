opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrado \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacanado ...")
    elif opcao == 2:
        print("Exibindo o extrato...")


while True:
    numero = int(input("Informe um número: "))
    if numero == 33:
        break
    print(numero)