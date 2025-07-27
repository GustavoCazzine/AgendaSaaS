#Importando as funções e bibliotecas
from core.servicos import adicionar_servico,listar_servicos,limpar_tela,delay,titulo, escolher_opcao, solicitar_informações
from core.agendamento import calcular_horario_fim, criar_novo_agendamento, converter_string_para_datetime, validar_horario_funcionamento, verificar_conflito
#Iniciando as listas para armazenas os agendamentos
lista_de_servicos = []
lista_de_agendamentos = []
config_salao = {
    'hora_abertura': 9,  # Representa 9:00
    'hora_fechamento': 18 # Representa 18:00
}


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


        #Escolha 3 - Agendar serviço
        case 3:
            print("--- Novo Agendamento ---")
            
            # --- Coleta de Dados do Usuário ---
            # (Aqui você adicionaria a lógica para o usuário escolher o serviço, etc.)
            cliente = input("Nome do cliente: ")
            # Suponha que o usuário escolheu o primeiro serviço da lista para este exemplo
            servico_selecionado = lista_de_servicos[0] 
            horario_str = input("Digite a data e hora (dd/mm/aaaa HH:MM): ")

            # --- Processamento e Lógica ---
            # 1. Usar o "tradutor" para converter e validar a entrada de horário
            horario_obj = converter_string_para_datetime(horario_str)

            if horario_obj is None:
                print("Formato de data/hora inválido! Use dd/mm/aaaa HH:MM.")
            else:
                # 2. Chamar a função orquestradora
                sucesso, resultado = criar_novo_agendamento(
                    lista_de_agendamentos,
                    config_salao,
                    cliente,
                    servico_selecionado,
                    horario_obj
                )

                # 3. Tratar o resultado
                if sucesso:
                    # Se deu certo, o resultado é a lista atualizada
                    lista_de_agendamentos = resultado 
                    print("Agendamento realizado com sucesso!")
                else:
                    # Se deu errado, o resultado é a mensagem de erro
                    print(resultado) 
            
            input("Pressione Enter para continuar...")
        #Escolha 4 - Encerrar programa
        case 4:
            limpar_tela()
            print("Finalizando programa...")
            delay(1)
            limpar_tela()
            break

        #Caso escolha inválida, aviso e retorna ao loop
        case _:
            print("Escolha uma opção válida. Tente novamente: \n")