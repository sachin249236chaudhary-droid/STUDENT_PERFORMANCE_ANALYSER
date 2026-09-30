"""Algorithm toolkit (factorial, fibonacci, reverse, binary, swap)."""


def swap(a, b):
    return b, a


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    seq, a, b = [], 0, 1
    for _ in range(max(n, 0)):
        seq.append(a)
        a, b = b, a + b
    return seq


def reverse_string(text):
    return text[::-1]


def to_binary(num):
    if num < 0:
        raise ValueError("Only non-negative integers are supported.")
    if num == 0:
        return "0"
    bits = ""
    while num > 0:
        bits = str(num % 2) + bits
        num //= 2
    return bits


def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result
