# highest and lowest

# ---
# ## CodeWars Description
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# highAndLow("1 2 3 4 5"); // return "5 1"
# highAndLow("1 2 -3 4 5"); // return "5 -3"
# highAndLow("1 9 3 4 -5"); // return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# ---
# ## Solution

def high_and_low(numbers):
    # Split the string of numbers by space and convert each part to an integer.
    x = [int(i) for i in numbers.split()]
    # Find the maximum and minimum numbers from the list.
    # Format them into a string with the highest number first, separated by a space.
    return f'{str(max(x))} {str(min(x))}'
