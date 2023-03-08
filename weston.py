# Weston

# Encoder
# Take an 8-digit password in string format containing only integers
# Stores password into a new variable
# Each digit shifted up by 3 digits (for char in pass) loop

# Decoder
# Takes encoded password
# Returns original password
# Inverse function of encoder

def decode(string):
	decoded = ''
	for i in string:
		decoded+=str((int(i)+7)%10)
	return decoded

def main_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def option_prompt():
    opt = int(input("Please enter an option: "))
    return opt

def encode_password(pass_word):
    enc_pass = ''
    for digit in pass_word:
        if int(digit) <= 6:
            idx = int(digit) + 3
            enc_pass += str(idx)
        elif int(digit) == 7:
            idx = 0
            enc_pass += str(idx)
        elif int(digit) == 8:
            idx = 1
            enc_pass += str(idx)
        elif int(digit) == 9:
            idx = 2
            enc_pass += str(idx)
    return enc_pass


if __name__ == "__main__":

    enc_dec = True

    password = ''

    while enc_dec:
        main_menu()

        option = option_prompt()

        if option == 1:
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():

                password = encode_password(password)

                print("Your password has been encoded and stored!\n")

            elif not password.isdigit():
                while not password.isdigit():
                    print("Please enter digits only.\n")
                    password = input("Please enter an option: ")
                    if password.isdigit():
                        password = encode_password(password)
                        print("Your password has been encoded and stored!\n")

            elif len(str(password)) != 8:
                while len(str(password)) != 8:
                    print("Please enter an 8 digit passcode.\n")
                    password = input("Please enter an option: ")
                    if len(str(password)) == 8:
                        password = encode_password(password)
                        print("Your password has been encoded and stored!\n")

        elif option == 2:
            decoded_pass = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded_pass}.\n")

        elif option == 3:
            enc_dec = False
        else:
            print("Please select options 1, 2, or 3 only.\n")
