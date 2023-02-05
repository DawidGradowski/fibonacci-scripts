def main():
    x = int(input("Set number of element from Fibonacci Sequence: "))
    print(fibonacci(x))


def fibonacci(x):
    if x <= 1:
        return x
    else:
        return (fibonacci(x - 1) + fibonacci(x - 2))


main()
