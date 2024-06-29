import time

print(time.ctime(0)) # reference point (Computer thinks time began)

print(time.time()) # retrun current seconds since epoch or reference time

print(time.ctime(time.time())) # return current time

time_object = time.localtime() # local time
# time_object = time.gmtime() # global time

# print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) # local time
print(local_time)

time_string = "28 June, 2024"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_tuple = (2024, 6, 28, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # retrun time according to the given value
print(time_string)

# (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_tuple = (2024, 6, 28, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) # retrun second according to the given value from epoch
print(time_string)