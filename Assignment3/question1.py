# check stirng is palindorme or not
string=input("Enter string: ")
reversedStr=""
for i in range(len(string)-1,-1,-1):
    reversedStr+=string[i]
if(string == reversedStr):
    print("Palindrome")
else:
    print("not Palindrome")


#there is another short method
def isPalindrome(string):
    if(string==string[::-1]):
        print("Palindrome")
    else:
        print("Not Palindrome")


print("using function:",end=" ")
isPalindrome(string)