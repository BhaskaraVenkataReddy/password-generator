import random
length=int(input("Enter length of Password: "))
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z'] 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~','*', '(', ')']
 
# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
# combine the character randomly selected above at this stage, the password contains only 4 characters but we want a 12-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
# we fill the rest of the password length by selecting randomly from the combined list of character above.
if length>=12:
    for x in range(length - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
    password = ""
    for x in temp_pass:
        password = password + x
    print(password)
else:
    print("Min length taken for generating password is 12")