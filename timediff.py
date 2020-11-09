# Calculate the difference between two listed times in seconds
from datetime import datetime

def timeDiff(t1, t2):
    time1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return int(abs(time1 - time2).total_seconds())

tests = [[["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"], 25200],
         [["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"], 88200]]
for test in tests:
    f = timeDiff
    print(test[1], f(*test[0]))