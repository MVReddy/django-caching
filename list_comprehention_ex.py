l = range(1, 21)

# Get square of each number in a list
l2 = [x*x for x in l]

# Get all even numbers in the list
l3 = [x for x in l if x%2 == 0]

# Get all numbers divisible by 2 & 3
l4 = [x for x in l if x%2 == 0 and x%3 == 0]

# Nested list comprehension
# Get square of all ever numbers in a list
l5 = [x*x for x in [x for x in l if x%2 == 0] ]

print(l)
print(l2)
print(l3)
print(l4)
print(l5)
