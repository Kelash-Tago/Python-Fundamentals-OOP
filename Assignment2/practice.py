word = "Prime"  
# Example 1 - Looping over a string  
for ch in word:  
    print(ch)  
# Example 2 - Check if char 'i' exists in word  
if 'i' in word:  
    print("letter exists")  
# # Example 3 - Count number of i's in the word  
word = "artificial intelligence"  
count = 0  
for ch in word:  
   if ch == 'i':  
      count += 1  
print(f"i occurs {count} times.")