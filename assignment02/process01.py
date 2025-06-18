# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time

def cooking(index):
    cooking_time = time()
    print(f"{ctime()} Kitchen number {index}    : Will cook with PID {os.getpid()}")
    sleep(2)
    duration = time() - cooking_time
    print(f"{ctime()} Kitchen number {index}    : Cooking done in {duration:0.2f} seconds.")

def kitchen(index):
    cooking(index)

if __name__ == "__main__":
    # Start main thread
    print(f"{ctime()} Main  : Starting cooking with PID {os.getpid()}")
    start_time = time()

    #multiple kitchens with chefs
    kitchens = list()
    for index in range(100):
        p = multiprocessing.Process(target=kitchen, args=(index, ))
        kitchens.append(p)
        # Start those processes
        p.start()

    for index, p in enumerate(kitchens):
        # Wait until they're done
        p.join()

    duration = time() - start_time
    print(f"{ctime()} Main  : Finished cooking in {duration:0.2f} seconds")