#transpose a total file

import time, os, sys
import TranspositionCipher as tc
import TranspositionDecrypt as td

def file_cipher():

    text = input('File name(must be a .txt file): ')

    if text[-4:] == '.txt':

        input_filename = text

    else:

        input_filename = text + '.txt'

    filename_list = input_filename.split('.')

    print()
    print(input_filename)
    print()
    correct = input('Is this the correct filename? [Y/n] ')
    print()

    if correct == ('n' or 'N'):

        sys.exit()

    key = input('Key: ')
    key = int(key)

    mode = input('encrypt or decrypt: ')

    if mode == 'encrypt':

        filename_list[0] = filename_list[0] + '.encrypted.txt'
        output_filename = filename_list[0]

    elif mode == 'decrypt':

        filename_list[0] = filename_list[0] + '.decrypted.txt'
        output_filename = filename_list[0]

    if not os.path.exists(input_filename):

        print()
        print('The file %s does not exist. Quitting...' % (input_filename))
        sys.exit()

    if os.path.exists(output_filename):

        print()
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (output_filename))
        response = input('> ')

        if not response.lower().startswith('c'):

            sys.exit()

    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()

    print()
    print('%sing...' % (mode.title()))

    start_time = time.time()

    if mode == 'encrypt':

        translated = tc.encrypt_message(key, content)

    elif mode == 'decrypt':

        translated = td.decrypt_message(key, content)

    total_time = round(time.time() - start_time, 2)

    print('%sion time: %s seconds' % (mode.title(), total_time))

    output_file_obj = open(output_filename, 'w')
    output_file_obj .write(translated)
    output_file_obj.close()

    print('Done %sing %s (%s characters).' % (mode, input_filename, len(content)))
    print()
    print('%sed file is %s' % (mode.title(), output_filename))


#file_cipher()