import winsound
import time

a=int(input("timer of: "))
while a!=0:
    print(a)
    time.sleep(1)
    a=a-1
winsound.Beep(1000, 1000)