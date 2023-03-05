def prime_num_check(n):
    count =0 
    for i in range(2,n):
        if n%i == 0:
            count+=1
    if count >1:
        print ("Not a Prime Number")
    else:
        print("It is a prime number")




n = int(input())

prime_num_check(n)
