""" PROBLEM COMPLETED BY JEFF BAYES
Project Euler Problem #10 - Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million. """

### POST-ANSWER ANALYSIS ###
# In retrospect, is_prime could just return True/False and let the rest of the program deal with inserting the prime
# into arrays. Simplifying is_prime would probably give it MORE applicability, thus improving my ability to stay DRY.


# I would have reused is_prime from PE_7.py, but that was a less-than-great prime checker.
# Used way too much memory. Refactored it here.
def is_prime(primes, number):
    """ Arguments:
            primes: a list of all prime numbers lower than number
            number: a number we're checking to see if it's prime
        Does:
            Adds number to the list of primes if number is prime
        Returns:
            A list of all prime numbers lower than or equal to number
            """
    if number <= 1 or number % 2 == 0:
        return primes
    for num in range(2, int(number**.5)+1):
        if number % num == 0:
            return primes
    primes.append(number)
    return primes

primes = [2] # optimizing outside of the existing function. we know 2 is prime, and any even number above two CANNOT be prime, thus...
number = 1 # must be odd so we can add two each time. evens can't be prime!
while primes[-1] < 2000000:
    primes = is_prime(primes, number)
    number += 2
    
del primes[-1] # I wanted to keep is_prime in tact without changing it.
# I could have prevented it from adding anything >= 2 million, but in something small scale like this, simple DRY > optimization.
    
prime_sum = 0 
for num in primes: # sums up all the numbers in the list of primes
    prime_sum += num
    
print prime_sum
