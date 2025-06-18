# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources
import multiprocessing
import os
from time import sleep, ctime, time

# Basket of eggs they're sharing
class Basket:
    def __init__(self):
        self.eggs = 50
    def use_eggs(self, index):
        print(f"{ctime()} Kitchen number {index}    : Chef {index} has locked with {self.eggs} eggs remaining")
        self.eggs -= 1
        print(f"{ctime()} Kitchen number {index}    : Chef {index} has released lock with {self.eggs} eggs remaining")

# Cooking for the chefs
def cooking(index, basket):
    #They'll use those eggs from the basket
    basket.use_eggs(index)
    sleep(2)

#Kitchen cooking
def kitchen(index, share_eggs):
    print(f"{ctime()} Kitchen number {index}    : Begin cooking with PID {os.getpid()}")
    cooking_time = time()
    cooking(index, share_eggs)
    duration = time() - cooking_time
    print(f"{ctime()} Kitchen number {index}    : Cooking done in {duration:0.2f} seconds")


if __name__ == "__main__":
    # Begin threads
    print(f"{ctime()} Main  : Start cooking with PID {os.getpid()}")
    start_time = time()

    basket = Basket()

    # multiple processes

    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        # start em up!
        p.start()

    for index, p in enumerate(kitchens):
        # wait until those processes are done
        p.join()

    print(f"{ctime()} Main  : Eggs remaining in basket: {basket.eggs}")
    duration = time() - start_time
    print(f"{ctime()} Main  : Finished cooking in {duration:0.2f} seconds")