# Functions with output
a = int(input("Type number: "))
b = int(input("Type number: "))


def my_function(a, b):
    return a * b


output = my_function(a, b)

print(output)

name = input("Type name: ")
lastName = input("Type nyour last name: ")


def formatName(f_name, l_name):
    # docstring
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


formated_string = formatName(name, lastName)

print(formated_string)

formatName()