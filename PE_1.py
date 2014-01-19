""" PROBLEM COMPLETED BY JEFF BAYES
Project Euler Problem #1 - Multiples of 3 and 5.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000. """

def sum_of_multiples(below_number):
    summed = 0 # Summed is the sum of multiples.
    for num in range(below_number):
        if num % 3 == 0 or num % 5 == 0: # If evenly divisible by 3 or 5.
            summed += num
    return summed
        
print sum_of_multiples(1000)
