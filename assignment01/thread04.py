# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

#custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')
        # store return value
        self.value = 99

# create the thread
thread = CustomThread()

thread.start()

print(f'{ctime()} Waiting for the thread to finish')
thread.join()

value = thread.value
print(f'{ctime()} Got: {value}')