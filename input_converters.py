import re


class Convert:
    """Converts arbitrary inputs to hex, dec, bin, ascii, and text."""
    def __init__(self, input_value, output_type):
        self.input_value = input_value
        self.output_type = output_type
        self.type_dictionary = ['OCT', 'BIN', 'DEC', 'ASCII', 'TEXT']


def convert_inputs(input_value, input_type, output_type):
    """"Returns the number conversion of a numeral input or an ASCII conversion if text."""
    if is_valid_input(input_value, input_type):
        print(">>>{}(input_value:'{}', input_type:'{}', output_type:'{}')".format("convert_inputs", input_value, input_type, output_type))
        if input_type in ['OCT', 'DEC', 'ASCII']:
            return convert_number_system(output_type, input_value)
        elif input_type == 'BIN':
            return convert_number_system(output_type, convert_bin_to_dec(input_value))
        elif input_type == 'TEXT':
            return convert_number_system(output_type, convert_word_to_ascii(input_value))


def is_valid_input(input_value, input_type):
    """Validate an input string according to its number type."""

    def __is_valid_octal(octal):
        """Returns True if input is a legal octal value."""
        # regex = r"^0[1-7][0-7]*$"
        return True

    def __is_valid_ascii(ascii):
        """Returns True if input is a legal ascii value."""
        return True

    def __is_valid_hex(hex):
        """Returns True if input is a legal hexidecimal value."""
        return True

    def __is_valid_dec(dec):
        """Returns True if input is a legal decimal value."""
        return True

    def __is_valid_binary(bin):
        """Returns True if input is a legal binary value."""
        return True

    is_valid = {
        'OCT': __is_valid_octal(input_value),
        'BIN': __is_valid_binary(input_value),
        'DEC': __is_valid_dec(input_value),
        'TEXT': __is_valid_ascii(input_value),
        'HEX': __is_valid_hex(input_value)
    }

    return is_valid[input_type]


def convert_bin_to_dec(binary):
    result = sum([2**int(index) for index, character in enumerate(reversed(binary)) if character == '1'])
    return result


def convert_word_to_ascii(word):
    """Takes a string word, as input, converts each character to ASCII and returns a list """
    return [convert_char_to_ascii(str(character)) for character in word]


def convert_char_to_ascii(char):
    return ord(char)


def convert_number_system(output_type, *inputs_to_convert):
    """Takes a list of inputs and returns their number type conversion."""
    output_dictionary = {'BIN': 2, 'OCT': 8, 'HEX': 16}
    if output_type == 'HEX':
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    radix = output_dictionary[output_type]

    result = []
    for word in inputs_to_convert[0]:
        binary = []
        product = word
        while product is not 0:
            digit = (product % radix)
            if output_type == 'HEX' and digit > 10:
                digit = hex_map[digit]
            binary.append(str(digit))
            product = (product // radix)
        result.append(("".join(reversed(binary))))

    return " ".join(result)

#print(convert_bin_to_dec('10011011'))
print(convert_inputs("Say hello to my little friend!", 'TEXT', 'BIN'))
