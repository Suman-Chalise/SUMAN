name = "Suman"
guess = ""
guess_limit = 4
guess_count = 0 
out_of_guess = False 

while guess != name and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("please enter  a guess : ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print ( " you have reached max limit ")
else:
    print("you win")
