# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1: int = 0
        self.wins2: int = 0
        self.rounds: int = rounds

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print('Word game:')
        for i in range(1, self.rounds+1):
            print(f'round {i}')
            answer1: str = input('player1: ')
            answer2: str = input('player2: ')

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print('player 1 won')
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print('player 2 won')
            else:
                pass # it's a tie

        print('game over, wins:')
        print(f'player 1: {self.wins1}')
        print(f'player 2: {self.wins2}')


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2

        return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def __count_vowels(self, player_word: str) -> int:
        vowels: str = 'aeiou'
        count: int = 0

        for letter in player_word:
            if letter in vowels:
                count += 1

        return count

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        player1: int = self.__count_vowels(player1_word)
        player2: int = self.__count_vowels(player2_word)

        if player1 > player2:
            return 1
        elif player2 > player1:
            return 2

        return 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str) -> int:
        choices: dict = {'rock' : 0, 'paper': 1, 'scissors': 2}

        if player1_word not in choices.keys() and player2_word not in choices.keys():
            return 0

        if player1_word not in choices.keys():
            return 2

        if player2_word not in choices.keys():
            return 1

        # Based on the difference we can find out who win or both choose the same choice
        difference = choices[player1_word] - choices[player2_word]

        if difference == 0:
            return 0

        if difference == 1 or difference == -2:
            return 1

        return 2


if __name__ == '__main__':
    p = RockPaperScissors(4)
    p.play()
