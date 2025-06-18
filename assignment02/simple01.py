# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time


def cooking(index):
    print(f'{ctime()} Kitchen number {index}    : Has started')
    sleep(2)
    print(f'{ctime()} Kitchen number {index}    : Has finished')

if __name__ == "__main__":
    #Thread time
    print(f'{ctime()} Main  : Begin cooking')
    start_time = time()
    #Begin cooking
    cooking(0)
    #Calculate time used
    duration = time() - start_time
    print(f'{ctime()} Main  : Finished cooking. Time spent is {duration:0.2f} seconds.')