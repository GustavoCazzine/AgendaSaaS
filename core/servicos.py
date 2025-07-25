from datetime import datetime, date, timedelta

#Função para receber o nome e duração do serviço.
def adicionar_servico():
    nome_servico = str(input("Nome do serviço: "))
    minutos = int(input("Duração do serviço: [Em minutos]"))

    #Converte os minutos com o timedelta
    duracao_minutos = timedelta(minutes = minutos)
    
    #Adiciona o novo serviço em um dicionário
    novo_servico = {
        "nome do servico" : nome_servico,
        "duracao_servico" : duracao_minutos
    }

    return novo_servico

#Função para listar os serviços cadastrados
def listar_servicos(lista_de_servicos):
    for servicos in lista_de_servicos:
        print(f"{servicos["nome do servico"]} - Duração: {servicos["duracao_servico"]}.")

