def main():
    x = int(input("Set number of element from Fibonacci Sequence: "))
    print(fibonacci(x))


def fibonacci(x):
    amount = 0
    a = 0
    b = 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        for i in range (x-1):
            amount = a + b
            a = b
            b = amount
        return amount


main()
