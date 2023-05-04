 # lets call one exaple as Girafe language 
 # vowels --> g     # it means lets convert any vowels in a word to g
 
# ------------------
# dog --> dgg      # example 
# cat --> cgt     # example

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
# print(translate(input("enter a phrase : ")))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("enter a phrase : ")))