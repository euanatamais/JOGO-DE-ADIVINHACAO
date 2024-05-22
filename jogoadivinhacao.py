import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = round(random.random()*100)
#print(numeroSecreto)
#Definindo o número de tentativas e rodada
numeroTentativas = 0
rodada = 1
pontos=1000

print('qual o nivel de dificuldade?')
print('(1)-facil, (2)-medio (3)-dificil')

while(rodada <= numeroTentativas):
    print('Tentativa',rodada, 'de' , numeroTentativas)

nivel=int(input('defina o nivel:'))

if(nivel==1):
    numeroTentativas=20
elif(nivel==2):
    numeroTentativas=10
else:
    numeroTentativas=5


#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou! E sua pontuação foi: ', pontos)
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
    pontos_perdidos=abs(numeroSecreto-chute)
    pontos=pontos-pontos_perdidos

    #numeroTentativas = numeroTentativas - 1
    rodada = rodada + 1



#Aula Elif 26.02.24

