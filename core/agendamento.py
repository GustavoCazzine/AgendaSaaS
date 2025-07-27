
from datetime import datetime, timedelta

# --- FUNÇÕES AJUDANTES (Helpers) ---
# Funções pequenas com uma única responsabilidade.

def converter_string_para_datetime(string_horario):
    """
    Tenta converter uma string de texto em um objeto datetime.
    Esta é a nossa "ponte" entre o que o usuário digita e o que o Python entende.
    """
    try:
        # datetime.strptime significa "string parse time" (analisar tempo a partir de uma string).
        # O primeiro argumento é a string que queremos converter.
        # O segundo argumento é o FORMATO que esperamos. %d=dia, %m=mês, %Y=ano, %H=hora, %M=minuto.
        return datetime.strptime(string_horario, "%d/%m/%Y %H:%M")
    except ValueError:
        # Se o usuário digitar algo que não bate com o formato (ex: "amanhã"),
        # a conversão dará um erro (ValueError). Nós o capturamos e retornamos None
        # para sinalizar que a entrada foi inválida.
        return None

def calcular_horario_fim(horario_inicio, servico):
    """
    Calcula o horário de término de um agendamento.
    """
    # A beleza de ter a duração como um objeto timedelta é que podemos simplesmente somá-la
    # a um objeto datetime para obter o resultado correto.
    return horario_inicio + servico['duracao_servico']

# --- FUNÇÕES DE VALIDAÇÃO ---
# Funções que respondem a uma pergunta com "Sim" (True) ou "Não" (False).

def validar_horario_funcionamento(horario_inicio, horario_fim, config_salao):
    """
    Verifica se o agendamento está dentro do horário de funcionamento do salão.
    """
    # Acessamos o atributo .hour de um objeto datetime para pegar apenas a hora.
    # Verificamos se o agendamento não começa antes da abertura E não termina depois do fechamento.
    if (horario_inicio.hour >= config_salao['hora_abertura'] and
        horario_fim.hour <= config_salao['hora_fechamento']):
        return True  # Horário Válido
    else:
        return False # Horário Inválido

def verificar_conflito(lista_de_agendamentos, horario_inicio_novo, horario_fim_novo):
    """
    Verifica se um novo agendamento se sobrepõe a algum agendamento existente.
    Esta é a lógica mais complexa.
    """
    # Para cada agendamento que já existe na nossa lista...
    for agendamento_existente in lista_de_agendamentos:
        inicio_existente = agendamento_existente['inicio']
        fim_existente = agendamento_existente['fim']

        # A CONDIÇÃO DE CONFLITO:
        # Pense em duas réguas de tempo. Uma sobrepõe a outra se:
        # O início do novo agendamento vem ANTES do fim do antigo
        # E (AND)
        # O fim do novo agendamento vem DEPOIS do início do antigo.
        # Se ambas as condições forem verdadeiras, temos uma sobreposição.
        if horario_inicio_novo < fim_existente and horario_fim_novo > inicio_existente:
            return True  # Conflito encontrado!
    
    # Se o laço terminar e nenhum conflito for encontrado, o horário está livre.
    return False # Sem conflitos

# --- FUNÇÃO PRINCIPAL (ORQUESTRADORA) ---

def criar_novo_agendamento(lista_de_agendamentos, config_salao, nome_cliente, servico_escolhido, horario_inicio):
    """
    Orquestra todo o processo de criação de um novo agendamento.
    Ela usa todas as outras funções para fazer seu trabalho.
    """
    # 1. Calcular o horário de término
    horario_fim = calcular_horario_fim(horario_inicio, servico_escolhido)

    # 2. Validar horário de funcionamento
    if not validar_horario_funcionamento(horario_inicio, horario_fim, config_salao):
        # Se a validação falhar, retornamos imediatamente com uma tupla de falha.
        return (False, "Erro: O horário solicitado está fora do expediente do salão.")

    # 3. Validar conflitos
    if verificar_conflito(lista_de_agendamentos, horario_inicio, horario_fim):
        # Se a validação de conflito falhar, retornamos com uma tupla de falha.
        return (False, "Erro: Horário indisponível. Já existe um agendamento neste período.")

    # 4. Se tudo passou, criar e adicionar o agendamento
    novo_agendamento = {
        'cliente': nome_cliente,
        'servico': servico_escolhido,
        'inicio': horario_inicio,
        'fim': horario_fim
    }
    lista_de_agendamentos.append(novo_agendamento)

    # 5. Retornar uma tupla de sucesso com a lista atualizada.
    return (True, lista_de_agendamentos)