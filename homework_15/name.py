import json
import argparse
running = True

class Record:
    def __init__(self):
        self._name = ""
        self._surname = ""
        self._age = 0
        self._phone_number = ""
        self._log_insta = ""
        self.get_input()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.isalpha():
            self._name = value
        else:
            raise ValueError("Invalid input! Name can be only contain letters, try again: ")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if value.isalpha():
            self._surname = value
        else:
            raise ValueError("Invalid input! Surname can be only contain letters, try again:")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value.isdigit() and 100 >= int(value) >= 1:
            self._age = int(value)
        else:
            raise ValueError("Invalid input! Name can be only contain digits and bigger then 0 and smaller then 101, "
                             "try again:")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value.isdigit() and len(value) <= 12:
            self._phone_number = value
        else:
            raise ValueError("Invalid input! Number should be in a valid format, try again:")

    @property
    def log_insta(self):
        return self._log_insta

    @log_insta.setter
    def log_insta(self, value):
        self._log_insta = value

    def get_input(self):
        while True:
            try:
                self.surname = input("Enter your surname: ").capitalize()
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.name = input("Enter your name: ").capitalize()
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.age = input("Enter your age: ")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.phone_number = input("Enter your phone number : ")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                self.log_insta = input("Enter your instagram login: ").lower()
                break
            except ValueError as e:
                print(e)

    def print_record(self, number):
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %20s |" % self._surname)
        print("| Name:    %20s |" % self._name)
        print("| Age:     %20s |" % self._age)
        print("| Phone:   %20s |" % self._phone_number)
        print("| Email:   %20s |" % self._log_insta)


class PhoneBook:
    def __init__(self, records=None):
        self.records = [] if not records else records


    @staticmethod
    def get_input_str(prompt=None, options=None):
        while True:
            user_input = input(prompt) if prompt else input()
            if not options:
                return user_input
            if user_input in options:
                return options[user_input]
            print('Try again. Valid options are: {}'.format(', '.join(options.keys())))

    def print_phonebook(self):
        print("#########  Phone book  ##########")

        number = 1
        for entry in self.records:
            self.print_entry(number, entry)
            number += 1

    @staticmethod
    def print_entry(number, entry):
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %30s |" % entry["surname"])
        print("| Name:    %30s |" % entry["name"])
        print("| Age:     %30s |" % entry["age"])
        print("| Phone:   %30s |" % entry["phone_number"])
        print("| Instagram account:   %18s |" % entry["log_insta"])
        print()

    def add_entry_phonebook(self):
        """The function create a new Record(obj) and add it to the book"""
        a = Record()
        self.records.append({"name": a.name,
                             "surname": a.surname,
                             "age": a.age,
                             "phone_number": a.phone_number,
                             "log_insta": a.log_insta
                             })

    def find_entry_age_phonebook(self):
        """The function creates an age variable and searches the phonebook for occurrences with the given age,
        if it finds a print of the occurrence"""
        user_input = input("Enter age: ")
        while True:
            if user_input.isdigit():
                break
            else:
                user_input = input("Invalid input! Name can be only contain digits, try again: ")
        counter = 0
        for num in self.records:
            if num['age'] == int(user_input):
                counter += 1
                PhoneBook.print_entry(counter, num)
        if counter == 0:
            print("Not found bro, don't be sad")

    def find_entry_name_phonebook(self):
        """The function creates an age variable and searches the phonebook for occurrences with the given name,
        if it finds a print of the occurrence"""
        user_input = input("Enter name: ")
        while True:
            if user_input.isalpha():
                break
            else:
                user_input = input("Invalid input! Name can be only contain digits, try again: ")
        counter = 0
        for num in self.records:
            if num['name'] == user_input:
                counter += 1
                PhoneBook.print_entry(counter, num)
        if counter == 0:
            print("Not found bro, don't be sad")

    def delete_entry_name_phonebook(self):
        """The function creates a variable with a name that the user enters. If such a name exists in the phonebook,
        delete it, print the number of occurrences removed and the edited phonebook. Use func 'get_input_str'
        to get confirmation from the user"""
        user_input = input("Enter name: ").capitalize()
        counter = 0
        while True:
            if user_input.isalpha():
                break
            else:
                user_input = input("Invalid input! Surname can be only contain letters, try again: ").capitalize()
        records_copy = self.records.copy()
        for num in records_copy:
            if num['name'] == user_input:
                counter += 1
                if PhoneBook.get_input_str(prompt="Are your sure? ", options=dict_yes_or_no):
                    self.records.remove(num)
                    print(f"The {counter} contact has been deleted")

        if counter == 0:
            print(f"No users found with '{user_input}' name")
        my_phone_book.print_phonebook()

    def count_all_entries_in_phonebook(self):
        """The function prints the length of the book"""
        print(len(self.records))

    def print_phonebook_by_age(self):
        """The function sorts the book in ascending order of the contact's age"""
        result = sorted(self.records, key=lambda x: x['age'])
        print(result)

    def increase_age(self):
        """The function increases the age of all occurrences by the entered number"""
        while True:
            user_input = input("Enter the digit: ")
            if user_input.isdigit():
                user_input = int(user_input)
                break
            else:
                print("Invalid input! Name can be only contain digits, try again: ")
        if PhoneBook.get_input_str(prompt="Are you sure? Enter 'y' if yes, 'n' if no: ", options=dict_yes_or_no):
            for num in self.records:
                num['age'] += user_input
            print(f'Age has been increased by {user_input} years')

    def avr_age_of_all_persons(self):
        """The function prints the average age of all contacts in the book"""
        summ_age = 0

        for num in self.records:
            summ_age += num['age']
        mid_sum_age = round(summ_age / len(self.records), 1)
        print(f"Average age of your contacts {mid_sum_age} years")

    @staticmethod
    def save_to_file():
        """The function exports the book into the main directory with the name export_phone_book.json"""
        if PhoneBook.get_input_str(prompt="Do you wan\'t save your contact file? If yes enter 'y, else 'n: ",
                                   options=dict_yes_or_no_for_save_file):
            with open('export_phone_book.json', 'w') as file:
                contents = json.dumps(my_phone_book.records)
                file.write(contents)
            print("Phone book saved to file")
        else:
            print("Maybe next time...")

    @staticmethod
    def load_from_file():
        if PhoneBook.get_input_str(prompt="Do you want to download a contact book? Enter 'y' if yes, 'n' if no: ",
                                   options=dict_yes_or_no):
            with open('export_phone_book.json', 'r') as file:
                try:
                    my_phone_new = json.load(file)
                    print("Phone book loaded")
                except ValueError:
                    print("File is not JSON")

        return my_phone_new


