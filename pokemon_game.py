import random
import requests
import time


def get_random_pokemon_stats() -> dict:
    """ Return dictionary with required stats. """

    pokemon_id = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)
    pokemon_all_stats = response.json()

    pokemon_needed_stats = {
        'name': pokemon_all_stats['name'],
        'id': pokemon_all_stats['id'],
        'height': pokemon_all_stats['height'],
        'weight': pokemon_all_stats['weight'],
        'base_experience': pokemon_all_stats['base_experience']
    }

    return pokemon_needed_stats


def winner_check() -> str:
    """Returns winner. """

    pokemon_player = get_random_pokemon_stats()
    pokemon_computer = get_random_pokemon_stats()
    print(f"Your pokemon's stats are: {pokemon_player}")

    stat = input("Which stat do you want to use? (id/height/weight/base_experience)")
    print(f"The {stat} of your opponent's pokemon is {pokemon_computer[stat]}")

    if pokemon_computer[stat] > pokemon_player[stat]:
        print("You lost!")
        return 'computer'
    elif pokemon_computer[stat] < pokemon_player[stat]:
        print("You won!")
        return 'player'
    else:
        print("It's a tie!")


def multiple_rounds():
    games_left = 3
    player_wins = 0
    computer_wins = 0
    while games_left > 0:
        print("New game!")
        winner = winner_check()
        if winner == 'computer':
            computer_wins = computer_wins + 1
        elif winner == 'player':
            player_wins = player_wins + 1

        games_left -= 1
        time.sleep(5)

    print(f'Computer - {computer_wins} vs Player - {player_wins}')


multiple_rounds()
