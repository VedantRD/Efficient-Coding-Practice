# ========================== normal approach ========================

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))

# =================== Memoization Top Down approach ============================


def fibonacciM(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n in memo.keys():
            return memo[n]
        memo[n] = fibonacciM(n-1, memo) + fibonacciM(n-2, memo)
        # print(memo)
        return memo[n]


memo = {0: 0, 1: 1}
# print(fibonacciM(35, memo))


# ============================== Tabulation bottom up approach =============================

def fibonacciT(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibs = [0, 1]
        for i in range(2, n+1):
            fibs.append(fibs[i-1]+fibs[i-2])
        return fibs[n]


print(fibonacciT(35))
