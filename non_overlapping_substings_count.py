# Given a string, break it into all possible combinations of non-overlapping substrings and return the count.
# input => ABCD
# substrings are =>   A,B,C,D
#                     A,B,CD
#                     A,BC,D
#                     A,BCD
#                     AB,C,D
#                     AB,CD
#                     ABC,D
#                     ABCD
# output => 8

s = input()
print(2**(len(s)-1))
