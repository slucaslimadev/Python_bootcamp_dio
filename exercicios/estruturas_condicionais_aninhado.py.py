conta_normal = False
conta_uni = True

saldo = 2000
saque = 2010   
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <+ (saldo + cheque_especial):
        print("Saque realizado com sucesso com o uso do cheque especial!")

elif conta_uni:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")