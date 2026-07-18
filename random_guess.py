import random
number = random.randint(1, 100)
count=0

for i in range(100):
    i=int(input("Enter a random guess:"))
    if i<number:
        print("Try higher!!")
        count+=1
    elif i>number:
        print("Try lower!!")
        count+=1
    else:
        print("Perfect guess")
        count+=1
        break
print("U took",count,"attempts!!")
print("CONGRATULATIONS!!")
