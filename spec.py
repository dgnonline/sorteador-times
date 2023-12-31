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

# Exemplo de uso
time1 = ["Jogador1", "Jogador2", "Jogador3", "Jogador4", "Jogador5"]
time2 = ["Jogador6", "Jogador7", "Jogador8", "Jogador9", "Jogador10"]
espectadores = carregar_espectadores("spec.txt")

lidar_com_espectadores(time1, time2, espectadores)
