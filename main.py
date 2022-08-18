import random
import string

import click

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
nums = string.digits
symbols = "!@#$%^&*"


def create_password(length):
    password = ""

    try:
        if int(length) <= 0:
            return "Error: {} is less than one, try again".format(int(length))

        if int(length) > 255:
            return "Error: {} is greater than 255, try again".format(int(length))

        for i in range(int(length)):
            selection = random.randint(1, 4)

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
def main(length):
    print(create_password(length))


if __name__ == '__main__':
    main()
