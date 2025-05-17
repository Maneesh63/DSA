def is_prime(num):
    if num in [0, 1]:
        return False

    elif num >= 2:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print(f"{num} Number is not prime")
                return False

    return True

print(is_prime(10))