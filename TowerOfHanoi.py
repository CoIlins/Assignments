from functools import lru_cache

@lru_cache(maxsize=10)

def tower_of_hanoi(n, source, target, auxiliary):

        if n == 0:
            return []
        moves = tower_of_hanoi(n - 1, source, auxiliary, target)
        moves += [(source, target)]
        moves += tower_of_hanoi(n - 1, auxiliary, target, source)
        return moves


def count_moves(n):
    if n == 0:
        return 0
    return 2 * count_moves(n - 1) + 1



def  printMoves():
    n = int(input("Please enter the number of discs:"))

    if n<=6:
        moves = tower_of_hanoi(n, 'A', 'C', 'B')

        for move in moves:
            print(f"Move disk from {move[0]} to {move[1]}")
        return print(f"Total moves required: {len(moves)}")
    else:
        return print("The number of moves is:", count_moves(n))

printMoves()
