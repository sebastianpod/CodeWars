# Cyclops numbers

# ---
# ## CodeWars Description
# A cyclops number is a number in binary that is made up of all 1's, with one 0 in the exact middle. That means all cyclops numbers must have an odd number of digits for there to be an exact middle.
# A couple examples:
# 101
# 11111111011111111
# You must take an input, n, that will be in decimal format (base 10), then return True if that number wil be a cyclops number when converted to binary, or False if it won't.
# Assume n will be a positive integer.
# A test cases with the process shown:
# cyclops (5)"""5 in biinary""""0b101""""because 101 is made up of all "1"s with a "0" in the middle, 101 is a cyclops number"""return Truecyclops(13)"""13 in binary""""0b1101""""because 1101 has an even number of bits, it cannot be a cyclops"""return Falsecyclops(17)"""17 in binary""""0b10001""""Because 10001 has more than 1 "0" it cannot be a cyclops number"""return False
# n will always be > 0.

# ---
# ## Solution

def cyclops(n):
    # Convert the decimal number n to its binary representation.
    # str(bin(n)) converts it to a string like "0b101".
    # [2:] slices the string to remove the "0b" prefix, leaving only the binary digits.
    binary_n = str(bin(n))[2:]
    
    # Check if the length of the binary string is even.
    # A cyclops number must have an odd number of digits to have an exact middle.
    if len(binary_n) % 2 == 0:
        # If the length is even, it cannot be a cyclops number.
        return False
    
    # Check if the binary string contains more than one '0'.
    # A cyclops number must have exactly one '0'.
    elif binary_n.count('0') > 1:
        # If there's more than one '0', it cannot be a cyclops number.
        return False
    
    # Calculate the middle index of the binary string.
    # For an odd length string, len(binary_n) // 2 will give the correct middle index.
    middle_index = len(binary_n) // 2
    
    # Check if the character at the exact middle index is '0'.
    # This is the final condition for a cyclops number: all 1's with one 0 in the middle.
    elif binary_n[middle_index] == '0':
        # If the middle digit is '0' and previous conditions passed, it's a cyclops number.
        return True
    
    # If none of the above conditions are met (e.g., middle digit is '1' but count of '0' is 1),
    # then it's not a cyclops number.
    else:
        return False
