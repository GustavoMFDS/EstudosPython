

lista_npcs = []
player = {
    "nome": "heroi",
    "level": 1,
    "exp": 0,
    "expMax": 30,
    "dano": 10,
    "hp": 100,
    "hp_max": 100
}

def criar_npc(level):
    novo_npc = {
        "nome": f"Monstro {level}",
        "level": level,
        "dano": 5 * level,
        "hp": 50 * level,
        "hp_max": 50 * level,
        "exp": 7*level,
    }
    return novo_npc

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)

def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print(f"Nome: {npc['nome']}, Level: {npc['level']}, Dano: {npc['dano']}, HP: {npc['hp']}")

def exibir_player():
    print(f"Nome: {player['nome']}, Level: {player['level']}, Dano: {player['dano']}, HP: {player['hp']}/{player['hp_max']}, EXP: {player['exp']}/{player['expMax']}")

def reset_player():
    player["hp"] = player["hp_max"]

def reset_npc(npc):
    npc["hp"] = npc["hp_max"]

def level_up():
    if player["exp"] >= player["expMax"]:
        player["level"] += 1
        player["exp"] -= player["expMax"]
        player["expMax"] = player["expMax"] * 2
        player["hp_max"] += 20
        player["hp"] = player["hp_max"]
        player["dano"] += 5
        print(f"O {player['nome']} subiu para o level {player['level']}!")

def iniciar_batalha(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_batalha(npc)

    if player["hp"] > 0: 
        print(f"O {player['nome']} venceu e ganhou {npc['exp']} de experiencia!")
        player["exp"] += npc["exp"]
        exibir_player()
    else:
        print(f"O {npc['nome']} venceu!")
        exibir_npc(npc)
    level_up()
    reset_player()
    reset_npc(npc)

def atacar_npc(npc):
    npc["hp"] -= player["dano"]

def atacar_player(npc):
    player["hp"] -= npc["dano"]


def exibir_batalha(npc):
    print(f"Player Hp: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print("-----------------------------------\n")


gerar_npcs(5)

npc_selecionado = lista_npcs[0]

for npc in lista_npcs:
    reset_npc(npc)
    iniciar_batalha(npc)
iniciar_batalha(npc_selecionado)

