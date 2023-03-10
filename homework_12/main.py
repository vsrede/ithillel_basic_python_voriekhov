import copy
from json import load, dumps
from utilities.check_valid_inp import get_input_str
import argparse
#parser.add_argument('-v', '--verbose', action='store_true')
running = True

# ------------------------------------------------------------------------------
# Never use real phone/fax numbers for tests. Use 555 numbers:
# https://en.wikipedia.org/wiki/555_(telephone_number)
parser = argparse.ArgumentParser(description='A program that greets you')

parser.add_argument('-f', '-filename', dest='path_to_file', type=str, help='File to check')
parser.add_argument('-v', '-ververbose', dest='activated_decorator', action='store_true', help='Bool for activated_decorator')

args = parser.parse_args()

address = args.path_to_file
f = open(address)
phone_book = load(f)
activated_decorator = args.activated_decorator


dict_yes_or_no = {'y': 'Will be done...', 'n': 'Maybe next time...'}
dict_yes_or_no_for_save_file = {'y': 'Now let\'s check if the books are different', 'n': 'Maybe next time...'}


# ------------------------------------------------------------------------------
def start_end_text(func):

    def another_func(*args, **kwargs):
        if activated_decorator:
            print('Starting to process your request')
        result = func(*args, **kwargs)

        if activated_decorator:
            print('Processing is over')

        return result

    return another_func


# ------------------------------------------------------------------------------
def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %30s |" % entry["surname"])
    print("| Name:    %30s |" % entry["name"])
    print("| Age:     %30s |" % entry["age"])
    print("| Phone:   %30s |" % entry["phone_number"])
    print("| Instagram account:   %18s |" % entry["log_insta"])
    print()


# ------------------------------------------------------------------------------
def print_phonebook():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


# ------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name = input("    Enter name: ")
    age = int(input("    Enter age: "))
    phone_number = input("    Enter phone num.: ")
    log_insta = input((" Enter login instagram: "))

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["log_insta"] = log_insta
    phone_book.append(entry)


# ------------------------------------------------------------------------------
def printError(message):
    print("ERROR: %s" % message)


# ------------------------------------------------------------------------------
def printInfo(message):
    print("INFO: %s" % message)


# ------------------------------------------------------------------------------
@start_end_text
def find_entry_name_phonebook():
    global phone_book
    name = str(input('Enter name: ')).capitalize()
    idx = 1
    found = False

    for entry in phone_book:
        if entry['name'] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        print('Not found!!')


# ------------------------------------------------------------------------------
@start_end_text
def find_entry_age_phonebook():
    global phone_book
    age = input('Enter age: ')

    while True:
        age = input('Try again,the age can only be an integer, try again: ')
        if age.isdigit():
            age = int(age)
            break
    counter = 0

    for i in range(len(phone_book)):
        if phone_book[i]['age'] == age:
            counter += 1
            print_entry(counter, phone_book[i])
    if counter == 0:
        print("Not found!!")


# ------------------------------------------------------------------------------
@start_end_text
def delete_entry_name_phonebook():
    global phone_book
    name = input('Enter the name: ').capitalize()

    while True:
        if name.isalpha():
            break
        else:
            name = input('Try again, the name can only consist of a letter: ')

    if get_input_str('Are you sure? Enter "y" if yes, "n" if no: ', dict_yes_or_no):
        copy_phone_book = list()
        for i in range(len(phone_book)):
            if phone_book[i]['name'] != name:
                copy_phone_book.append(phone_book[i])
        phone_book = copy.deepcopy(copy_phone_book)


# ------------------------------------------------------------------------------
@start_end_text
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


# ------------------------------------------------------------------------------
@start_end_text
def print_phonebook_by_age():
    global phone_book
    result = sorted(phone_book, key=lambda x: x['age'])
    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


# ------------------------------------------------------------------------------
@start_end_text
def print_phonebook_in_insta():
    global phone_book
    result = sorted(phone_book, key=lambda x: x['log_insta'])
    number = 1
    for entry in phone_book:
        if len(entry['log_insta']) != 0:
            print_entry(number, entry)
            number += 1


# ------------------------------------------------------------------------------
@start_end_text
def increase_age():
    global phone_book
    plus_age = int(input('Enter the digit: '))
    if get_input_str('Are you sure? Enter "y" if yes, "n" if no: ', dict_yes_or_no):
        for num in phone_book:
            num['age'] += plus_age


# ------------------------------------------------------------------------------
@start_end_text
def danger_contact():
    global phone_book
    for num in phone_book:
        if num['phone_number'][0:4] == '+102':
            num['name'] = 'Black_list'
    return phone_book


# ------------------------------------------------------------------------------
@start_end_text
def avr_age_of_all_persons():
    global phone_book
    mid_sum_age_persons = 0
    for num in phone_book:
        mid_sum_age_persons += (num['age'] // 2)
    print(f'The rounded average age is: {mid_sum_age_persons}')


# ------------------------------------------------------------------------------
@start_end_text
def save_to_file():
    global phone_book
    if get_input_str('Do you wan\'t save your contact file? If yes enter "y", else "n": ', dict_yes_or_no_for_save_file):
        f = open('export_phone_book.json')
        import_phone_book = load(f)
        f.close()
        if import_phone_book != phone_book:
            if get_input_str('The saved file and the file you are trying to save are different, '
                             'are you sure?: ', dict_yes_or_no):
                f = open('export_phone_book.json', 'w')
                contents = dumps(phone_book)
                f.write(contents)
                f.close()
        elif import_phone_book == phone_book:
            print('The saved file and the file you are trying to save are same')
        else:
            print('Maybe next time...')


# ------------------------------------------------------------------------------
@start_end_text
def load_from_file():
    save_to_file()
    global phone_book
    if get_input_str('Do you want to download a contact book? Enter "y" if yes, "n" if no: ', dict_yes_or_no):
        f = open('export_phone_book.json')
        phone_book = load(f)
        f.close()


# ------------------------------------------------------------------------------
@start_end_text
def police_contact():
    global phone_book
    for num in phone_book:
        if num['phone_number'][0:4] == '+102':
            num['name'] = 'Black_list'


# ------------------------------------------------------------------------------
def exit():
    global running
    running = False


# ------------------------------------------------------------------------------
def print_prompt():
    print()
    print()
    print()
    print("~ Welcome to phonebook ~")
    print("Select one of actions below:")
    print("     1 - Print phonebook entries")
    print("     2 - Print phonebook entries (by age)")
    print("     3 - Add new entry")
    print("     4 - Find entry by name")
    print("     5 - Find entry by age")
    print("     6 - Delete entry by name")
    print("     7 - The number of entries in the phonebook")
    print("     8 - Avr. age of all persons")
    print("     9 - Increase age by num. of years")
    print("     10 - Rename contact 'police' --> 'black list'")
    print("     11 - Print phonebook entries instagram")
    print("-----------------------------")
    print("     s - Save to file")
    print("     l - Load from file")
    print("     0 - Exit")
    print()


# ------------------------------------------------------------------------------
def main():
    while running:
        try:
            menu = {
                '1': print_phonebook,
                '2': print_phonebook_by_age,
                '3': add_entry_phonebook,
                '4': find_entry_name_phonebook,
                '5': find_entry_age_phonebook,
                '6': delete_entry_name_phonebook,
                '7': count_all_entries_in_phonebook,
                '8': avr_age_of_all_persons,
                '9': increase_age,
                '10': police_contact,
                '11': print_phonebook_in_insta,

                '0': exit,
                's': save_to_file,
                'l': load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()