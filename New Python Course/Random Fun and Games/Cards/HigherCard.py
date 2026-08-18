import random as r
faces=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
my_face=r.choice(faces)
your_face=r.choice(faces)
print("My card is",my_face,". Your card is",your_face)
if faces.index(my_face)>faces.index(your_face):
    print("I win")
elif faces.index(my_face)<faces.index(your_face):
    print("You win")
else:
    print("Tie!")