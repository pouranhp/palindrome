def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False


user_number = 47

if is_prime(user_number):
    print(f"{user_number} is prime")
else:
    print(f"{user_number} is not prime")
