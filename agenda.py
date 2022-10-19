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
        nome = input('Insira o nome do contato: ')
        numero = input(' insira o numero do contato: ')
        while True:
            confirme = input(f'você confirma nome: {nome} e numero: {numero} ?[SIM/NAO] ').upper()
            if confirme == 'SIM':
                funcao.inserir(nome, numero)
                break
            else:
                nome = input('Insira o nome do contato: ')
                numero = input(' insira o numero do contato: ')

        print('inserindo contato')

    elif opcao == '2':
        print('excluindo contato')
    elif opcao == '3':
        print('editando contato')
    elif opcao == '4':
        nome = input('Informe o nome do contato:  ')
        print('Visualizando contato...')
        vizualizar = funcao.vizualizar(nome=nome)
    elif opcao == '5':
        print('saindo')
        break
    
