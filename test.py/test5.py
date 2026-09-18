#Integer
import random

random.randint(50, 100)

#booLean

temp = random.randint(50, 100)
print (temp)
if temp > 80: 
    print("It's hot outside")
if temp < 60:
    print("It's cold outside")
if temp > 60 and temp < 80:
    print("It's perfect outside")