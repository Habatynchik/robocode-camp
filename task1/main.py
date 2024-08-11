import math
from collections import Counter


def get_fibonacci_up_to(n):
    fib_numbers = [0, 1]
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    return fib_numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

mean = sum(numbers) / len(numbers)
closest_number = min(numbers, key=lambda x: abs(x - mean))
closest_count = numbers.count(closest_number)
probability = closest_count / len(numbers)

print(f"The number closest to the mean: {closest_number}")
print(f"Probability of getting this number: {probability:.2f}")

max_number = max(numbers)
fib_numbers = get_fibonacci_up_to(max_number)
numbers = [num for num in numbers if num not in fib_numbers]

print("List after removing Fibonacci numbers:", numbers)

if numbers:
    min_number = min(numbers)
    numbers = [num for i, num in enumerate(numbers) if num % min_number != 0 or i == numbers.index(num)]

print("List after removing duplicates of numbers that are multiples of the smallest number:", numbers)
