from random import randint


def start_game():
    print('Welcome to the game')
    while True:
        try:
            number_of_players = int(input('Enter amount of players: \n'))
            return player_dices_render(number_of_players)
        except ValueError:
            print('Please enter valid integer')


def player_dices_render(number_of_players):
    player_dices = {}
    for i in range(number_of_players):
        player_dices.update({f'{i + 1}': [4, 6, 8, 12, 20]})
    return players_roll(player_dices, number_of_players)


def players_roll(player_dices, number_of_players):
    input('Click ENTER to roll \n')
    for key, values in player_dices.items():
        count = 0
        counter = []
        for dice in values:
            roll = randint(1, dice)
            print(f'Player {key}: D{dice} result: ' + str(roll))
            if roll == 1:
                count += 1
                counter.append(count)
        if count > 0:
            for i in counter:
                values.remove(values[-1])
    return check_player_dices(player_dices, number_of_players)


def check_amount_of_players(player_dices):
    if int(len(player_dices)) <= 1:
        for key, values in player_dices.items():
            print(f'Player {key} won')
            return input('Click ENTER to exit \n')
    elif len(player_dices) > 1:
        return players_roll(player_dices, len(player_dices))


def check_player_dices(player_dices, number_of_players):
    for i in range(number_of_players):
        try:
            for key, values in player_dices.items():
                if len(values) == 0:
                    print(f'Player {key} lost')
                    del player_dices[key]
                    if len(player_dices) == 1:
                        return check_amount_of_players(player_dices)
        except RuntimeError:
            return check_player_dices(player_dices, number_of_players)
    return check_amount_of_players(player_dices)


start_game()
