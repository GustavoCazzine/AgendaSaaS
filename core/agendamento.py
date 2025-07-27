#Importando bibliotecas
import datetime

#Função para converter STR em horários
def converter_datetime(inicio_servico, fim_servico, horario_abertura, horario_fechamento):

    inicio_servico = datetime.datetime.strptime(inicio_servico, "%H:%M").time()
    fim_servico = datetime.datetime.strptime(fim_servico, "%H:%M").time()
    horario_abertura = datetime.datetime.strptime(horario_abertura, "%H:%M").time()
    horario_fechamento = datetime.datetime.strptime(horario_fechamento, "%H:%M").time()

    return inicio_servico, fim_servico, horario_abertura, horario_fechamento

def validar_horario_funcionamento(input_inicio_servico, input_fim_servico, input_horario_abertura="09:30", input_horario_fechamento="19:00"):

    inicio_servico, fim_servico, horario_abertura, horario_fechamento = converter_datetime(input_inicio_servico, input_fim_servico, input_horario_abertura, input_horario_fechamento)

    if inicio_servico >= horario_abertura and fim_servico <= horario_fechamento:
        print(True)
    else:
        print(False)

def verificar_conflito(lista_agendamentos, horario_inicio_novo, horario_fim_novo):
    for horarios in lista_agendamentos:
        if horarios["inicio"] >= horario_inicio_novo and horarios["fim"] <= horario_fim_novo:
            horario_ocupado = True
        else:
            horario_ocupado = False
    
    if horario_ocupado:
        print("Horario ocupado")
    else:
        print("horario livre")

agendamentos = [{
    "inicio": "09:30",
    "fim": "10:30"
}, {
    "inicio": "10:30",
    "fim": "11:00"
}, {
    "inicio": "13:30",
    "fim": "14:30"
}]

verificar_conflito(agendamentos, "16:00", "17:00")