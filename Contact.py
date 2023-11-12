import Address
import PhoneNumber


class Contact:
    group: str = ""
    email: str = ""
    firstName: str = ""
    lastName: str = ""
    phoneNumber: PhoneNumber
    address: Address

    def __init__(self, group: str, email: str, firstName: str,
                 lastName: str, phoneNumber: PhoneNumber.PhoneNumber,
                 address: Address.Address) -> None:
        self.group = group
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.address = address

    def info(self) -> str:
        return f"name: {self.firstName} {self.lastName} \
                \n\tgroup: {self.group}\n\temail: {self.email} \
                \n\t{self.phoneNumber.info()}\n\t{self.address.info()}"

    def to_file(self) -> str:
        return (f"{self.group}!{self.email}!{self.firstName}!{self.lastName}!"
                f"{self.phoneNumber.countryCode}!{self.phoneNumber.number}!"
                f"{self.address.zipCode}!{self.address.country}!{self.address.city}")


if __name__ == "__main__":
    d = Contact("fx", "najibpour6@gmail.com",
                "mehdi", "najibpour",
                PhoneNumber.PhoneNumber("+98", "2"),
                Address.Address("64611", "IRAN", "Tehran"))
    print(d.info())
