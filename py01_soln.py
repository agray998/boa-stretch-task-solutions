#! venv/bin/python3

if __name__ == '__main__':
    input_name = input("Enter firstname,lastname: ")
    first_name, last_name = input_name.split(',') # this line unpacks the input into separate variables
    print(f"{last_name.upper()}, {first_name.capitalize()}")
    print(last_name.lower().endswith('son'))
    full_name = input_name.lower().replace(',', ' ')
    total_vowels = full_name.count('a') + full_name.count('e') + full_name.count('i') + full_name.count('o') + full_name.count('u')
    print(total_vowels)
    print((len(first_name) - len(last_name)) ** 2)