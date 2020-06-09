# transposition decryption algorithm

import math


def d_transpose():
    message = input('Message: ')

    key = input('Key: ')
    key = int(key)

    plain_text = decrypt_message(key, message)

    print(plain_text + '|')


def decrypt_message(key, message):
    num_of_columns = math.ceil(len(message) / key)

    num_of_rows = key

    num_of_shaded = (num_of_columns * num_of_rows) - len(message)

    plain_text = [''] * num_of_columns

    col = 0
    row = 0

    for symbol in message:

        plain_text[col] += symbol

        col += 1

        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded):
            col = 0
            row += 1

    return ''.join(plain_text)

# d_transpose()
