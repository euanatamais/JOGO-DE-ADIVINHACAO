def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')

    #Definir qual a palavra secreta
    palavraSecreta = "banana"

    enforcou = False
    acertou = False

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Escolha uma letra!")
        chute=chute.strip()

        index=0
        for letra in palavraSecreta:
            if(chute.upper() == letra.upper()):
                print("encontrei a letra {} na posição {}" .format( letra, index))
                index= index +1
                print(letra)
                
        print("Escolha outra letra!")


    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar_forca()