import time
from datetime import timedelta

speed = 1000
judit_time = 5/speed
opponent_time = 55/speed
opponents = 24
move_pairs = 30

def game(board):
    calc_time = ((judit_time*speed) + (opponent_time*speed))*move_pairs
    total_time = 0
    start = time.perf_counter()
    for i in range(move_pairs):
    
        time.sleep(judit_time)
        print(F"Board {board+1} turn {i+1} - Judit makes a move with {int(judit_time*speed)} seconds.")
        time.sleep(opponent_time)
        print(f"Board {board+1} turn {i+1} - Opponent makes a move with {int(opponent_time*speed)} seconds.")
    print(f">>><>>><><<<><<< Board {board} - would have finished in {calc_time} seconds.")
    print(f">>><>>><><<<><<< Board {board} - finishes in {(time.perf_counter() - start)*speed} seconds.")
    total_time += (time.perf_counter() - start)*speed
    return total_time, calc_time
    
if __name__ == "__main__":
    total_time_used = 0
    total_time_calc = 0
    print(f"Number of games: {opponents} games.")
    print(f"Number of moves per game: {move_pairs} moves.")
    for i in range(opponents):
        time_spent, time_calced = game(i)
        total_time_used += time_spent
        total_time_calc += time_calced
    print(f"<><><><><><><> Chess exhibition finished for {opponents} students ")
    print(f"<><><><><><><> Chess exhibition calculated to finish in {timedelta(seconds=round(total_time_calc))} hours")
    print(f"<><><><><><><> Chess exhibition finished in {timedelta(seconds=round(total_time_used))} hours")


