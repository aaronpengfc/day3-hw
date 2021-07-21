import random

r = input("number?")
r = int(r)
print(r)
x = random.randint(1,10)
print(x)
while r != x:
    r = input("number?")
    r = int(r)
    print(r)
    x = random.randint(1,10)
    print(x)
if r == x:
    print("right")
    
            
    