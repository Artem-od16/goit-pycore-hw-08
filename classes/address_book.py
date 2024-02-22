from collections import UserDict

from functions import get_upcoming_birthdays

from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def show_all(self):
        for name, record in self.data.items():
            print(record)

    def birthdays(self):
        get_upcoming_birthdays(self)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
