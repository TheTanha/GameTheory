import numpy as np
import nashpy as nash


def compute_nash_equilibrium(matrix):
    game = nash.Game(matrix)
    equilibria = game.lemke_howson_enumeration()

    nash_equilibria = []
    for eq in equilibria:
        eq_tuple = (tuple(eq[0]), tuple(eq[1]))
        if eq_tuple not in nash_equilibria:
            nash_equilibria.append(eq_tuple)

    return nash_equilibria


def compute_game_value(matrix):
    game = nash.Game(matrix)
    equilibria = game.lemke_howson_enumeration()

    values = []
    for eq in equilibria:
        value = np.dot(eq[0], np.dot(matrix, eq[1]))
        values.append(value)

    game_value = max(values)

    return game_value


# Example usage
matrix = np.array([

    [100, -50],
    [0, 100]


])

nash_equilibria = compute_nash_equilibrium(matrix)
game_value = compute_game_value(matrix)

# Output Nash equilibria
print("Nash Equilibria:")
for eq in nash_equilibria:
    player1_strategy, player2_strategy = eq
    print("Player 1 Strategies:")
    for i, strategy in enumerate(player1_strategy):
        print(f"Row {i + 1} Strategy: {strategy:.2f}")

    print("Player 2 Strategies:")
    for i, strategy in enumerate(player2_strategy):
        print(f"Column {i + 1} Strategy: {strategy:.2f}")

    print()

# Output game value
print(f"The value of the game is: {game_value:.2f}")
