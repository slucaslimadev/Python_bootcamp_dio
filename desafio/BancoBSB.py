menu = """
====== BEM VINDO(A) AO BANCOBSB ======

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

======================================
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:
    opcao = input(f"Digite a opção que melhor te atende: {menu}")

    if opcao == "1":
        valor = float(input("Digite um valor para depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor invalido")
    
    elif opcao == "2":
        valor = float(input("Digite um valor para sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("O valor do saque excede o limite.!")
        elif excedeu_saques:
            print("Você excedeu o número de saques díarios! Volte amanhã")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
        else:
            print("Valor informado é invalido.")
            
    elif opcao == "3":
        print("\n =========== EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==================================")


    elif opcao == "0":
        print("Saindo ...")
        break

    else:
        print("Opção inválida, por favor tente novamente.")