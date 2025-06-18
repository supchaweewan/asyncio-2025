# Thread version of cooking 1 kitchen 1 chefs 1 dishes
import os
from time import time, ctime, sleep
import threading

def cooking(index):
    print(f'{ctime()} Kitchen Number {index}    : Will start cooking. PID of kitchen: {os.getpid()}')
    cooking_time = time()
    print(f'{ctime()} Kitchen Number {index}    : Has began cooking.')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen Number {index}    : Cooking finished in {duration:0.2f} seconds.')

if __name__ == "__main__":
# Begin threading
    print(f'{ctime()} Main  : Starting cooking')
    start_time = time()
    print(f"{ctime()} Main  : ID of main process: {os.getpid()}")

# Threading the cooking process
    chefs = list()
    for index in range(2):
        c = threading.Thread(target=cooking, args=(index,))
        chefs.append(c)
        c.start()

    for index, c in enumerate(chefs):
        c.join()

    duration = time() - start_time
    print(f"{ctime()} Main  : Finished cooking in {duration:0.2f} seconds!")