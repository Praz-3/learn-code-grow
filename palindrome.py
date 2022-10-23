"""
This Program will check that given number is Palindrome or Not.

*Palindrome:A number is Palindrome when it reads same from start and end.

"""
input_num = int(input("Enter a number to check :"))
temp = input_num                                  #Storing the value of entered number to evaluate later
reverse = 0
while(temp > 0):
    dig = temp % 10                               #Storing the units place value of given number to first place
    reverse = reverse * 10 + dig
    temp = temp // 10
if input_num == reverse:                          #Checking whether the reversed number is equal to reversed number or not
    print("This is a Palindrome Number!")
else:
    print("This is Not a Palindrome Number!")