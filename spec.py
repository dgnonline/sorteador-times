import random

# Função para carregar os jogadores espectadores a partir de um arquivo txt
def carregar_espectadores(nome_arquivo):
    espectadores = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            espectadores.append(linha.strip())
    return espectadores

# Função para lidar com os espectadores
def lidar_com_espectadores(time1, time2, espectadores):
    num_espectadores = len(espectadores)

    if num_espectadores == 0:
        print("Sem espectadores")
    else:
        random.shuffle(espectadores)
        print("Espectadores:")
        for i, espectador in enumerate(espectadores):
            if i % 2 == 0:
                jogador_time_perdedor = random.choice(time1)
                time1.remove(jogador_time_perdedor)
                print(f"Espectador {i+1}: {espectador} - Tira do TIME PERDEDOR")
            else:
                jogador_time_perdedor = random.choice(time2)
                time2.remove(jogador_time_perdedor)
                print(f"Espectador {i+1}: {espectador} - Tira do TIME VENCEDOR")

# Função para calcular a média de habilidade de um time
def calcular_media_habilidade(time):
    habilidades = [jogador[1] for jogador in time]
    media = sum(habilidades) / len(habilidades)
    return media

# Exemplo de uso
time1 = [("Jogador1", 20), ("Jogador2", 25), ("Jogador3", 18), ("Jogador4", 22), ("Jogador5", 19)]
time2 = [("Jogador6", 23), ("Jogador7", 21), ("Jogador8", 24), ("Jogador9", 17), ("Jogador10", 20)]
espectadores = carregar_espectadores("spec.txt")

lidar_com_espectadores(time1, time2, espectadores)
