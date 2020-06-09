# detect english

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_and_space = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def load_dictionary():

    dictionary_file = open('dictionary.txt')

    english_WORDS = {}

    for word in dictionary_file.read().split('\n'):

        english_WORDS[word] = None

    dictionary_file.close()

    return english_WORDS


english_words = load_dictionary()


def get_english_count(message):

    message = message.lower()
    message = remove_non_letters(message)

    possible_words = message.split()

    if possible_words == []:
        return 0.0

    matches = 0

    for word in possible_words:

        if word in english_words:
            matches += 1

    return float(matches)/len(possible_words)


def remove_non_letters(message):

    letters_only = []

    for symbol in message:

        if symbol in letters_and_space:

            letters_only.append(symbol)

    return ''.join(letters_only)


def is_english(message, word_percentage=80, letter_percentage=85):

    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage

    return words_match and letters_match


print(is_english('The man from the moon travelled to the Earth.'))
print(is_english('Gyuif coaou haicuw tttt cvbx. Zoo yyyyyfg j aoscjowc.'))
