def numberOfSteps(self, num: int) -> int:
    steps = 0  # Initialize a variable to keep track of the steps.

    while num != 0:  # Continue the loop until num becomes 0.
        steps += 1  # Increment the step count by 1.

        # Check if the least significant bit (LSB) of num is 1 using bitwise AND.
        if num & 1:
            num -= 1  # If LSB is 1 (num is odd), subtract 1 from num.
        else:
            num >>= 1  # If LSB is 0 (num is even), right-shift num by 1 (divide by 2).

    return steps  # Return the total number of steps.

# Example usage:
result = numberOfSteps(None, 14)
print(result)  # This will output 6, as explained in previous responses.
