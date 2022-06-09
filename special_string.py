# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.

# All characters except the middle one are the same, e.g. aadaa.

# A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

# input => mnonopoO
# strings formed =>   m
#                     n
#                     o
#                     n
#                     o
#                     p
#                     o
#                     O
#                     non
#                     ono
#                     opo
# output => 11

def check_special(str):
    if len(str) == 1:
        return True
    else:
        s = str[0]
        # if len(str) % 2 == 1:
        mid = len(str) // 2
        for i in range(len(str)):
            if str[i] != s:
                if len(str) % 2 == 1 and i != mid:
                    return False
                elif len(str) % 2 == 0:
                    return False
        else:
            return True
        # else:
        #     for i in range(len(str)):
        #         if str[i] != s:
        #             return False
        #     else:
        #         return True

def find_substrings(str):
    count = 0
    for i in range(len(str)):
        temp = ""
        for j in range(i,len(str)):
            temp += str[j]
            if(check_special(temp)):
                print(temp)
                count += 1
    return count

print(find_substrings('aaaa'))
# print(check_special('abc'))