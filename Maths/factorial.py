# factorials
# thought this would be fun Maths
# or not if you type in a number larger than 20!
# what is a factorial?
# product of all the integers less than or equal to n
# 5! = 5 x 4 x 3 x 2 x 1 = 120


num = int(input('Enter a number: '))

factorial = 1

if num < 0:
    print('Sorry, factorials do not exist for negative numbers')

elif num == 0:
    print('The factorial of 0! is 1')

else:
    for i in range(1, num+1):
        factorial = factorial*i
    print('The factorial of', num, 'is', factorial)
