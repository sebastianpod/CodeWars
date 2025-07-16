# dot calculator

# ---
# ## CodeWars Description
# You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.
# Here are the following valid operators :
# + Addition
# - Subtraction
# * Multiplication
# // Integer Division
# Your Work (Task)
# You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction, the first number will always be greater than or equal to the second number.
# Examples (Input => Output)
# * "..... + ..............." => "...................."
# * "..... - ..."             => ".."
# * "..... - ."               => "...."
# * "..... * ..."             => "..............."
# * "..... * .."              => ".........."
# * "..... // .."             => ".."
# * "..... // ."              => "....."
# * ". // .."                 => ""
# * ".. - .."                 => ""

# ---
# ## Solution

def calculator(txt):
    # Initialize an empty string to store the result (dots).
    output = ''
    
    # Split the input string into parts: first number (dots), operator, second number (dots).
    parts = txt.split()
    num1_len = len(parts[0]) # Length of the first dot string
    operator = parts[1]      # The operator (+, -, *, //)
    num2_len = len(parts[2]) # Length of the second dot string
    
    # Perform calculations based on the operator.
    if operator == '+':
        # For addition, the result length is the sum of the lengths of the two dot strings.
        result_len = num1_len + num2_len
    elif operator == '-':
        # For subtraction, the result length is the difference of the lengths.
        result_len = num1_len - num2_len
    elif operator == '*':
        # For multiplication, the result length is the product of the lengths.
        result_len = num1_len * num2_len
    else: # Operator is '//' for integer division
        # For integer division, the result length is the integer division of the lengths.
        result_len = num1_len // num2_len
    
    # Append dots to the output string based on the calculated result length.
    # If result_len is 0, the loop won't run, and output will remain an empty string.
    for _ in range(result_len):
        output += '.'
        
    # Return the final string of dots.
    return output
