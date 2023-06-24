import os
import random
import string

import click

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
nums = string.digits
symbols = "!@#$%^&*"


def generate_password(length, exclude_uppercase, exclude_lowercase, exclude_numbers, exclude_symbols):
    characters = ''
    if not exclude_uppercase:
        characters += string.ascii_uppercase
    if not exclude_lowercase:
        characters += string.ascii_lowercase
    if not exclude_numbers:
        characters += string.digits
    if not exclude_symbols:
        characters += symbols

    if not characters:
        raise ValueError("At least one character type must be enabled.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_unique_file_name(file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1
    unique_file_name = file_name
    while os.path.exists(unique_file_name):
        unique_file_name = f"{base_name}_{counter}{extension}"
        counter += 1
    return unique_file_name

def create_txt_file(file_name, passwords):
    with open(file_name, "w") as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"Successfully exported to '{file_name}'.")


@click.command()
@click.option("--length", "-l", type=click.IntRange(1, 255), help="Length of password")
@click.option("--count", "-c", type=click.IntRange(1), default=1, show_default=True, help="Print number of passwords at once")
@click.option("--exclude_uppercase", "-uc", is_flag=True, help="Exclude uppercase letters")
@click.option("--exclude_lowercase", "-lc", is_flag=True, help="Exclude lowercase letters")
@click.option("--exclude_numbers", "-num", is_flag=True, help="Exclude numbers")
@click.option("--exclude_symbols", "-sym", is_flag=True, help="Exclude symbols letters")
@click.option("--export", "-x", is_flag=True, help="Export passwords")
def main(length, count, exclude_uppercase, exclude_lowercase, exclude_numbers, exclude_symbols, export):
    passwords = []

    for i in range(count):
         passwords.append(generate_password(length, exclude_uppercase, exclude_lowercase, exclude_numbers, exclude_symbols))

    if export:
        create_txt_file(get_unique_file_name("Passwords.txt"), passwords)
    else:
        for password in passwords:
            print(password)


if __name__ == '__main__':
    main()
