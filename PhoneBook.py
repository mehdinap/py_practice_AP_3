import Contact


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
            if (Contact.Contact(i).firstName.__eq__(firstname) and
                    Contact.Contact(i).lastName.__eq__(lastname)):
                self.contact.remove(i)
                return True
        return False

    def findContact(self, firstname: str, lastname: str) -> Contact:
        for i in self.contact:
            if (Contact.Contact(i).firstName.__eq__(firstname) and
                    Contact.Contact(i).lastName.__eq__(lastname)):
                return i
        return None

    def findContacts(self, group: str) -> list:
        lis = []
        for i in self.contact:
            if (Contact.Contact(i).group.__eq__(group)):
                lis.append(i)
        if lis.__len__() == 0:
            return None
        return lis

    def file_read(self) -> None:
        with open("storage/contacts", "r") as file:
            list = file.readlines(2)
            print(list)

    def file_write(self) -> None:
        with open("storage/contacts", "w") as file:
            file.flush()
            for i in self.contact:
                file.write(str(i.info()))
