salario = 2500

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))