import schedule as s
from time import sleep
import função


try:
    print("\033[1;33mEsperando para executar...\n")

    # Executar a cada 5 segundos
    s.every(5).seconds.do(função.Mensagem)

    while 1:
        s.run_pending()
        sleep(1)
    
    while True:
        print('\033[1;33m\nEsperando para executar novamente...\033[m')

except KeyboardInterrupt:
    print("\033[1;32m\nPrograma foi interrompido pelo usuário.\033[m")

