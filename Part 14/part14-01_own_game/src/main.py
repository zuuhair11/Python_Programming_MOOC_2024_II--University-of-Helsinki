import pygame
import pathlib
import sys
import random

pygame.init()


class Robot:
    def __init__(self):
        self.__robot = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/robot.png')
        self.__game_font = pygame.font.SysFont('Arial', 18)
        self.__score = 0
        self.move_center()
        self.__to_left = False
        self.__to_right = False


    @property
    def robot(self):
        return self.__robot
    
    @property
    def game_font(self):
        return self.__game_font
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def gain_point(self):
        self.__score += 1

    @property
    def robot_x(self):
        return self.__x

    @property
    def robot_y(self):
        return self.__y

    @property
    def to_left(self):
        return self.__to_left

    @property
    def to_right(self):
        return self.__to_right

    @to_left.setter
    def to_left(self, value):
        self.__to_left = value

    @to_right.setter
    def to_right(self, value):
        self.__to_right = value


    def move_left(self):
        if self.__x >= 0:
            self.__x -= 2

    def move_center(self):
        self.__x = (640 / 2) - (self.__robot.get_width() / 2)
        self.__y = 480 - self.__robot.get_height()

    def move_right(self):
        if self.__x <= 640 - self.__robot.get_width():
            self.__x += 2

    def jump_up(self):
        # I want to call this method any time the robot manage to catch a coin and as a reword:
        # I will increment the height of the robot so it can reach the top, to win the game
        pass

    def new_game(self):
        self.move_center()
        self.__score = 0


class Coin:
    def __init__(self):
        self.__coin = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/coin.png')
        self.__coins = []

        for _ in range(3):
            coin = self.generate_coins()
            self.__coins.append(coin)

    @property
    def coin(self):
        return self.__coin

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, new_coins):
        self.__coins = new_coins


    def generate_coins(self):
        self.__x = random.randint(0, 640 - self.__coin.get_width())
        self.__y = random.randint(-480, -self.__coin.get_height())

        return { 'x': self.__x, 'y': self.__y }

    def update_position(self, coin):
        coin['y'] += 1

    def hide_coin(self, coin):
        coin['y'] = 481

    def new_game(self):
        self.__coins = []


class Monster:
    def __init__(self):
        self.__monster = pygame.image.load(f'{pathlib.Path(__file__).parent.resolve()}/monster.png')
        self.__monsters = [self.generate_monsters()]


    @property
    def monster(self):
        return self.__monster

    @property
    def monsters(self):
        return self.__monsters

    @monsters.setter
    def monsters(self, new_monsters):
        self.__monsters = new_monsters


    def generate_monsters(self):
        self.__x = random.randint(0, 640 - self.__monster.get_width())
        self.__y = random.randint(-480, -self.__monster.get_height())

        return { 'x': self.__x, 'y': self.__y }

    def update_position(self, monster):
        monster['y'] += 3

    def hide_monster(self, monster):
        monster['y'] = 481

    def new_game(self):
        self.__monsters = []


class UI:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Golden Rain')

        self.robot = Robot()
        self.coin = Coin()
        self.monster = Monster()

        self.clock = pygame.time.Clock()

        self.lunch()


    def lunch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.robot.to_left = True
                    if event.key == pygame.K_RIGHT:
                        self.robot.to_right = True
                    if event.key == pygame.K_F2:
                        print('New Game')
                        self.robot.new_game()
                        self.coin.coins = []
                    if event.key == pygame.K_ESCAPE:
                        print('Escape the game')
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.robot.to_left = False
                    if event.key == pygame.K_RIGHT:
                        self.robot.to_right = False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.robot.to_left:
                self.robot.move_left()
            if self.robot.to_right:
                self.robot.move_right()

            self.screen.fill((72, 61, 139))
            self.screen.blit(self.robot.robot, (self.robot.robot_x, self.robot.robot_y))
            """ Generate coins and monsters """
            # Coins
            for coin in self.coin.coins:
                # Check if the robot manage to catch the coin. THEN:
                if coin['y'] + self.coin.coin.get_height() > 480 - self.robot.robot.get_height():
                    if coin['x'] + self.coin.coin.get_width() > self.robot.robot_x and coin['x'] < (self.robot.robot_x + self.robot.robot.get_width()):
                        # Hide the coin by giving it a height of > 480 so later I can get ride of it
                        self.coin.hide_coin(coin)
                        # Increment the score of the game
                        self.robot.gain_point()
                        # And let the robot jump a little bit up
                        self.robot.jump_up()

                if coin['y'] <= 480:
                    self.coin.update_position(coin)

                self.screen.blit(self.coin.coin, (coin['x'], coin['y']))

            # Monster
            for monster in self.monster.monsters:
                if monster['y'] + self.monster.monster.get_height() > 480 - self.robot.robot.get_height():
                    if monster['x'] + self.monster.monster.get_width() > self.robot.robot_x and monster['x'] < (self.robot.robot_x + self.robot.robot.get_width()):
                        # Lost the game
                        self.screen.fill((50, 50, 50))

                        score_text = self.robot.game_font.render(f'Score {str(self.robot.score)}', True, (255, 255, 255))
                        new_game_text = self.robot.game_font.render('Press F2 to start new game', True, (0, 255, 0))
                        or_text = self.robot.game_font.render('OR', True, (0, 0, 0))
                        exit_game_text = self.robot.game_font.render('Press ESC to exit the game', True, (255, 0, 0))

                        self.screen.blit(score_text, (300, 135))
                        self.screen.blit(new_game_text, (220, 170))
                        self.screen.blit(or_text, (310, 200))
                        self.screen.blit(exit_game_text, (220, 230))
                        pygame.display.flip()

                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_F2:
                                        """" I will work on this feature more later """
                                        self.robot.new_game()
                                        self.coin.new_game()
                                        self.monster.new_game()
                                        self.robot.to_left = False
                                        self.robot.to_right = False
                                        self.lunch()
                                    if event.key == pygame.K_ESCAPE:
                                        print('Escape the game')
                                        pygame.quit()
                                        sys.exit()

                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()

                if monster['y'] <= 480:
                    self.monster.update_position(monster)

                self.screen.blit(self.monster.monster, (monster['x'], monster['y']))

            score = self.robot.score
            score_text = self.robot.game_font.render('Score: ' + str(score), True, (255, 255, 255))
            new_game_text = self.robot.game_font.render('F2 = new game', True, (0, 255, 0))
            exit_game_text = self.robot.game_font.render('ESC = exit game', True, (255, 0, 0))

            self.screen.blit(score_text, (560, 10))
            self.screen.blit(new_game_text, (280, 10))
            self.screen.blit(exit_game_text, (0, 10))


            # Get ride of any coin or monster the robot miss to pick up
            self.coin.coins = [coin for coin in self.coin.coins if coin['y'] <= 480]
            self.monster.monsters = [monster for monster in self.monster.monsters if monster['y'] <= 480]

            if random.randint(1, 100) == 1:
                self.coin.coins.append(self.coin.generate_coins())

            if random.randint(1, 200) == 1:
                self.monster.monsters.append(self.monster.generate_monsters())

            pygame.display.flip()

            self.clock.tick(60)


if __name__ == '__main__':
    application = UI()
    application.lunch()
