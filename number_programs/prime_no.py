#Program to check a number is prime number or not
n = int(input("Enter the no"))
if n <= 1:
    print("false")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Its not Prime")
            break
    else:
        print("Prime")




