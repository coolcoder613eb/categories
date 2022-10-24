import time
from datetime import datetime as dt
from datetime import timedelta as dl
import sys
start_time = time.time()
t1 = dt.today()
t2 = dl(seconds=30)
t3 = t1 + t2
print(t3-t1)
while t3 > t1:
    print('\r',end='')
    sys.stdout.flush()
    print(str(t3-t1).split('.')[0],end='')
    t1 = dt.today()

print("--- %s seconds ---" % (time.time() - start_time))