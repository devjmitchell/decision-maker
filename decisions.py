from random import randint

# Welcome messages
print ("\nUnsure what to do? Enter your choices and I'll help you decide what you should do.")
print ("Hint: Type DONE when you've entered all of your choices.")

# Start your_input blank, since it needs DONE to finish asking
your_input = ""

# Creates a blank list for decisions to be added
choices = []

def picker(n):
    random_choice = randint(1,n)
    print ("\nYou had %d things to choose from." % (n))
    print ("You should %s." % (choices[random_choice - 1]))

while your_input.upper() != "DONE":
    your_input = input("\nWhat is your choice #%d? " % (len(choices) + 1))
    if your_input.upper() != "DONE":
        print ("I've added \"%s\" to your choices." % (your_input))
        choices.append(your_input)
    else:
        picker(len(choices))
