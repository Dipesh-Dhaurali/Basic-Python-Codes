def check_prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1

    if count == 0:
        print("It is a prime number")
    else:
        print("It is not prime number")

# num = int(input("Enter any number : "))
check_prime(5)


