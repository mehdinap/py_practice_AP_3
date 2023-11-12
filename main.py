import PhoneBook
import Controller


def printGuid() -> None:
    print("\n1- contacts -a <contact firstName> <contact lastName>\n"
          "2 - contacts - r < contact firstName > < contact lastName >\n"
          "3 - show - g < group name >\n"
          "4 - show - c < contact firstName > < contact lastName >\n"
          "5 - show\n"
          "6 - exit\n"
          )


def choose(phonebook: PhoneBook) -> None:
    order = int(input("chose a number:\t"))
    match order:
        case 1:
            print(Controller.addContact(phonebook))
        case 2:
            print(Controller.deleteContact(phonebook))
        case 3:
            Controller.print_group(phonebook)
        case 4:
            print("\t",Controller.print_contact(phonebook))
        case 5:
            print(phonebook)
        case 6:
            Controller.exit()


if __name__ == '__main__':
    phonebook = PhoneBook.PhoneBook()
    phonebook.file_read()
    while True:
        printGuid()
        choose(phonebook)
