import random as r
keep_going=True
while keep_going:
    dice=[0,0,0,0,0]
    for x in range(5):
        dice[x]=r.randint(1,6)
        print("You rolled:", dice)
        answer=input("Keep going?")
        keep_going=(answer=="")