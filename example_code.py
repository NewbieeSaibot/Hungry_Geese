from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
import numpy as np

# Info
n_players_alive = 4
alive_players = []
players_tam = []
players = []
current_board = np.zeros((11, 7))
iteration = -1
food_row = -1
food_column = -1
player_row = -1
player_column = -1


def atualize_data(observation, configuration):
    global alive_players, n_players_alive, players_tam, players, iteration, \
        food_row, food_column, player_row, player_column

    iteration += 1
    # 2.1. Players
    player_index = observation.index
    n_players_alive = len(observation.geese)
    players_tam = []
    alive_players = []
    players = []
    for player in observation.geese:
        playerxy = []
        for i in range(len(player)):
            row, col = row_col(player[i], configuration.columns)
            playerxy.append((row, col))

        players.append(playerxy)
        players_tam.append(len(player))
        if len(player) > 0:
            alive_players.append(1)
        else:
            alive_players.append(0)

    player_row, player_column = players[player_index][0][0], players[player_index][0][1]

    # 2.2. Comidas
    food = observation.food[0]
    food_row, food_column = row_col(food, configuration.columns)


def decision_taker():
    if food_row > player_row:
        return Action.SOUTH.name
    if food_row < player_row:
        return Action.NORTH.name
    if food_column > player_column:
        return Action.EAST.name
    return Action.WEST.name


def agent(obs_dict, config_dict):
    # 1. Converte as entradas para objetos utilizáveis
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    # 2. Atualiza os dados
    atualize_data(observation, configuration)
    # 3.Toma decisão
    return decision_taker()
