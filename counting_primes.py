#Given two integers N and M, count the number of prime numbers between N and M (both inclusive)

def is_prime(number):
    return number > 1 and all(number % i for i in xrange(2, number))

def counting_primes(N,M):
    primes_count = 0
    for num in range(N,M):
        if(is_prime(num)):
            primes_count = primes_count + 1
    print primes_count    

#example: N = 2, M = 10, would output 4