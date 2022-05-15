import random
print(" This is a password generator")

letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
spec_char="!@#$%^&*()_+-*/"

def split(letters):
    return [char for char in letters]
letters = split(letters)
def split(num):
    return [char for char in num]
num = split(num)
def split(spec_char):
    return [char for char in spec_char]
spec_char = split(spec_char)

ch_letter=(int (input("Enter the no of characters do you want           : ")))
nm_num=(int (input("Enter the no of numbers do you want                 : ")))
spc_letter=(int (input("Enter the no of special characters do you want  : ")))

password=""

for char in range(1,ch_letter+1):
    password += random.choice(letters)
for char in range(1,nm_num+1):
    password += random.choice(num)
for char in range(1,spc_letter+1):
    password += random.choice(spec_char)

print("your password is : ",password)

           


