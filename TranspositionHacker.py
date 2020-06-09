# brute force hack a transposition cipher

import DetectEnglish as de
import TranspositionDecrypt as td
import numpy as np


def t_hack():
    message = input('What needs to be hacked? > ')

    hacked_mesaage = hack_transposition(message)

    if hacked_mesaage == None:

        print('Failed to hack encryption.')

    else:

        print(hacked_mesaage)


def hack_transposition(message):
    print('Hacking...')

    print('(Ctrl-D to quit at any time.)')

    for key in range(1, len(message)):

        print('Trying key %s...' % key)

        decrypted_text = td.decrypt_message(key, message)

        if de.is_english(decrypted_text):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decrypted_text[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')

            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decrypted_text

    return None


t_hack()
