#Given two integers N and M, count the number of prime numbers between N and M (both inclusive)

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    sqr = int(number**0.5) + 1

    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True

def counting_primes(N,M):
    primes_count = 0
    for num in range(N,M):
        if(is_prime(num)):
            primes_count = primes_count + 1
    print primes_count    

#example: N = 2, M = 10, would output 4