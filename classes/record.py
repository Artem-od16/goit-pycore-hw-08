from datetime import datetime

from .birthday import Birthday
from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @classmethod
    def add_phone(cls, args: list, book):
        if len(args) < 2:
            return "Provide both name and phone for the contact."

        name, phone = args

        if not phone.isdigit() or len(phone) != 10:
            return "Phone number must consist of 10 digits."

        exist = book.find(name)
        if not exist:
            record = cls(name)
            record.phones.append(Phone(phone))
            book.add_record(record)
            return "Phone added."
        else:
            exist.phones.append(Phone(phone))
            return "Phone added."

    @classmethod
    def add_birthday(cls, args: list, book):
        if len(args) < 2:
            return "Provide both name and date for the birthday."

        name, date = args

        try:
            datetime.strptime(date, "%d.%m.%Y")
            exist = book.find(name)
            if not exist:
                return "Contact not found."
            else:
                exist.birthday = Birthday(date)
                return "Birthday added."
        except ValueError:
            return "Invalid date format. Use DD.MM.YYYY."

    @classmethod
    def remove_phone(cls, args: list, book):
        if len(args) < 2:
            return "Provide both name and phone of the contact."

        name, phone = args

        exist = book.find(name)
        if not exist:
            return "Contact not found."
        else:
            exist.phones = [p for p in exist.phones if p.value != phone]
            return "Phone deleted."

    @classmethod
    def remove_birthday(cls, args: list, book):
        if len(args) < 2:
            return "Provide name of the contact."

        name = args[0]

        exist = book.find(name)
        if not exist:
            return "Contact not found."
        else:
            exist.birthday = None
            return "Birthday deleted."

    @classmethod
    def remove_contact(cls, args: list, book):
        if len(args) < 1:
            return "Provide name of the contact."

        name = args[0]

        exist = book.find(name)
        if not exist:
            return "Contact not found."
        else:
            book.delete(name)
            return "Contact deleted."

    @classmethod
    def edit_phone(cls, args: list, book):
        if len(args) < 3:
            return "Provide all arguments name,old and new phones of the contact."

        name, old_phone, new_phone = args

        if (not old_phone.isdigit() or len(old_phone) != 10) or (
            not new_phone.isdigit() or len(new_phone) != 10
        ):
            return "Phone number must consist of 10 digits."

        exist = book.find(name)
        if not exist:
            return "Contact not found."
        else:
            for phone in exist.phones:
                if phone.value == old_phone:
                    phone.value = new_phone
                    return "Phone changed."
        return "Phone not found."

    @classmethod
    def edit_birthday(cls, args: list, book):
        if len(args) < 2:
            return "Provide both name and date for the birthday."

        name, date = args

        try:
            datetime.strptime(date, "%d.%m.%Y")
            exist = book.find(name)
            if not exist:
                return "Contact not found."
            else:
                exist.birthday = Birthday(date)
                return "Birthday changed."
        except ValueError:
            return "Invalid date format. Use DD.MM.YYYY."

    @classmethod
    def find_phone(cls, args: list, book) -> Phone:

        if len(args) < 1:
            return "Provide name of the contact."

        contact = args[0]

        for name, record in book.data.items():
            if name == contact:
                return record
            else:
                continue
        return "Contact not found."

    @classmethod
    def find_birthday(cls, args: list, book) -> Birthday:

        if len(args) < 1:
            return "Provide name of the contact."

        contact = args[0]

        for name, record in book.data.items():
            if contact == name:
                return record.birthday
            else:
                continue
        return "Contact not found."

    def __str__(self):

        birthday_info = ""
        if self.birthday:
            birthday_info = f"birthday date: {self.birthday.value.strftime('%d %B %Y')}"

        phones_info = ", ".join(str(p) for p in self.phones)

        return f"      - Contact name: {self.name.value}; phones: {phones_info}; {birthday_info}"
