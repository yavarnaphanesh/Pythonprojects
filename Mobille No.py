
#Number in a coded format 

number= input("Enter your number : ")
eno=len(number)
result=number[0:4]+'*'*(eno-7)+ number[-3:]
print(eno)
print( "Encoded format ",result)
