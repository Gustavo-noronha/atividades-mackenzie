import random

# SUPER TRUNFO - TEMA: PLANETAS DO SISTEMA SOLAR



# gabarito dos atributos (índice 0 é o nome, demais são atributos)
# [nome, diametro_km, distancia_sol_UA, num_luas, gravidade_ms2]
GABARITO = [
    "Nome",
    "Diâmetro (km)",
    "Distância do Sol (UA)",
    "Nº de Luas",
    "Gravidade (m/s²)"
]

#Baralho que a gente escolheu sobre planetas e as luas suas luas
BARALHO_BASE = [
    ["Mercúrio",    4879,    0.39,   0,   3.7],
    ["Vênus",      12104,    0.72,   0,   8.9],
    ["Terra",      12742,    1.00,   1,   9.8],
    ["Marte",       6779,    1.52,   2,   3.7],
    ["Júpiter",   139820,    5.20,  95,  24.8],
    ["Saturno",   116460,    9.58,  83,  10.4],
    ["Urano",      50724,   19.22,  27,   8.7],
    ["Netuno",     49244,   30.05,  14,  11.2],
    ["Plutão",      2376,   39.48,   5,   0.6],
    ["Ceres",        945,    2.77,   0,   0.3],
    ["Éris",        2326,   67.67,   1,   0.8],
    ["Haumea",      1960,   43.13,   2,   0.6],
    ["Makemake",    1430,   45.79,   1,   0.5],
    ["Io",          3643,    5.20,   0,   1.8],   # lua de Júpiter
    ["Europa",      3122,    5.20,   0,   1.3],   # lua de Júpiter
    ["Ganimede",    5262,    5.20,   0,   1.4],   # lua de Júpiter
    ["Titã",        5150,    9.58,   0,   1.4],   # lua de Saturno
    ["Caronte",     1212,   39.48,   0,   0.3],   # lua de Plutão
    ["Triton",      2707,   30.05,   0,   0.8],   # lua de Netuno
    ["Miranda",      472,   19.22,   0,   0.1],   # lua de Urano
]


def criar_baralho():
    # retorna cópia do baralho base para não modificar o original
    baralho = []
    for carta in BARALHO_BASE:
        baralho.append(carta[:])  # copia a sublista
    return baralho


def embaralhar(baralho):#embaralha
    random.shuffle(baralho)


def distribuir(baralho):#distribui
    metade = len(baralho) // 2
    jogador1 = baralho[:metade]
    jogador2 = baralho[metade:]
    return jogador1, jogador2


def exibir_carta(carta, mostrar_atributos=True):
    if mostrar_atributos:
        print(f"     {carta[0]:<26}")
        for i in range(1, len(GABARITO)):
            nome_attr = GABARITO[i]
            valor = carta[i]
            print(f"    [{i}] {nome_attr:<18} {valor:>6} ")
    else:
        print(f"        (carta oculta)          ")


def escolher_atributo(carta):
    print("\n  Escolha o atributo para comparar:")
    for i in range(1, len(GABARITO)):
        print(f"    [{i}] {GABARITO[i]}")

    while True:
        try:
            escolha = int(input("\n  Sua escolha: "))
            if 1 <= escolha <= len(GABARITO) - 1:
                return escolha
            else:
                print("    Número fora do intervalo, tente de novo.")
        except ValueError:
            print("    Digite apenas um número.")


def pc_escolher_atributo(carta):
    # o pc escolhe o atributo de maior valor
    melhor_idx = 1
    for i in range(2, len(GABARITO)):
        if carta[i] > carta[melhor_idx]:
            melhor_idx = i
    return melhor_idx


def comparar(carta1, carta2, idx_atributo):
    v1 = carta1[idx_atributo]
    v2 = carta2[idx_atributo]
    if v1 > v2:
        return 1   # jogador 1 vence
    elif v2 > v1:
        return 2   # jogador 2 vence
    else:
        return 0   # empate


def pausar():
    input("\n  [Enter para continuar...]")




