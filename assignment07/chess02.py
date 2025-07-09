import time
from datetime import timedelta
import asyncio

speed = 100
judit_time = 5/speed
opponent_time = 55/speed
opponents = 24
move_pairs = 30

async def game(board):
    
    start = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(judit_time)
        print(f"Board {board+1} turn {i+1} - Judit made a move with {int(judit_time*speed)} seconds.")
        await asyncio.sleep(opponent_time)
        print(f"Board {board+1} turn {i+1} - Opponent made a turn with {int(opponent_time*speed)} seconds")
    print(f">>><>>><><<<><<< Board {board+1} - finishes in {(time.perf_counter() - start)*speed} seconds.")
    
    return {"calculated_board_time": (time.perf_counter()- start)*speed}


async def main():
    tasks = []

    for j in range(opponents):
        tasks += [game(j)]
    await asyncio.gather(*tasks)
    
    print(f"<><><><><><><> Chess exhibition finished in {timedelta(seconds=speed*round(time.perf_counter() - startingTime))} hours")


if __name__ == "__main__":
    print(f"Number of games: {opponents} games.")
    print(f"Number of moves per game: {move_pairs} moves.")
    startingTime = time.perf_counter()
    asyncio.run(main())
