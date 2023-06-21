import random

# Função para carregar os jogadores e níveis de habilidade a partir de um arquivo txt
def carregar_jogadores(nome_arquivo):
    jogadores = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            jogador, habilidade = linha.strip().split(',')
            jogadores.append((jogador, int(habilidade)))
    return jogadores

# Função para carregar a sequência de mapas a partir de um arquivo txt
def carregar_mapas(nome_arquivo):
    mapas = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            mapas.append(linha.strip())
    return mapas

# Função para sortear os times
def sortear_times(jogadores):
    jogadores_ordenados = sorted(jogadores, key=lambda x: x[1], reverse=True)

    time1 = []
    time2 = []

    for i, jogador in enumerate(jogadores_ordenados):
        if i % 2 == 0:
            time1.append(jogador)
        else:
            time2.append(jogador)

    return time1, time2

# Função para sortear a sequência de mapas
def sortear_sequencia_mapas(mapas):
    sequencia_sorteada = random.sample(mapas, len(mapas))
    return sequencia_sorteada

# Função para exibir os times e a sequência de mapas
def exibir_resultados(time1, time2, sequencia_mapas):
    print("Time 1:")
    for jogador in time1:
        print(f"Jogador: {jogador[0]}, Habilidade: {jogador[1]}")
    print("")

    print("Time 2:")
    for jogador in time2:
        print(f"Jogador: {jogador[0]}, Habilidade: {jogador[1]}")
    print("")

    print("Sequência de Mapas:")
    for i, mapa in enumerate(sequencia_mapas):
        print(f"Mapa {i+1}: {mapa}")

# Nome dos arquivos txt que contêm os jogadores, níveis de habilidade e a sequência de mapas
nome_arquivo_jogadores = "jogadores.txt"
nome_arquivo_mapas = "mapas.txt"

# Carrega os jogadores e a sequência de mapas a partir dos arquivos
jogadores = carregar_jogadores(nome_arquivo_jogadores)
mapas = carregar_mapas(nome_arquivo_mapas)

# Verifica se existem pelo menos 10 jogadores para formar os times
if len(jogadores) < 10:
    print("Número insuficiente de jogadores.")
else:
    # Sorteia os times
    random.shuffle(jogadores)
    time1, time2 = sortear_times(jogadores)

    # Sorteia a sequência de mapas
    sequencia_mapas = sortear_sequencia_mapas(mapas)

    # Exibe os times e a sequência de mapas
    exibir_resultados(time1, time2, sequencia_mapas)
