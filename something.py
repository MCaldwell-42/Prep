import sys

name = sys.stdin

def FizzBuzz(T, *args):
    i = 0
    while i < T + 1:
        for instances in args:
            instance = list(range(1, instances+1))
            for number in instance:
                if number % 3 == 0 and number % 5 == 0:
                    print('FizzBuzz')
                elif number % 3 == 0:
                    print('Fizz')
                elif number % 5 == 0:
                    print('Buzz')
                else:
                    print(number)
                i += 1

FizzBuzz(name)


t = int(input())
s = input()
    
def swapping_cases(t, s):
    i=0

    while i < t+1:
        for case in s:
            q=0
            while q < len(case):
                word = []
                if case[0].isupper():
                    case[0].islower()
                    word.append(case[0])
                for letter in case:
                    if letter.isupper():
                        word.append("_")
                        word.append(letter)
                    else:
                        word.append(letter)
                    q += 1
        i += 1
        print(word)
    
swapping_cases(t, s)