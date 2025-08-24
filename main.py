# TODO: create a personalized invite letter for each person in a list, with a template called starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

"""
My methodology:
1. Draft a template of the letter (f string probably?).
2. go through invited_names.txt and add each name to a list
3. Take each name from the list, add it to the template, then create/write a .txt letter using that name.

Need to figure out:
How to read/distinguish names in the invited_names.txt (for ex how do I know where a line starts/stops, character, etc.?)
    then how to write each name to a letter

Solution:
Will use readlines() to return the names from invited_names.txt as a list https://www.w3schools.com/python/ref_file_readlines.asp
Will use strip() method removes any leading, and trailing whitespaces (spaces, tabs, newlines) https://www.w3schools.com/python/ref_string_strip.asp
Will use replace() to replace the [name] with a name from the list (no f string after all?) https://www.w3schools.com/python/ref_string_replace.asp


We will do this by:
opening the file
converting it into a string
replacing the contents with what we want
writing it back into a .txt file

"""


with open("Input/Names/invited_names.txt") as invited_names: # You’re not yet reading the file. You’re just creating a file object f that points to the file, which we are calling invited_names.
    names_list = invited_names.readlines() # we will fill this name bank with names from the invited_names.txt using the readlines() method
    cleaned_names_list = []
    for name in names_list:
        cleaned_name = name.strip()
        cleaned_names_list.append(cleaned_name)
    print(cleaned_names_list)
#
# Then we will open the starting letter (which is our template), and then convert it to a string so we can manipulate its data
with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read() # this turns our .txt file into a string, which allows us to use the replace method later
    for name in cleaned_names_list:
        personalized_letter = letter_contents.replace("[name]", name)# Now we can replace the letter
        letters_list = []
        letters_list.append(personalized_letter)
       # print(personalized_letter)
        print(letters_list)
        #Now that we have our contents, let's create the actual txt files
        with open(f"Output/ReadyToSend/{name}.txt", "w") as new_letter:
            new_letter.write(personalized_letter)


"""
# Angela's solution:
# only major difference is that she stripped the names as she was creating the txt files. i did it way before before we even used .read()

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
"""