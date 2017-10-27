# Patrick Kunst
# CSC 241
# Assignment 3 Part C
import time

def cur_time():
    time_fmt = '%I:%M:%S %p %Z, %A, %B %d, %Y'
    return time.strftime(time_fmt, time.localtime())

now = cur_time()
print(now)
