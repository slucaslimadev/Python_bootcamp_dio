idade_permitida = 18

idade_user = int(input("Digite sua idade:"))

if idade_user >= idade_permitida:
    print("Idade permitida")
else:
    print("Menor de idade")


crianca = 12
adolescente = 18
adulto = 40
idoso = 90

user_id = int(input("Qual sua idade"))

if user_id <= crianca:
    print("Você é criança")
elif user_id <= adolescente:
    print("Você é adolescente") 
elif user_id <= adulto:
    print("Você é adulto")
else:
    print("Idoso")