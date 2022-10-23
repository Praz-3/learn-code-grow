x = int(input("Enter a Number to check:"))  #Taking input from user to check whether given number is prime or not
if x < 1 :
    print("Invalid input")
else:
    count = 0
    for i in (2,x) :
        if x%i == 0:
            count=1
        else:
            count=0
    if count == 1:
       print("Not a Prime Number!")
    else:
       print("Prime NUmber")





