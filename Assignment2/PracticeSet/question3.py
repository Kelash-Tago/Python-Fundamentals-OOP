#3. Count vowels in a word. [using   for loop  ] 

word="Artificial intelligence"
word=word.lower()
vowel=0
for ch in word:
    if(ch=='a' or ch == 'e' or ch=='i' or ch=='o' or ch=='u'):
        vowel+=1

print(f"vowels in word {word} are {vowel}")
