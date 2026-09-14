# 1.  Reverse a string
text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)


# 2. Palindrome
text = input("Enter a string: ")

reversed_text = text[::-1]

if text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome")


# 3. Largest and Second Largest Number
numbers = [10, 25, 7, 40, 18]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest and number != largest:
        second_largest = number

print("Largest number:", largest)
print("Second largest number:", second_largest)

# 4. Remove Duplicates
numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = list(dict.fromkeys(numbers))

print("After removing duplicates:", unique_numbers)

# 5. Find the Missing Number
numbers = [1, 2, 3, 5, 6]

n = 6

expected_sum = n * (n + 1) // 2

actual_sum = 0

for number in numbers:
    actual_sum = actual_sum + number

missing = expected_sum - actual_sum

print("Missing number:", missing)

# 6.Character Frequency
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print(frequency)


# Exercise 7 - First Non-Repeating Character

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

found = False

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        found = True
        break

if not found:
    print("No non-repeating character found.")

#  8. Merge Two Sorted Arrays

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):

    if list1[i] < list2[j]:
        merged.append(list1[i])
        i = i + 1

    else:
        merged.append(list2[j])
        j = j + 1


while i < len(list1):
    merged.append(list1[i])
    i = i + 1


while j < len(list2):
    merged.append(list2[j])
    j = j + 1


print("Merged list:", merged)

# 9. Common Elements in Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("Common elements:", common)

#  10 . Stack 
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

removed = stack.pop()

print("Popped element:", removed)
print("Stack after pop:", stack)

# 11. Queue
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

removed = queue.popleft()

print("Removed element:", removed)
print("Queue after removal:", queue)

# 12. Linear Search
numbers = [10, 25, 7, 40, 18]

target = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Number found at index:", i)
        found = True
        break

if not found:
    print("Number not found.")

# 13. — Sort Without Built-in Sorting
numbers = [5, 2, 8, 1, 3]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

#  14 - Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = int(input("Enter a number: "))

result = factorial(number)

print("Factorial:", result)

#  15 - Maximum Subarray Sum

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = numbers[0]
maximum_sum = numbers[0]

for number in numbers[1:]:
    current_sum = max(number, current_sum + number)
    maximum_sum = max(maximum_sum, current_sum)

print("Maximum subarray sum:", maximum_sum)