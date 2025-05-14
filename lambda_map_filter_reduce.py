from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Step 2: Square each even number
squared = list(map(lambda x: x**2, evens))
print("Squared even numbers:", squared)

# Step 3: Sum the squared numbers
total = reduce(lambda x, y: x + y, squared)
print("Sum of squares:", total)
