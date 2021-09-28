from random import randint


def game():
    print('Welcome to the game')
    number_of_players = int(input('Enter amount of players: \n'))
    dices = [4, 6, 8, 12, 20]
    player_dices = {}
    for i in range(number_of_players):
        player_dices.update({f'dices{i}': [4, 6, 8, 12, 20]})
    print(player_dices)
    while True:
        for key, values in player_dices.items():
            
            input('Click ENTER to roll \n')
            count = 0
            counter = []
            for dice in dices:
                roll = randint(1, dice)
                print(f'D{dice} result: ' + str(roll))
                if roll == 1:
                    count += 1
                    counter.append(count)
            if count > 0:
                for i in counter:
                    dices.remove(dices[-1])
            if len(dices) == 0:
                print('\nGame ended')
                input('Click ENTER to close\n')
                break


game()
