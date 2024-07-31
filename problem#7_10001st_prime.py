#Problem #7: 10001st prime
#What is the 10001st prime number?

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    count = 0
    candidate = 2  # Starting with the first prime number
    while count < n:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1
    return -1  # This should never be reached

# Find the 10001st prime number
result = find_nth_prime(10001)
print("The 10001st prime number is:", result)
