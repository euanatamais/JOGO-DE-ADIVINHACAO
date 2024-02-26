print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 9

chuteString= input('Digite um número: ')


print('Você digitou o número', chuteString)

chute= int(chuteString)

if numeroSecreto == chute:
    print('Você acertou!')
elif(chute>numeroSecreto):
    print('você errou!! o numero secreto é menor')
else:
    print('Você errou!! o numero secreto é um numero maior')

