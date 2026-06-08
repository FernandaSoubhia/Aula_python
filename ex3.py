#Peça ao usuário 5 números e mostre a soma deles ao final.
soma = 0
for i in range(5):
    numero = float(input(f"Digite um número: ")) 
    soma += numero
print("A soma é:" , soma)