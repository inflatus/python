'''taking an input and applying the 3n+1 conjecture to it'''
'''one of my favorite number theory problems'''

def main():
    '''main function'''
    n = int(input("Enter a number: "))
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
