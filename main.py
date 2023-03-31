from operacoesbd import *

conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria')

opcao = 10

while opcao != 9:
    print()
    print('HOSPITAL zZz')
    print('PORTAL DE OUVIDORIA')
    print()
    print('OPÇÕES:')
    print('1) Inserir nova reclamação (até mil caracteres)')
    print('2) Listar reclamações')
    print('3) Pesquisar reclamação pelo código')
    print('4) Remover reclamação pelo código')
    print('5) Inserir novo elogio e/ou sugestão (até mil caracteres)')
    print('6) Listar elogios e/ou sugestões')
    print('7) Pesquisar elogio e/ou sugestão pelo código')
    print('8) Remover elogio e/ou sugestão pelo código')
    print('9) Sair')

    print()

    opcao = input('Digite a sua opção: ')

    try:
        opcao = int(opcao)
    except ValueError:
        pass

    if opcao == 1:

        reclamacao = input('Digite a nova reclamação: ')

        consultaInserirNovaReclamacao = 'insert into reclamacoes(reclamacao) values(%s)'
        dados = (reclamacao,)

        insertNoBancoDados(conexao, consultaInserirNovaReclamacao, dados)
        print('Reclamação adicionada com sucesso!')

    elif opcao == 2:

        consultaListagem = ('select * from reclamacoes')
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Não há reclamações disponíveis')
        else:
            print()
            print('Listagem de reclamações')
            for reclamacao in listaReclamacoes:
                print('Código:', reclamacao[0], 'Reclamação:', reclamacao[1])

    elif opcao == 3:

        consultaListagem = ('select * from reclamacoes')
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Não há reclamações disponíveis')
        else:
            print()
            print('Listagem de reclamações')
            for reclamacao in listaReclamacoes:
                print('Código:', reclamacao[0], 'Reclamação:', reclamacao[1])

            print()
            print('Pesquisa de reclamação por código')
            try:
                codigo = int(input('Digite o código da reclamação: '))
                consultaListagem = ('select * from reclamacoes where codigo = ' + str(codigo))
                listaReclamacoes = listarBancoDados(conexao, consultaListagem)

                if len(listaReclamacoes) == 0:
                    print('Código inválido!')
                else:
                    print()
                    print('Resultado da pesquisa')
                    for reclamacao in listaReclamacoes:
                        print('Código:', reclamacao[0], 'Reclamação:', reclamacao[1])
            except ValueError:
                print('Código inválido!')

    elif opcao == 4:

        consultaListagem = ('select * from reclamacoes')
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Não há reclamações disponíveis')
        else:
            print()
            print('Listagem de reclamações')
            for reclamacao in listaReclamacoes:
                print('Código:', reclamacao[0], 'Reclamação:', reclamacao[1])

            print()
            try:
                codigo = int(input('Digite o código da reclamação a ser removida: '))
                consultaListagem = ('select * from reclamacoes where codigo = ' + str(codigo))
                listaReclamacoes = listarBancoDados(conexao, consultaListagem)

                if len(listaReclamacoes) == 0:
                    print('Código inválido!')
                else:
                    consultaRemoverReclamacao = 'delete from reclamacoes where codigo = %s'
                    dados = (codigo,)

                    excluirBancoDados(conexao, consultaRemoverReclamacao, dados)
                    print('Reclamação removida com sucesso!')
            except ValueError:
                print('Código inválido!')

    elif opcao == 5:

        elogioSugestao = input('Digite o novo elogio e/ou sugestão: ')
        consultaInserirNovoElogioSugestao = 'insert into elogios_sugestoes(elogio_sugestao) values(%s)'
        dados = (elogioSugestao,)

        insertNoBancoDados(conexao, consultaInserirNovoElogioSugestao, dados)
        print('Elogio e/ou sugestão adicionado(a) com sucesso!')

    elif opcao == 6:

        consultaListagem = ('select * from elogios_sugestoes')
        listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

        if len(listaElogioSugestao) == 0:
            print('Não há elogios e/ou sugestões disponíveis')
        else:
            print()
            print('Listagem de elogios e/ou sugestões')
            for elogioSugestao in listaElogioSugestao:
                print('Código:', elogioSugestao[0], 'Elogio e/ou sugestão:', elogioSugestao[1])

    elif opcao == 7:

        consultaListagem = ('select * from elogios_sugestoes')
        listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

        if len(listaElogioSugestao) == 0:
            print('Não há elogios e/ou sugestões disponíveis')
        else:
            print()
            print('Listagem de elogios e/ou sugestões')
            for elogioSugestao in listaElogioSugestao:
                print('Código:', elogioSugestao[0], 'Elogio e/ou sugestão:', elogioSugestao[1])

            print()
            try:
                codigo = int(input('Digite o código do elogio e/ou sugestão: '))
                consultaListagem = ('select * from elogios_sugestoes where codigo = ' + str(codigo))
                listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

                if len(listaElogioSugestao) == 0:
                    print('Código inválido!')
                else:
                    print()
                    print('Resultado da pesquisa')
                    for elogioSugestao in listaElogioSugestao:
                        print('Código:', elogioSugestao[0], 'Elogio e/ou Sugestão:', elogioSugestao[1])

            except ValueError:
                print('Código inválido!')

    elif opcao == 8:
        consultaListagem = ('select * from elogios_sugestoes')
        listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

        if len(listaElogioSugestao) == 0:
            print('Não há elogios e/ou sugestões disponíveis')
        else:
            print()
            print('Listagem de elogios e/ou sugestões')
            for elogioSugestao in listaElogioSugestao:
                print('Código:', elogioSugestao[0], 'Elogio e/ou sugestão:', elogioSugestao[1])

            print()
            try:
                codigo = int(input('Digite o código do elogio e/ou sugestão a ser removido(a): '))
                consultaListagem = ('select * from elogios_sugestoes where codigo = ' + str(codigo))
                listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

                if len(listaElogioSugestao) == 0:
                    print('Código inválido!')
                else:
                    consultaRemoverElogioSugestao = 'delete from elogios_sugestoes where codigo = %s'
                    dados = (codigo,)

                    excluirBancoDados(conexao, consultaRemoverElogioSugestao, dados)
                    print('Elogio e/ou sugestão removido(a) com sucesso!')
            except ValueError:
                print('Código inválido!')

    elif opcao != 9:
        print('Opção inválida!')

encerrarBancoDados(conexao)
print('Obrigado pela preferência!')
print('E volte sempre.')