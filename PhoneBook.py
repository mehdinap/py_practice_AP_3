from Contact import Contact


class PhoneBook:
    contact: list = []

    def __init__(self) -> None:
        pass

    def addContact(
            self,
            contact: Contact
    ) -> bool:
        if contact in self.contact: return False
        self.contact.append(contact)
        return True

    def deleteContact(
            self,
            firstname: str,
            lastname: str
    ) -> bool:
        for i in self.contact:
            if (Contact(i).firstName == firstname and
                    Contact(i).lastName == lastname):
                self.contact.remove(i)
                return True
        return False

    def findContact(
            self,
            firstname: str,
            lastname: str
    ) -> Contact:
        for i in self.contact:
            if (Contact(i).firstName == firstname and
                    Contact(i).lastName == lastname):
                return i
        return None

    def findContacts(
            self,
            group: str
    ) -> list:
        lis = []
        for i in self.contact:
            if (Contact(i).group == group):
                lis.append(i)
        return lis

    def printContacts(self) -> list:
        return self.contact
