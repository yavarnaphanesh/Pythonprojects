print("Weelcome to Python Pizza Deliveries")
size= input("What size of pizza do you want ? S,M,L : ")
veg_nonvg = input("Veg (V) or Non-Veg(N) : ")
add_pepper=input("Do you want pepper ? Y or N : ")
cheese= input("Do you want me to add cheese Y or N : ")
spicy= input("Do want to make to more spicy (Y) or Less spicy(N) :")

bill=0

if size=="S":
    bill+= 100
elif size == "M":
    bill+= 200
elif size== "L":
    bill+=300
else:
    print("Your selection is wrong and choose correct one")

if veg_nonvg == "V":
    bill+=150
elif veg_nonvg == "N":
    bill+=200
else:
    print("Your selection is wrong and choose correct one")


if add_pepper=="Y":
    bill+=50
    
if cheese=="Y":
    bill+=100

if spicy=="Y":
    bill+=100


    
print("Your total bill is ", bill)
