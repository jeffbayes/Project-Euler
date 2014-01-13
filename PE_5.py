""" PROBLEM COMPLETED BY JEFF BAYES
Project Euler Problem #5 - Smallest multiple.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

def divisor_check(number, divisor):
    """ Checks if the number is evenly divisible by all numbers from 1 to 20. 
            Always initiate function with divisor as 1. """
    if number % divisor == 0:
        if divisor < 20:
            divisor_check(number, divisor+1)
        else:
            print number
            return True
    else:
        return False
            
#   This taught me a valuable lesson in memory use. I nearly crashed my computer trying to iterate
#   through that entire number list. Dumb dumb dumb dumb dumb. 
#
#   for i in range(100000000):
#       divisor_check(i, 1)

num = 0
while not divisor_check(num, 1):
    num += 20
    
# That was really quick and dirty, but I got the answer from this.
