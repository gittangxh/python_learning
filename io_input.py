def reverse(text):
    return text[::-1]


def is_palindrome(text):
    newtext=''
    for ch in text:
        if ch.isalpha() and ch.isnumeric():
            newtext+=ch.lower()
    return newtext == reverse(newtext)


something = input('Enter text:')

if is_palindrome(something):
    print('yes, it is palindrome')
else:
    print('no, it is not a palindrome')
