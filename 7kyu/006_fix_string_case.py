# Fix string case

# ---
# ## CodeWars Description
# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Equal == lowercase. Change all to lowercase.

# ---
# ## Solution

def solve(s):
    # Initialize counters for lowercase and uppercase letters.
    l = 0  # Counter for lowercase letters
    u = 0  # Counter for uppercase letters
    
    # Iterate through each character in the input string 's'.
    for i in s:
        # Check if the current character is an uppercase letter.
        if i.isupper():
            u += 1  # Increment uppercase counter
        # Check if the current character is a lowercase letter.
        elif i.islower():
            l += 1  # Increment lowercase counter
            
    # Compare the counts of lowercase and uppercase letters.
    # If the number of lowercase letters is greater than or equal to the number of uppercase letters,
    # convert the entire string to lowercase.
    if l >= u:
        return s.lower()
    # Otherwise (if uppercase letters are more numerous),
    # convert the entire string to uppercase.
    else:
        return s.upper()
