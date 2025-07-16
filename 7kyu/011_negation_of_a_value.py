# negation of a value

# ---
# ## CodeWars Description
# In programming you know the use of the logical negation operator (!), it reverses the meaning of a condition.
# !false = true
# !!false = false
# Your task is to complete the function 'negationValue()' that takes a string of negations with a value and returns what the value would be if those negations were applied to it.
# negationValue("!", false); //=> true
# negationValue("!!!!!", true); //=> false
# negationValue("!!", []); //=> true
# Do not use the eval() function or the Function() constructor in JavaScript.
# Note: Always return a boolean value, even if there're no negations.

# ---
# ## Solution

def negation_value(s, val):
    # Check if the string 's' (representing negations) is not empty or not equivalent to 0.
    # In Python, an empty string "" is considered "falsy", but "" != 0 evaluates to True.
    # This condition ensures the loop runs only if there are negations to process.
    if s != 0:
        # Iterate through each character in the string 's'.
        # Each character represents a negation operation.
        for i in s:
            # Apply the logical NOT operator to the current value 'val'.
            # This flips the boolean value (True becomes False, False becomes True).
            val = not val
        # After applying all negations, return the final boolean value.
        return val
    else:
        # This 'else' block is reached if 's' is numerically 0.
        # Based on the problem description, 's' is expected to be a string of negations.
        # If 's' somehow evaluates to 0 (e.g., if it were an integer 0),
        # this would return False, which might not align with the "no negations" case
        # where the original 'val' should be returned.
        # However, assuming 's' is always a string, this branch would only be hit
        # if 's' was literally the string "0" and the problem implies 's' is only '!' characters.
        # Given the problem's context of 's' being negations, this specific 'else' case
        # for 's == 0' might not be typically encountered with valid inputs.
        return False
