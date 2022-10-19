import dados
from time import sleep

funcao = dados.Dadosbd()

while True:
    opcao = input(f'''
            ****** LISTA TELEFONICA ******
            
            AÇÃO DESEJADA:
            
            1-INSERIR CONTATO
            2-EXCLUIR CONTATO
            3-EDITAR CONTATO
            4-VISUALIZAR CONTATO
            5-SAIR
            :''')

    if opcao == '1':
        print('inserindo contato')
    elif opcao == '2':
        print('excluindo contato')
    elif opcao == '3':
        print('editando contato')
    elif opcao == '4':
        sleep(2)
        nome = input('Informe o nome do contato:  ')
        print('Visualizando contato...')
        sleep(2)
        vizualizar = funcao.vizualizar(nome=nome)
        sleep(4)
    elif opcao == '5':
        print('saindo')
        break
    
