import argparse


def add_number(num_buf: str, num_list: list):

    if num_buf == '':
        # sign after sign, like '2++2'
        # or sign at the beginning, like '+2+3'
        raise ValueError('Operation sign must be after the number')

    num_list.append(int(num_buf))


def __calculate(numbers: list, signs: list):
    if not all(isinstance(i, int) for i in numbers):
        raise ValueError('Numbers list should contain only numbers')

    if not all(isinstance(i, bool) for i in signs):
        raise ValueError('Signs list should contain only bools')

    result = numbers[0]
    for i in range(0, len(signs)):
        if signs[i]:  # if it's equal to '+'
            result += numbers[i + 1]
        else:
            result -= numbers[i + 1]

    return result


def ebnf(input_string: str):
    if not isinstance(input_string, str):
        raise TypeError('Input value should be str')

    numbers = []
    signs = []

    number_buf = ''
    for char in input_string:
        if char.isdigit():
            number_buf += char
        elif char in ('+', '-'):
            add_number(number_buf, numbers)
            number_buf = ''
            signs.append(char == '+')  # memory optimization, we store bool instead of str
        else:
            raise ValueError('Unsupported character')

    add_number(number_buf, numbers)

    if len(numbers) - len(signs) != 1:
        raise ValueError('Invalid format')

    return __calculate(numbers, signs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('expression', type=str)
    args = parser.parse_args()
    input_str = args.expression

    try:
        print("True, " + str(ebnf(input_str)))
    except ValueError:
        print("False, None")
