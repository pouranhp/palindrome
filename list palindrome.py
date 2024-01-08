def is_palindrome(number):
    number_str = str(number)
    reversed_number_str = number_str[::-1]

    if number_str == reversed_number_str:
        return True
    else:
        return False


user_number = 1331

if is_palindrome(user_number):
    print(f"{user_number} is palindrome")
else:
    print(f"{user_number} is not palindrome")
