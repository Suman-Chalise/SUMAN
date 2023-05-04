
def translate (phrase):
    translation = ""
    for letters in phrase: 
        if letters in "aeiou":
            translation = translation + "K"
        else:
            translation = translation + letters
    return translation
print(translate(input("please enter a phrase\n")))
