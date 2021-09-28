from random import randint


def game():
    print('Welcome to the game')
    number_of_players = int(input('Enter amount of players: \n'))
    dices = [4, 6, 8, 12, 20]
    player_dices = {}
    for i in range(number_of_players):
        player_dices.update({f'{i + 1}': [4, 6, 8, 12, 20]})
    print(player_dices)
    lost_counter = 0
    while True:
        input('Click ENTER to roll \n')
        for key, values in player_dices.items():
            count = 0
            counter = []
            for dice in values:
                roll = randint(1, dice)
                if len(values) > 0:
                    print(f'Player {key}: D{dice} result: ' + str(roll))
                    if roll == 1:
                        count += 1
                        counter.append(count)
            if count > 0:
                for i in counter:
                    values.remove(values[-1])
            elif len(values) == 0:
                print(f'Player {key} lost')
                lost_counter += 1
                print(f'lost counter {lost_counter}')
            elif int(lost_counter) == int(number_of_players) - 1:
                print(f'Player {key} won!')
                return 0




game()
