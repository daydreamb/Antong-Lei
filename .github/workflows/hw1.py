def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Example:
word = "test"
print("Number of vowels in", word, ":", count_vowels(word))

#
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())
#3
for num in range(0,20):
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num, "odd")

#4
def sum_of_integers(a, b):
    return a + b
numA = int(input("Number A: "))
numB = int(input("Number B: "))

print("Sum:", sum_of_integers(numA, numB))

