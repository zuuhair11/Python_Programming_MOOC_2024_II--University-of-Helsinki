# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games


class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        games_before_1990 = []

        for game in super().list_games():
            if game.year < 1990:
                games_before_1990.append(game)

        return games_before_1990


if __name__ == '__main__':
    museum = GameMuseum()
    museum.add_game(ComputerGame('Pacman', 'Namco', 1980))
    museum.add_game(ComputerGame('GTA 2', 'Rockstar', 1999))
    museum.add_game(ComputerGame('Bubble Bobble', 'Taito', 1986))
    for game in museum.list_games():
        print(game.name)
