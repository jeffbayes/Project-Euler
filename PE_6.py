""" PROBLEM COMPLETED BY JEFF BAYES
Project Euler Problem #6 - Sum square difference.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

def sum_square_difference():
    sum_of_squares = 0
    square_of_sum = 0
    
    for i in range (1, 101):
        j = i**2
        sum_of_squares += j
    print sum_of_squares # sort of debugging print statement. verifies this step.
    
    sum = 0
    for i in range (1, 101):
        sum += i
    square_of_sum = sum**2
    print square_of_sum # same deal - step verification

    print(square_of_sum - sum_of_squares)
    
sum_square_difference()
