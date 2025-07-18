# Regex count lowercase letters

# ---
# ## CodeWars Description
# Your task is simply to count the total number of lowercase letters in a string.
# Examples
# "abc" ===> 3
#
# "abcABC123" ===> 3
#
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
#
# "" ===> 0;
#
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
#
# "abcdefghijklmnopqrstuvwxyz" ===> 26

# ---
# ## Solution

def lowercase_count(strng):
    cnt = 0
    for char in strng:
        if char.islower():
            cnt += 1
    return cnt
