import Address
import Contact
import PhoneNumber


class PhoneBook:
    contact: Contact

    def __init__(self) -> None:
        self.contact = []

    def addContact(self, contact: Contact) -> bool:
        if contact in self.contact:
            return False
        self.contact.append(contact)
        return True

    def deleteContact(self, firstname: str, lastname: str) -> bool:
        for i in self.contact:
            if (i.firstName.__eq__(firstname) and
                    i.lastName.__eq__(lastname)):
                self.contact.remove(i)
                return True
        return False

    def findContact(self, firstname: str, lastname: str) -> Contact:
        for i in self.contact:
            if i.firstName.__eq__(firstname) and i.lastName.__eq__(lastname):
                return i
        return None

    def findContacts(self, group: str) -> list:
        lis = []
        for i in self.contact:
            if (i.group.__eq__(group)):
                lis.append(i)
        if lis.__len__() == 0:
            return None
        return lis

    def file_read(self) -> None:
        with open("storage/contacts", "r") as file:
            while True:
                try:
                    file_contact = make_contact(file.__next__().split("!"))
                except StopIteration:
                    break
                self.contact.append(file_contact)

    def file_write(self) -> None:
        with open("storage/contacts", "w") as file:
            file.flush()
            for i in self.contact:
                file.write(str(i.to_file()))


def make_contact(info: list) -> Contact.Contact:
    return Contact.Contact(info[0], info[1], info[2],
                           info[3], PhoneNumber.PhoneNumber(info[4], info[5]),
                           Address.Address(info[6], info[7], info[8])
                           )