def jogar_single_player():#jogar contra PC
    print("    MODO: VOCÊ VS COMPUTADOR")
    baralho = criar_baralho()
    embaralhar(baralho)
    mao_jogador, mao_pc = distribuir(baralho)

    monte_espera = []   # cartas em caso de empate
    rodada = 0
    vez_humano = True   # humano começa

    while len(mao_jogador) > 0 and len(mao_pc) > 0:
        rodada += 1
        print(f"  Rodada {rodada} | Você: {len(mao_jogador)} cartas | PC: {len(mao_pc)} cartas")

        carta_jogador = mao_jogador[0]
        carta_pc = mao_pc[0]

        if vez_humano:
            print("\n  Sua carta:")
            exibir_carta(carta_jogador)
            print("\n  Carta do PC: (oculta)")
            exibir_carta(carta_pc, mostrar_atributos=False)

            idx = escolher_atributo(carta_jogador)
        else:
            print("\n  Vez do PC escolher o atributo.")
            print("\n  Sua carta:")
            exibir_carta(carta_jogador)
            print("\n  Carta do PC:")
            exibir_carta(carta_pc)

            idx = pc_escolher_atributo(carta_pc)
            print(f"\n  PC escolheu: [{idx}] {GABARITO[idx]}")

        resultado = comparar(carta_jogador, carta_pc, idx)

        print(f"\n   Comparando '{GABARITO[idx]}':")
        print(f"     Você  → {carta_jogador[idx]}")
        print(f"     PC    → {carta_pc[idx]}")

        # remove as cartas do topo
        mao_jogador.pop(0)
        mao_pc.pop(0)

        if resultado == 1:
            print("\n  VOCÊ VENCEU a rodada!")
            mao_jogador.append(carta_jogador)
            mao_jogador.append(carta_pc)
            for c in monte_espera:
                mao_jogador.append(c)
            monte_espera = []
            vez_humano = True

        elif resultado == 2:
            print("\n   PC VENCEU a rodada!")
            mao_pc.append(carta_jogador)
            mao_pc.append(carta_pc)
            for c in monte_espera:
                mao_pc.append(c)
            monte_espera = []
            vez_humano = False

        else:
            print("\n   EMPATE! Cartas vão pro monte de espera.")
            monte_espera.append(carta_jogador)
            monte_espera.append(carta_pc)
            # vez não muda

        pausar()

    # resultado final
    print("\n" + "="*50)
    if len(mao_jogador) == 0:
        print("   PC VENCEU O JOGO!")
    else:
        print("   VOCÊ VENCEU O JOGO! Parabéns!")
    print(f"  Total de rodadas: {rodada}")
    print("="*50)




def jogar_dual_player():#dois jogadores
    print("    MODO: JOGADOR 1 VS JOGADOR 2")

    nome1 = input("\n  Nome do Jogador 1: ").strip() or "Jogador 1"
    nome2 = input("  Nome do Jogador 2: ").strip() or "Jogador 2"

    baralho = criar_baralho()
    embaralhar(baralho)
    mao1, mao2 = distribuir(baralho)

    monte_espera = []
    rodada = 0
    vez = 1   # 1 ou 2

    while len(mao1) > 0 and len(mao2) > 0:
        rodada += 1
        print(f"  Rodada {rodada} | {nome1}: {len(mao1)} cartas | {nome2}: {len(mao2)} cartas")

        carta1 = mao1[0]
        carta2 = mao2[0]

        if vez == 1:
            nome_vez = nome1
            print(f"\n  Vez de {nome1} escolher!")
            print(f"\n  Sua carta ({nome1}):")
            exibir_carta(carta1)
            print(f"\n  Carta de {nome2}: (oculta)")
            exibir_carta(carta2, mostrar_atributos=False)
            idx = escolher_atributo(carta1)
        else:
            nome_vez = nome2
            print(f"\n  Vez de {nome2} escolher!")
            print(f"\n  Carta de {nome1}: (oculta)")
            exibir_carta(carta1, mostrar_atributos=False)
            print(f"\n  Sua carta ({nome2}):")
            exibir_carta(carta2)
            idx = escolher_atributo(carta2)

        resultado = comparar(carta1, carta2, idx)

        print(f"\n   Comparando '{GABARITO[idx]}':")
        print(f"     {nome1} → {carta1[idx]}")
        print(f"     {nome2} → {carta2[idx]}")

        mao1.pop(0)
        mao2.pop(0)

        if resultado == 1:
            print(f"\n   {nome1} VENCEU a rodada!")
            mao1.append(carta1)
            mao1.append(carta2)
            for c in monte_espera:
                mao1.append(c)
            monte_espera = []
            vez = 1

        elif resultado == 2:
            print(f"\n   {nome2} VENCEU a rodada!")
            mao2.append(carta1)
            mao2.append(carta2)
            for c in monte_espera:
                mao2.append(c)
            monte_espera = []
            vez = 2

        else:
            print("\n  EMPATE! Cartas vão pro monte de espera.")
            monte_espera.append(carta1)
            monte_espera.append(carta2)

        pausar()

    if len(mao1) == 0:
        print(f"   {nome2} VENCEU O JOGO!")
    else:
        print(f"   {nome1} VENCEU O JOGO!")
    print(f"  Total de rodadas: {rodada}")

def menu():#menu
    print("\n" + "="*50)
    print("    SUPER TRUNFO - SISTEMA SOLAR  ")
    print("="*50)
    print("\n  [1] Single Player (vs Computador)")
    print("  [2] Dual Player (vs Outro Jogador)")
    print("  [0] Sair")

    while True:
        try:
            op = int(input("\n  Escolha uma opção: "))
            if op in [0, 1, 2, 3]:
                return op
            else:
                print("   Opção inválida.")
        except ValueError:
            print("   Digite apenas um número.")


if __name__ == "__main__":#chama a funçao inicial
    while True:
        opcao = menu()

        if opcao == 1:
            jogar_single_player()
        elif opcao == 2:
            jogar_dual_player()
        elif opcao == 0:
            print("\n  Até mais! \n")
            break
