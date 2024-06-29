# daemon thread = a thread that runs in the background, not important for program to run
# Your program will not wait for deamon threads to complete before exiting
# Non-deamon threads cannot normailly be killed, stay alive until task is complete
# ex. background tasks, garbage collection, waiting for input, long running processes


import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for {} seconds".format(count))

x = threading.Thread(target=timer, args=(), daemon=True)
#x.setDaemon(True)
x.start()
#print(x.isDaemon())

answer = input("Do you want to exit? ")
