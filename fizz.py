

def FizzBuzz():
    my_list = list(range(1, 101))
    for number in my_list:
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)


FizzBuzz()
