a=int(input("Enter a Number: "))
i=1
s=0

while(i<=a):
    if(i%2 is not 0):
         print(i*i,end=",")
         s=s+i*i
    i=i+1
print("The sum of odd numbers till",a,"is:",s)
