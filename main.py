#Importando as funções e bibliotecas
from core.servicos import adicionar_servico,listar_servicos,limpar_tela,delay,titulo, escolher_opcao, solicitar_informações

#Iniciando as listas para armazenas os agendamentos
lista_de_servicos = []
lista_de_agendamentos = []

while True:
    limpar_tela()

    titulo("agendaSaaS")

    escolha = escolher_opcao()

    match escolha:
        #Escolha 1 - Adicionar um novo serviço
        case 1:
            #Solicita informações de nome e duração do serviço
            nome_do_servico, minutos = solicitar_informações()

            #Adiciona na lista atraves da função adicionar_servico()
            try:
                lista_de_servicos.append(adicionar_servico(nome_do_servico, minutos))
                print(f"\n{nome_do_servico} adicionado com sucesso!")
            except:
                print("Erro ao adicionar serviço, tente novamente")
            delay(2)

        #Escolha 2 - Listar serviços adicionados
        case 2:
            listar_servicos(lista_de_servicos)
            delay(1, True)
            limpar_tela()


        #Escolha 3 - Encerrar programa
        case 3:
            limpar_tela()
            print("Finalizando programa...")
            delay(1)
            limpar_tela()
            break

        #Caso escolha inválida, aviso e retorna ao loop
        case _:
            print("Escolha uma opção válida. Tente novamente: \n")