# power

# ---
# ## CodeWars Description
# The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies number by itself power times).
# Examples
# numberToPower(3, 2)  // -> 9 ( = 3 * 3 )
# numberToPower(2, 3)  // -> 8 ( = 2 * 2 * 2 )
# numberToPower(10, 6) // -> 1000000
# Note: Math.pow and some other Math functions like eval() and ** are disabled.

# ---
# ## Solution

def number_to_pwr(number, p):
    # Initialize result with the base number.
    result = number
    # Handle edge case where power is 0 (any number to the power of 0 is 1).
    if p == 0:
        result = 1
    # Handle edge case where power is 1 (any number to the power of 1 is itself).
    elif p == 1:
        result = number
    # Handle edge case where number is 0 (0 to any positive power is 0).
    elif number == 0:
        result = 0
    # For other cases, multiply 'number' by itself 'p-1' times.
    else:     
        for i in range(p-1):
            result *= number
    # Return the calculated result.
    return result
