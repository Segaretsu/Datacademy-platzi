def palindrome (word):
    word = word.replace(" ", "").lower()
    invertedWord = word[::-1]
    if word == invertedWord:
        return True
    else:
        return False


def main ():
    word = input("Enter one word: ")
    isPalindrome = palindrome(word)
    if isPalindrome == True:
        print("It is palindrome")
    else:
        print("It is not palindrome")


if __name__ == '__main__':
    main()

