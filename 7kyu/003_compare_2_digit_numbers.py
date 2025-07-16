# Compare 2 digit numbers

# ---
# ## CodeWars Description
# Compare 2 digit numbers
# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.
# Example:
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.

# ---
# ## Solution

def compare(a, b):
    # Extract digits of the first number and put them into a set to handle unique digits.
    # For example, 22 will become {2}.
    digits_a = {a // 10, a % 10}
    
    # Extract digits of the second number and put them into a set.
    digits_b = {b // 10, b % 10}
    
    # Find the common digits by taking the intersection of the two sets.
    # The intersection contains only the digits that are present in both numbers.
    common_digits = digits_a.intersection(digits_b)
    
    # The similarity percentage is calculated based on how many unique digits are common.
    # Since each number has at most 2 unique digits, the maximum possible common digits is 2.
    # (len(common_digits) / 2) gives the proportion of common digits.
    # Multiplying by 100 converts it to a percentage.
    percentage = (len(common_digits) / 2) * 100
    
    # Return the result formatted as a string with a percentage sign.
    return f"{int(percentage)}%"
