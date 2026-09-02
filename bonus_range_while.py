#ELABORE UM PROGRAMA QUE LEIA DOIS NÚMEROS (INICIO E FIM). O NÚMERO DE INICIO 
#DEVE SER MENOR QUE O NÚMERO DE FIM
#EXIBA: A QTDE DE NÚMEROS PARES E A SOMA DOS NÚMEROS ÍMPARES
opcao='S'
while opcao.upper()=='S':
    qtdePares=0
    somaImpares=0
    inicio=int(input('Valor de inicio: '))
    fim=int(input('Valor de fim: '))
    if inicio<fim: 
        for i in range(inicio,fim+1):
            if i%2==0:
                qtdePares +=1   
            else:
                somaImpares+=i
            print(f'A qtde de números pares é: {qtdePares}')
            print(f'A soma de números ímpares é: {somaImpares}')
    else:
        print('Valor de início deve ser menor que o valor de fim!!!!')
        opcao=input('Deseja continuar (S/N): ')
