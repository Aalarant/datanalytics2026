# Let's create a list that display fifteen 1's. 1
numbers = [1]

for x in range(0, 14):
    numbers.append(numbers[x])
print(numbers)


# Let's create a list that display fifteen 7's using list comprehension. 2
numbers1 = [7 for x in range(0, 15)]
print(numbers1)

# Let's create a list that display the numbers from 100 to 149 using list comprehension. 3
numbers2 = [x for x in range(100, 151)]
print(numbers2)

# Let's create a list that displays even numbers between 0 and 100. 4
numbers3 = [x for x in range(0, 101) if x % 2 == 0]
print(numbers3)

# Let's create a list that displays years between 1950 and 2020 that are divisible by 4. 5
years = [x for x in range(1950, 2021) if x % 4 == 0]
print(years)

