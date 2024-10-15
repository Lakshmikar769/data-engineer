def palindrome(word):
    return word == word[::-1]
Given_word = input("Enter a word: ")
if palindrome(Given_word):
    print(f"{Given_word} is a palindrome.")
else:
    print(f"{Given_word} is not a palindrome.")