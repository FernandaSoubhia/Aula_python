#Usuário digite a sua idade e o programa deve verificar !
#Menor que 16 anos não pode votar
#entre 16 e 17 o voto é facultativo
#18+ voto obrigatótio
idade=int(input('Digite sua idade: '))
if idade>16:#estrutura condicional encadeado
     print('Não pode votar')
elif idade<=17:
     print('Voto facultativo!')
else:
    print('Voto obrigatório!') 