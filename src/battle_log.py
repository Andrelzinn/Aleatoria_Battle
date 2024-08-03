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

