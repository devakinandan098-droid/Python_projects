sub1=int(input("Enter your Grade for Subject 1 (0-100): "))
sub2=int(input("Enter your Grade for Subject 2 (0-100): "))
sub3=int(input("Enter your Grade for Subject 3 (0-100): "))

Total=sub1+sub2+sub3
percentage=Total*100/300

if(percentage>=80):
    Grade="A"
elif(percentage>70 and percentage<80):
    Grade="B"
elif(percentage>=60 and percentage<70):
    Grade="C"
elif(percentage<60):
    Grade="D"

print("The Percentage of the Student:",percentage)
print("The Student got a",Grade)
