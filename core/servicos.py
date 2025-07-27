#Importnado bibliotecas para formatações e organização
from datetime import datetime, date, timedelta
import os
import time

#Função para solicitar nome do serviço e minutos de duração
def solicitar_informações():

    limpar_tela()

    while True:
        try:
            nome_do_servico = str(input("Nome do serviço: "))

            if nome_do_servico:
                while True: 
                    try: 
                        minutos = int(input("Duração do serviço: (minutos): "))

                        if nome_do_servico and minutos:
                            return nome_do_servico, minutos
                        
                        else:
                            print("Erro inesperado, tente novamente.")
                            delay(2)
                            limpar_tela()
                            break
                        
                    except:
                        
                        print("Digite a duração total do serviço, em minutos (1 hora = 60 minutos).")
            else:
                limpar_tela()
                print("Campo em branco, informe o nome do serviço")
        except:
            print("Insira o nome do serviço, tente novamente...")   

#Função para receber o nome e duração do serviço.
def adicionar_servico(nome_do_servico, minutos):
    #Converte os minutos com o timedelta
    duracao_minutos = timedelta(minutes = minutos)
    
    #Adiciona o novo serviço em um dicionário
    novo_servico = {
        "nome do servico" : nome_do_servico,
        "duracao_servico" : duracao_minutos
    }

    return novo_servico

#Função para listar os serviços cadastrados
def listar_servicos(lista_de_servicos):
    limpar_tela()
    if not lista_de_servicos:
        print("\nNenhum serviço cadastrado.")
    else:
        for servicos in lista_de_servicos:
            print(f"\n{(servicos["nome do servico"]).capitalize()} - Duração: {servicos["duracao_servico"]}")

#Função para limpar o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função para uma pausa no terminal
def delay(segundos, continuar=False):
    if continuar:
        input("\nPressione ENTER para continuar...")
    else:
        time.sleep(segundos)

#Função para preparar titulos padronizados
def titulo(msg):
    print(f"\n--- {msg.upper()} ---\n")

#Função para listar as opções
def listar_opcoes():
        
    opcoes = ["Adicionar Serviço", "Listar Serviços", "Agendar Serviço","Sair\n"]

    for e, opcao in enumerate(opcoes,start=1):
        print(f"{e}. {opcao}")

    return opcoes

#Função que trabalha junto ao listar_opcoes() e retorna a escolha do usuario
def escolher_opcao():

    opcoes = listar_opcoes()

    quantidade_opcoes = len(opcoes)

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha > 0 and escolha <= quantidade_opcoes:
                return escolha
            else:
                limpar_tela()
                print(f"\nEscolha inválida, escolha uma entre as {quantidade_opcoes} opções\n")
                listar_opcoes()
        except:
            limpar_tela()
            print("\nDigite o número referente a opção desejada, tente novamente...\n")
            listar_opcoes()