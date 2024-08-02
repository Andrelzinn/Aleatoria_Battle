import random
import time


class Dado:
    def __init__(self) -> None:
        self.__faces: int = 0
        self.__possiveis_faces: list[int] = [4, 8, 10, 12]

    @property
    def faces(self) -> int:
        return self.__faces

    @property
    def possiveis_faces(self) -> list:
        return self.__possiveis_faces

    @faces.setter
    def faces(self, numero_faces: int):
        if numero_faces in self.possiveis_faces:
            self.__faces = numero_faces
        else:
            print("Numero de faces Invalida")


class Player:
    def __init__(self) -> None:
        self.__player = None
        self.__dado = Dado()

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, nome: str) -> None:
        self.__player = nome

    def rolar_dado(self) -> int:
        self.__dado.faces = random.choice(self.__dado.possiveis_faces)
        return random.randint(1, self.__dado.faces)


class BattleLog:
    def __init__(self):
        self.log_rodadas = []
        self.__log_partida = None

    def adicionar_resultado(self, info):
        self.log_rodadas.append(info)


    def placar(self, player1: str, player2: str, points1: int, points2: int) -> str:
        return f"Placar: {player1} {points1} X {points2} {player2}"

    def log_resultado(self, player1: str, player2: str, player1_points: int, player2_points: int) -> list[str]:
        if player2_points > player1_points:
            return [f"{player2} Ganhou!", self.placar(player1, player2, player1_points, player2_points)]
        elif player1_points > player2_points:
            return [f"{player1} Ganhou!", self.placar(player1, player2, player1_points, player2_points)]
        elif player1_points == player2_points:
            return [f"{player1} e {player2} Empataram!",
                    self.placar(player1, player2, player1_points, player2_points)]

    def mostra_linha(self) -> None:
        print('______________________________________________________')


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
