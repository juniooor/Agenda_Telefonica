from ast import Break


while True:
    opcao = input(f'''
            ****** LISTA TELEFONICA ******
            
            AÇÃO DESEJADA:
            
            1-INSERIR NUMERO
            2-EXCLUIR NUMERO
            3-EDITAR NUMERO
            4-VISUALIZAR NUMERO
            5-SAIR
            :''')

    if opcao == '2':
        print('excluindo')
    elif opcao == '1':
        print('inserindo numero')
    elif opcao == '3':
        print('editando numero')
    elif opcao == '4':
        print('Visualizando numero')
    elif opcao == '5':
        print('saindo')
        break