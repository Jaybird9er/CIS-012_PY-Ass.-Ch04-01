def isVowel(userChar):
    if userChar == 'a' or userChar == 'A':
        return("True")
    elif userChar == 'e' or userChar == 'E':
        return("True")
    elif userChar == 'i' or userChar == 'I':
        return("True")
    elif userChar == 'o' or userChar == 'O':
        return("True")
    elif userChar == 'u' or userChar == 'U':
        return("True")
    else:
        return("False")

print("Enter a character between a and z (or A and Z): ")
userChar = input()

print("\n")
print(userChar, " is a vowel: ", isVowel(userChar))



