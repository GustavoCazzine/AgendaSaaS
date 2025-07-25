#Importando as funções e bibliotecas
from core.servicos import adicionar_servico, listar_servicos
import os

#Iniciando as listas para armazenas os agendamentos
lista_de_servicos = []
lista_de_agendamentos = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Adicionar Serviço \n2 - Listar Serviços")

    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            #Solicita informações de nome e duração do serviço
            nome_do_servico = str(input("Nome do serviço: "))
            minutos = int(input("Duração do serviço: (minutos): "))
            #Adiciona na lista atraves da função adicionar_servico()
            lista_de_servicos.append(adicionar_servico(nome_do_servico, minutos))

        case 2:
            listar_servicos(lista_de_servicos)

        case 3:
            print("Finalizando programa...")
            
            break
        case _:
            print("Escolha uma opção válida. Tente novamente: \n")