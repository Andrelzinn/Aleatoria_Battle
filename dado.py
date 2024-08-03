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

