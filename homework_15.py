my_phone = [{"name": "GGG", "surname": "Super", "age": 57, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
            {"name": "GGG", "surname": "Super", "age": 57, "phone_number": "+18005550102", "log_insta": "cynepcyc"},
            {"name": "GGG", "surname": "Super", "age": 57, "phone_number": "+18005550102", "log_insta": "cynepcyc"}]


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
            raise ValueError("Invalid input! Name can be only contain letters")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if value.isalpha():
            self._surname = value
        else:
            raise ValueError("Invalid input! Surname can be only contain letters")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value.isdigit() and 100 >= int(value) >= 1:
            self._age = int(value)
        else:
            raise ValueError("Invalid input! Name can be only contain digits and bigger then 0 and smaller then 101")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value.isdigit() and len(value) <= 12:
            self._phone_number = value
        else:
            raise ValueError("Invalid input! Number should be in a valid format.")

    @property
    def log_insta(self):
        return self._log_insta

    @log_insta.setter
    def log_insta(self, value):
        self._log_insta = value

    def get_input(self):
        while True:
            try:
                self.surname = input("Enter your surname: ")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.name = input("Enter your name: ")
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
                self.log_insta = input("Enter your instagram login: ")
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

    def print_phonebook(self):
        print("#########  Phone book  ##########")

        number = 1
        for entry in self.records:
            self.print_entry(number, entry)
            number += 1

    @staticmethod
    def print_entry(number, entry):
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %30s |" % entry.surname)
        print("| Name:    %30s |" % entry.name)
        print("| Age:     %30s |" % entry.age)
        print("| Phone:   %30s |" % entry.phone_number)
        print("| Instagram account:   %18s |" % entry.log_insta)
        print()

    def add_entry_phonebook(self, record):
        self.records.append(record)


my_phone = PhoneBook(my_phone)
my_phone.print_phonebook()

