from jogo import Jogo
import time


class AleatoriaBattle:
    def __init__(self):
        self.aleatoria_battle = Jogo()

    def init(self):
        time.sleep(0.2)
        name_player1 = input("Digite o nome do jogador 1: ")
        name_player2 = input("Digite o nome do jogador 2: ")
        time.sleep(0.2)
        self.aleatoria_battle.nomear_jogadores(name_player1, name_player2)
        self.aleatoria_battle.iniciar_jogo()
        time.sleep(0.8)


init = AleatoriaBattle()
init.init()