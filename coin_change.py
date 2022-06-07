# A classic example of Greedy algorithm is the "Coin Change Problem".
# The cashier has to give some amount to the customer using the least number of coins. The cashier can use the same denomination any number of times.

# For example, the cashier has coins of denomination - 1, 2, 5 and 10.
# If the cashier has to give $15 to the customer, which will the cashier prefer?
# 15 x 1$ or 1x10$ and 1x5$?

# Greedy approach picks the largest denomination available, which will take one step closer to the desired goal of 15. In this case, it is 10. The next greedy choice will be 5.
# We can see that this approach will fail in some situations. For example, if the denominations are 1,3,5 and 6 and the cashier has to return $8 to the customer, then, as per greedy approach, the solution will be 6,1,1 even though the optimal solution would have been 5 and 3.

def coin_change(amount, coins):
    coins.sort(reverse = True)
    i = 0
    c = 0
    while(amount != 0):
        if(amount >= coins[i]):
            amount -= coins[i]
            c += 1
        else:
            i += 1
    return c

print(coin_change(15, [1, 2, 5, 10]))
print(coin_change(8, [1, 3, 5, 6]))