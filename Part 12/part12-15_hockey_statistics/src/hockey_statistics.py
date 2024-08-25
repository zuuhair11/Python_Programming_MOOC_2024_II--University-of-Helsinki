# Write your solution here
import json

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: str) -> None:
        self.__name = name
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def nationality(self) -> str:
        return self.__nationality
    
    @property
    def assists(self) -> int:
        return self.__assists
    
    @property
    def goals(self) -> int:
        return self.__goals
    
    @property
    def penalties(self) -> int:
        return self.__penalties
    
    @property
    def team(self) -> str:
        return self.__team
    
    @property
    def games(self) -> str:
        return self.__games
    
    def __str__(self) -> str:
        total = self.goals + self.assists
        return f'{self.name:21}{self.team}{self.goals:4} + {self.assists:2} = {total:3}'


class League:
    def __init__(self) -> None:
        self.__players = {}

    @property
    def players(self) -> dict:
        return self.__players

    def search_for_player(self, name) -> Player:
        if name in self.players:
            return self.__players[name]

        return 'Never landed!'

    def teams(self) -> list:
        teams: set = set(map(lambda player: player.team, self.players.values()))
        return sorted(list(teams))

    def countries(self) -> list:
        countries: set = set([player.nationality for player in self.players.values()])
        return sorted(list(countries))


class FileHandler:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def load_file(self) -> dict:
        with open(self.__filename, mode='r') as file:
            data = json.load(file)

        return data


class Application:
    def __init__(self) -> None:
        self.__league = League()
        self.__filehandler = FileHandler(self.__get_filename())

        for player in self.__filehandler.load_file():
            name: str = player['name']
            nationality: str = player['nationality']
            assists: int = player['assists']
            goals: int = player['goals']
            penalties: int = player['penalties']
            team: str = player['team']
            games: int = player['games']

            self.__league.players[name] = Player(name, nationality, assists, goals, penalties, team, games)

        print(f'read the data of {len(self.__league.players)} players')
        print()


    def __get_filename(self) -> None:
        return input('file name: ')

    def help(self) -> None:
        print('commands:')
        print('0 quit: ')
        print('1 search for player: ')
        print('2 teams: ')
        print('3 countries: ')
        print('4 players in team: ')
        print('5 players from country: ')
        print('6 most points: ')
        print('7 most goals: ')

    def search_for_player(self) -> None:
        name = input('name: ')

        player: Player = self.__league.search_for_player(name)
        print(player)

    def teams(self) -> None:
        for team in self.__league.teams():
            print(team)

    def countries(self) -> None:
        for country in self.__league.countries():
            print(country)

    def players_in_team(self) -> None:
        pass

    def players_from_country(self) -> None:
        pass

    def most_points(self) -> None:
        pass

    def most_goals(self) -> None:
        pass

    def run(self) -> None:
        self.help()
        while True:
            print()
            command = input('command: ')

            if command == '0':
                break
            elif command == '1':
                self.search_for_player()
            elif command == '2':
                self.teams()
            elif command == '3':
                self.countries()
            elif command == '4':
                self.players_in_team()
            elif command == '5':
                self.players_from_country()
            elif command == '6':
                self.most_points()
            elif command == '7':
                self.most_goals()
            else:
                self.help()


application = Application()
application.run()
