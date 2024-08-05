# Simple script to calculate 1 + 1 and print the result
import os

# Perform the calculation
a = 10
b = 1000
result = a + b

# Print the result
if result >= 1000:
    print("Success calculate a + b =", result)
    print(os.environ['ENV_VAR'])
    exit(0)
elif result <= 1000:
    print("Too tiny dude")
    print(os.environ['ENV_VAR'])
    exit(1)
