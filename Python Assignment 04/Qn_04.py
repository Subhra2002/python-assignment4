def vowel(x):
    if len(letter) != 1:
            print("You character length is more than 1 .. please enter 1 letter")
    elif x in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        return "True"
    else:
        return "False "

letter = input("Enter the letter: ")
print(vowel(letter))

