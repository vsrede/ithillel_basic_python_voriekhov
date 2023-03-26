import json

from utilities.decorator import start_end_decorator
from utilities.dicts import dict_yes_or_no, dict_yes_or_no_for_save_file
from utilities.parser import start_parser

running = True


class Record:
    """Class for creating contact attributes and validating incoming data"""
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
            raise ValueError("Invalid input! Number should be in tests valid format, try again:")

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
        """The function can print tests contact, I don’t know why I did it here initially, I didn’t delete it"""
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %20s |" % self._surname)
        print("| Name:    %20s |" % self._name)
        print("| Age:     %20s |" % self._age)
        print("| Phone:   %20s |" % self._phone_number)
        print("| Email:   %20s |" % self._log_insta)


class PhoneBook:
    """The class contains the main functions for working with the phone book"""
    def __init__(self, records=None):
        self.records = [] if not records else records

    @staticmethod
    def get_input_str(prompt=None, options=None):
        """Helper function to validate information from the user. Answer options are in the dictionary"""
        while True:
            user_input = input(prompt) if prompt else input()
            if not options:
                return user_input
            if user_input in options:
                return options[user_input]
            print('Try again. Valid options are: {}'.format(', '.join(options.keys())))

    def print_phonebook(self):
        """Template function () displays objects on the screen"""
        print("#########  Phone book  ##########")

        number = 1
        for entry in self.records:
            self.print_entry(number, entry)
            number += 1

    @staticmethod
    @start_end_decorator
    def print_entry(number, entry):
        """The function is tests template for displaying tests contact"""
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %30s |" % entry["surname"])
        print("| Name:    %30s |" % entry["name"])
        print("| Age:     %30s |" % entry["age"])
        print("| Phone:   %30s |" % entry["phone_number"])
        print("| Instagram account:   %18s |" % entry["log_insta"])
        print()

    def print_phonebook_by_age(self):
        """The function sorts the book in ascending order of the contact's age"""
        result = sorted(self.records, key=lambda x: x['age'])
        number = 1
        for entry in result:
            self.print_entry(number, entry)
            number += 1

    @start_end_decorator
    def add_entry_phonebook(self):
        """The function create tests new Record(obj) and add it to the book"""
        a = Record()
        self.records.append({"name": a.name,
                             "surname": a.surname,
                             "age": a.age,
                             "phone_number": a.phone_number,
                             "log_insta": a.log_insta
                             })
        print("Successful")

    def find_entry_age_phonebook(self):
        """The function creates an age variable and searches the phonebook for occurrences with the given age,
        if it finds tests print of the occurrence"""
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
        if it finds tests print of the occurrence"""
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
        """The function creates tests variable with tests name that the user enters. If such tests name exists in the
        phonebook, delete it, print the number of occurrences removed and the edited phonebook. Use func 'get_input_str'
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

    @start_end_decorator
    def count_all_entries_in_phonebook(self):
        """The function prints the length of the book"""
        print("Quantity are", len(self.records))

    @start_end_decorator
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

    @start_end_decorator
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
        if PhoneBook.get_input_str(prompt="Do you want to download tests contact book? Enter 'y' if yes, 'n' if no: ",
                                   options=dict_yes_or_no):
            with open('export_phone_book.json', 'r') as file:
                try:
                    my_phone_new = json.load(file)
                    print("Phone book loaded")
                except ValueError:
                    print("File is not JSON")

        return my_phone_new


my_phone_book = PhoneBook(start_parser()[0])


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

        except Exception:
            printError("Something went wrong. Try again...")


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
