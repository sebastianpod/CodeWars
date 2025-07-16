# Number Of Occurrences

# ---
# ## CodeWars Description
# Write a function that returns the number of occurrences of an element in an array.
# This function will be defined as a property of Array with the help of the method Object.defineProperty, which allows to define a new method directly on the object (more info about that you can find on MDN).
# Examples
# var arr = [0, 1, 2, 2, 3];arr.numberOfOccurrences(0) === 1;arr.numberOfOccurrences(4) === 0;arr.numberOfOccurrences(2) === 2;arr.numberOfOccurrences(3) === 1;

# ---
# ## Solution

def number_of_occurrences(element, sample):
    # Use the built-in list.count() method to efficiently count occurrences of 'element' in 'sample'.
    return sample.count(element)
