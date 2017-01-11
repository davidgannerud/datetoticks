from datetime import datetime
offset = input('Time offset from now in minutes: ')
t0 = datetime(1, 1, 1)
now = datetime.now()
seconds = (now - t0).total_seconds() + (offset * 60)
ticks = seconds * 10**7
print(long(ticks))