# RICKY NANEY ASSIGNMENT 6
#
###### DUE OCTOBER 16TH
import string
def decode():
    print() 
    code = input('Enter (brief) text to decrypt: ')
    num = int(input('Enter the number to shift the letters by: '))
    code = code.upper()
    value = 0
    new_value = 0
    correct_num = 0
    new_code = ''
    for i in range(len(code)):
        if code[i] not in string.ascii_uppercase:
            new_code = new_code + ' '
            continue
        value = ord(code[i])
        new_value = value - num
        if new_value < 65:
            correct_num = 65 - new_value
            new_value = 91 - correct_num
            new_code = new_code + chr(new_value)
        else:
            new_code = new_code + chr(new_value)
    print('Decrypted:', new_code)
    print()

def encode():
    print()
    code = input('Enter (brief) text to encrypt: ')
    num = int(input('Enter the number to shift the letters by: '))
    code = code.upper()
    value = 0
    new_value = 0
    correct_num = 0
    new_code = ''
    for i in range(len(code)):
        if code[i] not in string.ascii_uppercase: 
            new_code = new_code + ' '
            continue
        value = ord(code[i]) 
        new_value = value + num
        if new_value > 90:
            correct_num = new_value - 90
            new_value = 64 + correct_num
            new_code = new_code + chr(new_value)
        else:
            new_code = new_code + chr(new_value)
    print('Encrypted:', new_code)
    print()
while True:
    print() 
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')
    play = input('Enter your selection ==> ')
    if play == 'Q' or play == 'q': 
        print('Have a great day')
        break
    elif play == '1': 
        encode()
    elif play == '2': 
        decode()
    print('You must enter 1, 2, or Q/q to continue. Please try again')
