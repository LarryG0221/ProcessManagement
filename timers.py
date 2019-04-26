from time import sleep
from datetime import datetime,timedelta

def timers():
    time1= datetime.now()
    sleep(3)
    time2 = datetime.now()
    return time2-time1

#print(timers().total_seconds())

dt = datetime.now() # Get timezone naive now
dt = dt + timedelta(days=1)
seconds = dt.timestamp()
print(seconds, dt)