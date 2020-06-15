class Game:
    """
    Класс самой игры
    """

    def __init__(self):
        self.barrels = [_ for _ in range(1, 91)]
        self.players = list()

    def __iter__(self):
        return (player for player in self.players)
