from time import sleep


# Criar a função que será chamada
def Mensagem():

    sleep(1)

    # Opção para a mensagem
    opção = int(input("\n\033[1;34mAgora é manhã (1), tarde (2) ou noite (3)?\033[m "))

    if opção != 1 and opção != 2 and opção != 3:

        print('\n\033[1;31mOpção inválida.\033[m')
    else:
        
        # Condição
        if opção == 1:
            o = 'Dia'
        elif opção == 2:
            o = 'Tarde'
        else:
            o = 'Noite'

        msg = f'''\033[1;32m
            Bom {o}!!!
        \033[m'''

        # Enviar mensagem
        print(msg)

