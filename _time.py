import time

print(time.ctime(0))
print(time.time())

print(time.ctime(time.time()))
print(time.localtime())
local_time = time.strftime("%B %d %Y %H:%M:%S", time.localtime())
print(local_time)

time_string = "20 April, 2020"
time_obj = time.strptime(time_string, "%d %B, %Y")
print(time_obj)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_str = time.asctime(time_tuple)
time_mk = time.mktime(time_tuple)
print(time_str)
print(time_mk)