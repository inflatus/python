numbers = [12, 37, 25, 46, 2, 75, 1, 29]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)
