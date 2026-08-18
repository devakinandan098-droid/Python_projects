a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))

if(a>b and a>c):
    print(a,"is the greatest number")
elif(b>a and b>c):
    print(b,"is the greatest number")
elif(c>a and c>b):
    print(c,"is the greatest number")
elif(a==b and a>c):
    print(a,"is greater than",c)
elif(a==c and a>b):
    print(a,"is greater than",b)
elif(a==b and a<c):
    print(c,"is the greatest number")
elif(a==c and a>b):
    print(b,"is the greatest number")
elif(b==c and b>a):
    print(b,"is the greatest number")
elif(b==c and b<a):
    print(a,"is the greatest number")
else:
    print("All of the Numbers are Equal")
