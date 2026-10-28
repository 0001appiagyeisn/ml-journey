def is_palindrome(text):
    text = text.lower().replace(" ","").replace(",","").replace("'","")
    return print(text[::-1] == text)

    

is_palindrome("Madam, I'm Adam")
is_palindrome("level") 
is_palindrome("python") 