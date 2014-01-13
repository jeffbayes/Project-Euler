""" PROBLEM COMPLETED BY JEFF BAYES
Project Euler Problem #7 - 10,001st Prime
By listing the first six prime numbers (2, 3, 5, 7, 11, 13), we can see that the 6th prime is 13.
What is the 10,001st prime number? """

def is_prime(primes, number):
    for element in primes:
        if number % element == 0:
            return primes
    primes.append(number)
    return primes
    
        
primes = [2,3,5,7,11,13]
number = 2
while len(primes) != 10001:            
    primes = is_prime(primes, number)
    number += 1
    
print primes[-1]    
 
""" Print statement used to verify first ten or so primes.
for element in primes:
    print element
"""
