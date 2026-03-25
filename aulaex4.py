#Leia a nota de um aluno.
#Se a nota for maior ou igual a 6, mostre:
#"Aprovado".
#Se a nota estiver entre 4 e 5.9, mostre:
#"Recuperação".
#Caso contrário, mostre:
#"Reprovado".
nota = float(input("Digite a nota: "))
if nota >= 6:
    print("Aprovado")
elif nota >= 4:
    print("Recuperação")
else:
    print("Reprovado")