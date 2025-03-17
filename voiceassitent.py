def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = 10  # Number of Fibonacci numbers to generate
for number in fibonacci_generator(n):
    print(number)
