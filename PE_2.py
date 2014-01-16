def fibonacci_sum(x, y, sum):
    n_sum = sum
    n_x = x
    n_y = y
    z = x+y
    if z % 2 == 0:
        n_sum += z
        print n_sum
    if x < 4000000:
        fibonacci_sum(y, z, n_sum)
        
fibonacci_sum(0, 1, 0)

