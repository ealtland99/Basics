for x in range(1, 21):
    if x%15==0:
        print('FizzBuzz')
    elif x%3==0: 
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    else:
        print(x)
