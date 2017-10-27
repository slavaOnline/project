import serial 
import time 

r = serial.Serial("com3", 9600)
f = open("sens-temp.txt", "w")

while True:
        t = float(r.readline())
        e = time.clock()
        l = round (e, 2)
        print(t)
        f = open("sens-temp.txt", "a")
        f.write(str(t))
        f.write("\n")
f.close()        