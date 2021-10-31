def xkcdpwgen():  
    import argparse
    import random
    parser = argparse.ArgumentParser(
        description=
        'Generate a secure, memorable password using the XKCD method')
    parser.add_argument('-w',
                        '--words',
                        help='include WORDS words in the password (default=4)',
                        type=int,
                        default=4)
    parser.add_argument(
        '-c',
        '--caps',
        help='capitalize the first letter of CAPS random words (default=0)',
        type=int,
        default=0)
    parser.add_argument(
        '-n',
        '--numbers',
        help='insert NUMBERS random numbers in the password (default=0)',
        type=int,
        default=0)
    parser.add_argument(
        '-s',
        '--symbols',
        help='insert SYMBOLS random symbols in the password (default=0)',
        type=int,
        default=0)
    args = parser.parse_args()
    words = args.words
    caps = args.caps
    numbers = args.numbers
    symbols = args.symbols
    password = ""
    with open('words.txt', 'r') as f:
        word_list = f.read().splitlines()
    for i in range(words):
        password += random.choice(word_list)
        if i < words - 1:
            password += " "
    for i in range(caps):
        password = random.choice(password.split())
        password = password[0].upper() + password[1:]
    for i in range(numbers):
        password += str(random.randint(0, 9))
    for i in range(symbols):
        password += random.choice(list('~!@#$%^&*.:;'))
    print(password)
    return
