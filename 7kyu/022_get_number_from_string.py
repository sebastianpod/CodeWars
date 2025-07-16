# Get number from string

# ---
# ## CodeWars Description
# Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
# Function:
# getNumberFromString(s)

# ---
# ## Solution

def get_number_from_string(string):
    # Iterate through each character in the input string.
    # Keep only characters that are numeric (digits).
    # Join the filtered digits to form a new string of numbers.
    # Convert this new string of digits into an integer.
    return int(''.join(i for i in string if i.isnumeric()))
