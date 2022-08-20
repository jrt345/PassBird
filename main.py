import random
import string

import click

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
nums = string.digits
symbols = "!@#$%^&*"


def get_selected_options(options):
    options_selection = []

    if not any(options):
        for i in range(4):
            options_selection.append(i + 1)

    for i in range(4):
        if options[i]:
            options_selection.append(i + 1)

    return options_selection


def create_password(length, options):
    password = ""

    try:
        if int(length) <= 0:
            return "Error: {} is less than one, try again".format(int(length))

        if int(length) > 255:
            return "Error: {} is greater than 255, try again".format(int(length))

        for i in range(int(length)):
            selection = random.choice(get_selected_options(options))

            if selection == 1:
                password = password + random.choice(list(uppercase))
            if selection == 2:
                password = password + random.choice(list(lowercase))
            if selection == 3:
                password = password + random.choice(list(nums))
            if selection == 4:
                password = password + random.choice(list(symbols))
    except ValueError:
        return "Error: '{}' is not a number, try again".format(length)

    return password


@click.command()
@click.option("--length", "-l", type=int, help="Length of password (1-255)")
@click.option("--count", "-c", type=int, default=1, show_default=True, help="Print number of passwords at once")
@click.option("--include_uppercase", "-uc", is_flag=True, help="Include uppercase letters")
@click.option("--include_lowercase", "-lc", is_flag=True, help="Include lowercase letters")
@click.option("--include_numbers", "-num", is_flag=True, help="Include numbers")
@click.option("--include_symbols", "-sym", is_flag=True, help="Include symbols letters")
def main(length, count, include_uppercase, include_lowercase, include_numbers, include_symbols):
    options = (include_uppercase, include_lowercase, include_numbers, include_symbols)

    for i in range(count):
        print(create_password(length, options))


if __name__ == '__main__':
    main()