def start_parser():
    parser = argparse.ArgumentParser(description='A program that greets you')

    parser.add_argument('-f', '-filename', dest='path_to_file', type=str, help='File to check')
    parser.add_argument('-v', '-verbose', dest='activated_decorator', action='store_true',
                        help='Bool for activated_decorator')

    args = parser.parse_args()

    address = args.path_to_file
    activated_decorator = args.activated_decorator
    with open(address) as file:
        phone_book = json.load(file)
        return phone_book, activated_decorator



# my_phone_book = PhoneBook(start_parser()[0])
my_phone_book = [
  {"name": "Gus", "surname": "Super", "age": 51, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Bus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Nus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Zus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Cus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Vus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Bus", "surname": "Super", "age": 1, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Nus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Mus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Aus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Sus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Dus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
  {"name": "Fus", "surname": "Super", "age": 50, "phone_number": "+18005550102", "log_insta": "cynepcyc"}
]
my_phone_book = PhoneBook(my_phone_book)
dict_yes_or_no = {'y': 'Will be done...', 'n': 'Maybe next time...'}
dict_yes_or_no_for_save_file = {'y': 'Now let\'s check if the books are different', 'n': 'Maybe next time...'}


def printError(message):
    print("ERROR: %s" % message)


def printInfo(message):
    print("INFO: %s" % message)


def exit():
    global running
    running = False


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
                '1': my_phone_book.print_phonebook,
                '2': my_phone_book.print_phonebook_by_age,
                '3': my_phone_book.add_entry_phonebook,
                '4': my_phone_book.find_entry_name_phonebook,
                '5': my_phone_book.find_entry_age_phonebook,
                '6': my_phone_book.delete_entry_name_phonebook,
                '7': my_phone_book.count_all_entries_in_phonebook,
                '8': my_phone_book.avr_age_of_all_persons,
                '9': my_phone_book.increase_age,

                '0': exit,
                's': my_phone_book.save_to_file,
                'l': my_phone_book.load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# my_phone_book = PhoneBook(my_phone_book)
# my_phone_book.print_phonebook()
# my_phone_book.add_entry_phonebook()
# my_phone_book.find_entry_age_phonebook()
# my_phone_book.find_entry_name_phonebook()
# my_phone_book.delete_entry_name_phonebook()
# my_phone_book.count_all_entries_in_phonebook()
# my_phone_book.print_phonebook_by_age()
# my_phone_book.increase_age()
# my_phone_book.avr_age_of_all_persons()
# my_phone_book.save_to_file()
# my_phone_book = PhoneBook(PhoneBook.load_from_file())

