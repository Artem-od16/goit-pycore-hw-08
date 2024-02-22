import pickle

from classes import AddressBook, Record
from functions import parse_input


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()

    methods = {
        "add": Record.add_phone,
        "change": Record.edit_phone,
        "phone": Record.find_phone,
        "delete-phone": Record.remove_phone,
        "delete-contact": Record.remove_contact,
        "add-birthday": Record.add_birthday,
        "show-birthday": Record.find_birthday,
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(methods["add"](args, book))

        elif command == "change":
            print(methods["change"](args, book))

        elif command == "phone":
            print(methods["phone"](args, book))

        elif command == "delete-phone":
            print(methods["delete-phone"](args, book))

        elif command == "all":
            book.show_all()

        elif command == "add-birthday":
            print(methods["add-birthday"](args, book))

        elif command == "show-birthday":
            print(methods["show-birthday"](args, book))

        elif command == "birthdays":
            book.birthdays()

        elif command == "delete-contact":
            print(methods["delete-contact"](args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
