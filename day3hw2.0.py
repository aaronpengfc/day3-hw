import random
a = 0
x = random.randint(1,20)
print(x)
while True:
    r = input("number?")
    r = int(r)
    print(r)
    
    
    
    a = a +1
    if a >= 5: 
        print("gameover") 
        break
    
    if r == x:
        print("correct")
        print("you played", (a) , "times")
        
        break
        
    elif r != x:
        if r < x :
            print("too small")
        elif r > x:
            print("too big")
            
    