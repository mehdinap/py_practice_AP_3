import Address
import Contact, PhoneNumber, PhoneBook


def addContact(phonebook: PhoneBook.PhoneBook) -> str:
    if phonebook.addContact(makeContact()):
        phonebook.file_write()
        return "the contact added"
    else:
        return "the contact is exist"


def makeContact() -> Contact.Contact:
    first: str = input("Please enter contact's last name:")
    last: str = input("Please enter contact's first name:")
    group: str = input("Please enter contact's group(None):")
    email: str = input("Please enter contact's email(None):")
    countrycode: str = input("Please enter contact's country code:")
    number: str = input("Please enter contact's phone number:")
    zipcode: str = input("Please enter contact's zip code(None):")
    country: str = input("Please enter contact's country(None):")
    city: str = input("Please enter contact's city:")
    return Contact.Contact(
        group,
        email,
        first,
        last,
        PhoneNumber.PhoneNumber(
            countrycode,
            number
        ),
        Address.Address(
            zipcode,
            country,
            city
        )
    )


def deleteContact(phonebook: PhoneBook.PhoneBook) -> str:
    first, last = input("enter <first name> <last name>:").split(" ")
    if phonebook.deleteContact(first, last):
        # phonebook.file_write()
        return "OK"
    else:
        return "Not found"


def print_group(phonebook: PhoneBook.PhoneBook) -> None:
    lis = get_group(phonebook)
    if lis.__eq__("None"):
        print("Not find")
    for i in lis:
        print("\t", Contact.Contact(i).info())


def get_group(phonebook: PhoneBook.PhoneBook) -> list:
    group = input("enter a group: ")
    return phonebook.findContacts(group)


def print_contact(phonebook: PhoneBook.PhoneBook) -> str:
    (first, *last) = input("enter <first name> <last name>:").split(" ")
    contact: Contact.Contact = phonebook.findContact(first, last)
    if contact is None:
        return "\n\t<<<Not find>>>"
    return contact.info()


def print_contacts(phonebook: PhoneBook.PhoneBook) -> None:
    for i in phonebook.contact:
        print("\t", Contact.Contact(i).info())


def exit() -> None:
    quit(0)
