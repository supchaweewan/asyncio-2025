# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes
from time import sleep, ctime, time


def cooking(index):
    print(f'{ctime()} Kitchen number {index}    : Has started')
    sleep(2)
    print(f'{ctime()} Kitchen number {index}    : Has finished')

if __name__ == "__main__":
    #Thread time
    print(f'{ctime()} Main  : Begin cooking')
    start_time = time()
    #Begin cooking for both
    for index in range(2):
        cooking(index)
    #Calculate time used
    duration = time() - start_time
    print(f'{ctime()} Main  : Finished cooking. Time spent is {duration:0.2f} seconds.')