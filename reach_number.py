# You will be given a number n which you have to reach with minimum number of steps by following below rules
# add 1 to number or double the number
# input  => 8
# output => 4
# input  => 6
# output => 4

def count_minimum_steps(n):
    count = 0

    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
        count += 1
    return count

n = 6
print(count_minimum_steps(n))