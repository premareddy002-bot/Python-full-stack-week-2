numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of squares using list comprehension
squares = [n ** 2 for n in numbers]

# Create a list of even numbers using lambda
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print("Squares:", squares)
print("Even Numbers:", even_numbers)