word = input("Enter a word: ").replace(" ", "").replace("'", "").replace(",", "").lower()
reverse_word = word[::-1]
if word == reverse_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")