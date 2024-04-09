import random #for randomly selecting indices to generate the password
import os
import sys


#defining our constants
ALPHAS_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHAS_UPPER = [character.upper() for character in ALPHAS_LOWER]
NUMBERS = [str(i) for i in range(10)]
SYMBOLS = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', ',', '>', '.', '?', '/']


def generate_password(length, lowers, uppers, numbers, symbols):
    
    #first create the list of allowed characters to choose from
    allowed_characters = []
    if lowers:
        allowed_characters.extend(ALPHAS_LOWER)
    if uppers:
        allowed_characters.extend(ALPHAS_UPPER)
    if numbers:
        allowed_characters.extend(NUMBERS)
    if symbols:
        allowed_characters.extend(SYMBOLS)
    
    #now we create a list of random indices within this list
    password_indices = []
    for i in range(length):
        num = random.randint(0, len(allowed_characters) - 1) #pick an index within the range of the list
        password_indices.append(num)

    #now we create a list of chosen characters for our password
    password_list = []
    for index in password_indices:
        character = allowed_characters[index]
        password_list.append(character)
    
    #finally, make it a string!
    password = "".join(password_list)
    return password


#we will ask the user their preferences for the password
def get_inputs():
    
    #first, we need the length!
    password_length = 0
    while password_length < 1:
        try:
            password_length = int(input("how many characters long do you want your password to be? Enter an integer no less than 1: \n"))
        except ValueError:
            print("that is not an integer! try again")
            password_length = 0
        
        if password_length < 1:
                print(f"{password_length} response not allowed! Enter a number >= 1")



    #we will start with checking if they want lowercase letters
    allowed_lowers = ''
    while allowed_lowers not in ['y', 'n']:
        allowed_lowers = input("Would you like to include lowercase letters (a-z) in the password? (y/n): \n")
        if allowed_lowers not in ["y", "n"]:
            print("response not allowed! Enter y or n")
    #once we have an acceptable response, convert it to a boolean input for our function.
    if allowed_lowers == 'y':
        allowed_lowers = True
    else:
        allowed_lowers = False
    
    #repeat for uppercase letters
    allowed_uppers = ''
    while allowed_uppers not in ['y', 'n']:
        allowed_uppers = input("Would you like to include uppercase letters (A-Z) in the password? (y/n): \n")
        if allowed_uppers not in ["y", "n"]:
            print("response not allowed! Enter y or n")
    #once we have an acceptable response, convert it to a boolean input for our function.
    if allowed_uppers == 'y':
        allowed_uppers = True
    else:
        allowed_uppers = False
    
    #repeat for numbers
    allowed_numbers = ''
    while allowed_numbers not in ['y', 'n']:
        allowed_numbers = input("Would you like to include numbers (0-9) in the password? (y/n): \n")
        if allowed_numbers not in ["y", "n"]:
            print("response not allowed! Enter y or n")
    #once we have an acceptable response, convert it to a boolean input for our function.
    if allowed_numbers == 'y':
        allowed_numbers = True
    else:
        allowed_numbers = False
    
    #repeat for symbols
    allowed_symbols = ''
    while allowed_symbols not in ['y', 'n']:
        allowed_symbols = input("Would you like to include symbols in the password? (y/n): \n")
        if allowed_symbols not in ["y", "n"]:
            print("response not allowed! Enter y or n")
    #once we have an acceptable response, convert it to a boolean input for our function.
    if allowed_symbols == 'y':
        allowed_symbols = True
    else:
        allowed_symbols = False
    

    #check if our results allow us to create a password
    checking_array = [password_length, allowed_lowers, allowed_uppers, allowed_numbers, allowed_symbols]
    if True not in checking_array:
        print("please choose at least one type of character to build your password from!")
        return get_inputs()
    
    #once done, return our results
    return password_length, allowed_lowers, allowed_uppers, allowed_numbers, allowed_symbols


def get_textfile_inputs():
    want_textfile = ''
    while want_textfile not in ['y', 'n']:
        want_textfile = input("Would you like to write this password to the text file for safekeeping? (y/n): \n")
        if want_textfile not in ["y", "n"]:
            print("response not allowed! Enter y or n")
    #once we have an acceptable response, convert it to a boolean input for our function.
    if want_textfile == 'y':
        want_textfile = True
    else:
        want_textfile = False

    #now we either terminate or continue to get the info needed to write to text file.

    if not want_textfile:
        username = ''
        sitename = ''
        return sitename, username, want_textfile
    else:
        sitename = input("Enter the name of the site this password is for: \n")
        username = input("Enter the username this password is associated with: \n")

        return sitename, username, want_textfile

def write_to_textfile(want_textfile, sitename, username, password):
    if want_textfile:
        with open('passwords.txt','a') as file:
            file.writelines([f'sitename: {sitename}\n' f'username: {username}\n', f'password: {password}\n', '\n'])
            print("written to passwords.txt successfully!")
    else:
        return


def main():
    print("Welcome to the password generator! You'll be prompted to answer a series of questions, after which a password will be created for you!\n")
    length, lowers, uppers, numbers, symbols = get_inputs()

    password = generate_password(length, lowers, uppers, numbers, symbols)

    print(f"your password is: {password}")

    sitename, username, want_textfile = get_textfile_inputs()

    write_to_textfile(want_textfile, sitename, username, password)


if __name__ == "__main__":
    main()