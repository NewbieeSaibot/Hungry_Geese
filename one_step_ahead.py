from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration, Action, row_col
import numpy as np

# Info
all_moves = [Action.SOUTH.name, Action.EAST.name, Action.NORTH, Action.WEST.name]
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

last_move_tobias = []


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


def get_valid_moves():
    return all_moves.copy().remove(last_move_tobias)


def get_heuristic(board):
    pass


def change_board(move, board):
    pass


def decision_taker(obs, config):
    valid_moves = get_valid_moves()
    scores = []
    for move in valid_moves:
        scores.append(get_heuristic(change_board(move, obs.board)))

    best_move = valid_moves[np.argmax(scores)]
    return best_move


def agent(obs_dict, config_dict):
    # 1. Converte as entradas para objetos utilizáveis
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    # 2. Atualiza os dados
    atualize_data(observation, configuration)
    # 3.Toma decisão
    last_move_tobias = decision_taker(observation, configuration)
    return last_move_tobias
