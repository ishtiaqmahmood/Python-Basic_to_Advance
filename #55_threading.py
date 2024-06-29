# thread = a flow of execution. Like a seperate order of instruction
# However each thread takes trun running to achieve concurrency
# GIL = (global interpreter lock)
# allows only one thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of it's tiime waiting for internal events (CPU intensive)
# use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
# use multithreading         


import threading
import time


# multithreading

def eat_breakfast():
    time.sleep(3)
    print("You eat the breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish study")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# sync with main thread

x.join() # main thread wait for x 
y.join() # main thread wait for y
z.join() # main thread wait for z 


print(threading.active_count())
print(threading.enumerate())
print(time.process_time())
print(time.perf_counter())