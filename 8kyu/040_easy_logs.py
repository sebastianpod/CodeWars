# easy logs

# ---
# ## CodeWars Description
# Given a logarithm base X and two values A and B, return a sum of logarithms with the base X: logXA + logXB.

# ---
# ## Solution

import math

def logs(x, a, b):
    return math.log(a,x) + math.log(b,x)
