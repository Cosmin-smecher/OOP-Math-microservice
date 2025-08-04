class MathService:
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return a

    def power(self, x, y):
        return x ** y
