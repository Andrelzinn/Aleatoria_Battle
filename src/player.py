import random
from dado import Dado

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
