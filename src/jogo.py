import random
import time
from player import Player
from battle_log import BattleLog

class Jogo:
    def __init__(self):
        self.player1: Player = Player()
        self.player2: Player = Player()
        self.player1_points: int = 0
        self.player2_points: int = 0
        self.jogadores_nomeados: bool = False
        self.battle_log: BattleLog = BattleLog()

    def nomear_jogadores(self, nome1: str, nome2: str) -> None:
        self.player1.player = nome1
        self.player2.player = nome2
        self.jogadores_nomeados = True

    def iniciar_jogo(self) -> None:

        if self.jogadores_nomeados:
            partidas = random.randint(3, 7)
            rodada_contador = 0

            while rodada_contador < partidas:
                rodada_contador += 1
                points1 = self.player1.rolar_dado()
                points2 = self.player2.rolar_dado()
                time.sleep(0.3)
                print(f"Rodada {rodada_contador}")
                resp = self.battle_log.log_resultado(self.player1.player, self.player2.player, points1, points2)
                if resp[0] == f"{self.player2.player} Ganhou!":
                    self.player2_points += 1
                    print(resp[0])
                    print(resp[1])
                elif resp[0] == f"{self.player1.player} Ganhou!":
                    self.player1_points += 1
                    print(resp[0])
                    print(resp[1])
                else:
                    self.battle_log.adicionar_resultado(f"{resp[0]} {resp[1]}")
                self.battle_log.mostra_linha()
            print()
            time.sleep(0.6)
            self.battle_log.mostra_linha()
            self.mostrar_ganhador()
        else:
            print("Nomeie Os Jogadores")

    def mostrar_ganhador(self):
        print("PLACAR FINAL:")
        resp = self.battle_log.log_resultado(self.player1.player, self.player2.player, self.player1_points,
                                             self.player2_points)
        print(resp[0])
        print(resp[1])
