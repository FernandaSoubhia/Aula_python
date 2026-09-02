def soma():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a + b
    print("Resultado: ", resultado)

def subtracao(a, b):
    resultado = a - b
    print("Resultado: ", resultado)

def multiplicacao():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a * b

def divisao(a, b):
    return a / b 

print("Escolha a operação")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Opção: "))

if opcao == 1:
    soma()
elif opcao == 2:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    subtracao(n1, n2)
elif opcao == 3:
    resultado = multiplicacao()
    print("Resultado:", resultado)
elif opcao == 4:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = divisao(n1, n2)
    print("REsultado:", resultado)
else:
    print("Opção inválida")