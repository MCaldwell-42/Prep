# the fibonacci sequence is a series of numbers in which the next number is
# found by adding up the previous two numbers. fib = 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# write a function that takes number n and tells you what the number is in that sequence.


def fibonnaci(n):
    if n == 1:
        print('0')
    elif n == 2:
        print('1')
    elif n > 2:
        i = 0
        x = 0
        y = 1
        n -= 2
        while i < n:
            z = x + y
            x = y
            y = z
            i += 1
        print(z)


fibonnaci(5)