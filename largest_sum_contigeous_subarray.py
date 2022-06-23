# Largest Sum Contiguous Subarray
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# 4 -1 -2 1 5 this subarray gives max sum
# Maximum contiguous sum is 7

# kadane's algorithm
# Initialize:
#     max_current = a[0]
#     max_global = a[0]

# Loop for each element of the array
#   max_current = max(max_current,a[i] + max_current)
#   if (max_current > max_global)
#             max_global = max_current
# return max_global


a = [-2, -3, 4, -1, -2, 1, 5, -3]
max_current = a[0]
max_global = a[0]

for i in range(1, len(a)):
    max_current = max(a[i], a[i] + max_current)
    if (max_current > max_global):
        max_global = max_current
print(max_global)
