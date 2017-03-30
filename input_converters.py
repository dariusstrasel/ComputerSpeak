
import re
# ord(char): converts a character to its unicode equivalent
# chr(number): converts a unicode number to its character.

def convert_inputs(input_value, input_type, output_type):
    type_dictionary = {
        'OCT': 1,
        'BIN': 1,
        'DEC': 1,
        'ASCII': 1,
        'TEXT': 1
    }
    valid_inputs = []

def valid_input(input, type):
    type_dictionary = {
        'OCT': is_valid_octal(input),
        'BIN': is_valid_binary(input),
        'DEC': is_valid_dec(input),
        'ASCII': is_valid_ascii(input),
        'TEXT': 1
    }

def is_valid_octal(octal):
    # regex = r"^0[1-7][0-7]*$"
    pass


def is_valid_ascii(ascii):
    pass


def is_valid_hex(hex):
    pass


def is_valid_dec(dec):
    pass


def is_valid_binary(bin):
    pass


def convert_word_to_decimal(word):
    return convert_number_system('HEX', convert_word_to_ascii(word))


def convert_word_to_ascii(word):
    return [convert_char_to_ascii(str(character)) for character in word]


def convert_char_to_ascii(char):
    return ord(char)


def convert_number_system(output_type, *number):
    output_dictionary = {'DEC': 2, 'OCT': 8, 'HEX': 16}
    radix = output_dictionary[output_type]

    result = []
    for word in number[0]:
        binary = []
        product = word
        while product is not 0:
            digit = (product % radix)
            binary.append(str(digit))
            product = (product // radix)
        result.append(("".join(reversed(binary))))
    return " ".join(result)


print(convert_word_to_decimal("TEST"))