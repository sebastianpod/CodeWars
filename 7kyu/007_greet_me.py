# Greet me

# ---
# ## CodeWars Description
# Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.
# Example:
# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

# ---
# ## Solution

def greet(name): 
    # The .title() method capitalizes the first letter of each word in the string
    # and converts the rest of the letters to lowercase.
    # This ensures that names like "riley" become "Riley" and "JACK" become "Jack".
    # The f-string then formats the greeting with "Hello " and an exclamation mark "!".
    return f'Hello {name.title()}!'
