# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = 0
        self.__latest_observation = ''

    def add_observation(self, observation: str):
        self.__latest_observation = observation
        self.__observations += 1

    def latest_observation(self):
        return self.__latest_observation

    def number_of_observations(self):
        return self.__observations

    def __str__(self):
        return '{}, {} observations'.format(self.__name, self.__observations)


if __name__ == '__main__':
    station = WeatherStation('Houston')
    station.add_observation('Rain 10mm')
    station.add_observation('Sunny')
    print(station.latest_observation())

    station.add_observation('Thunderstorm')
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
