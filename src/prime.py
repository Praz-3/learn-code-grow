def is_prime(n):
    flag = 0
    if (n == 1):
        print(n,"is not a prime number")
    else:
        for i in range(2,int(n/2)+1):
            if (n % i == 0):
                flag = 1
        if(flag == 1):
            print(n,"is not a prime number")
        else:
            print(n,"is a prime number")

num = int(input())
is_prime(num)
