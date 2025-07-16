# Keypad horror

# ---
# ## CodeWars Description
# Having two standards for a keypad layout is inconvenient!
# Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.
# Example:
# "789" -> "123"
# Notes:
# You get a string with numbers only

# ---
# ## Solution

def computer_to_phone(numbers):
    # Initialize an index variable (though not strictly necessary as it's reassigned).
    ind = 0
    # Initialize an empty string to build the phone number output.
    str_ = ''
    
    # Define the standard phone keypad layout as a tuple for quick lookup by index.
    phone_keypad = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    # Define the computer keypad layout as a tuple, matching the visual representation.
    # The order here is crucial as it dictates the mapping to the phone keypad.
    comp_keypad = ('7', '8', '9' ,'4', '5', '6', '1', '2', '3', '0')
    
    # Iterate through each character (digit) in the input 'numbers' string.
    for i in numbers:
        # Find the index of the current computer keypad digit 'i' within the 'comp_keypad' tuple.
        # This index will correspond to the position of the equivalent digit in the 'phone_keypad'.
        ind = comp_keypad.index(i)
        # Append the digit from the 'phone_keypad' at the found index to the result string.
        str_ += phone_keypad[ind]
        
    # Return the final converted string, which represents the number as if typed on a phone.
    return str_
