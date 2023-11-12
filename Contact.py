from Address import Address
from PhoneNumber import PhoneNumber


class Contact:
    group: str = ""
    email: str = ""
    firstName: str = ""
    lastName: str = ""
    phoneNumber: PhoneNumber
    address: Address

    def __init__(
            self,
            group: str = None,
            email: str = None,
            firstName: str = not None,
            lastName: str = not None,
            phoneNumber: PhoneNumber = not None,
            address: Address = not None
    ) -> None:
        self.group = group
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.address = address
