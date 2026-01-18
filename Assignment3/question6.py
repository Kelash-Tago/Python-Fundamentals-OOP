# from a list Create a dictionary that maps each word to its length

words = ["apple", "banana", "kiwi", "cherry", "mango"]
fruits={}
for fruit in words:
    fruits[fruit]=len(fruit)

print(fruits)