from random import randint
from typing import List


class DicePlayer:
    no_of_hits: int = 0

    def __init__(self, name):
        self.name: str = name
        self.dices: List[int] = [4, 6, 8, 12, 20]

    def roll_dices(self) -> None:
        print(f'{self.name} rolls: ')
        for dice in self.dices:
            roll: int = randint(1, dice)
            if roll == 1:
                self.no_of_hits += 1
            print(f'D{dice} result: {roll}')

    def remove_dices(self) -> None:
        if self.no_of_hits > 0:
            self.dices = self.dices[:-self.no_of_hits]
        self.no_of_hits = 0

    def is_player_without_dices(self) -> bool:
        return len(self.dices) != 0


class DiceGame:
    def __init__(self):
        no_of_players: int = int(input('Enter amount of players: '))
        self.automatic_roll: bool = input('Automatic roll? (y/n): ') == 'y'
        self.players: List[DicePlayer] = [DicePlayer(f'Player {i + 1}') for i in range(no_of_players)]

    def roll(self) -> None:
        for player in self.players:
            if not self.automatic_roll:
                input('Click ENTER to roll \n')
            player.roll_dices()
            player.remove_dices()
            if player.is_player_without_dices():
                print(f'{player.name} lost')
                self.players.remove(player)

    def play(self) -> None:
        while len(self.players) > 1:
            self.roll()
        print(f'{self.players[0].name} won!')
        return


if __name__ == '__main__':
    game = DiceGame()
    game.play()
