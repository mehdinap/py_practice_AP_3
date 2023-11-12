class PhoneNumber:
    countryCode: str = ""
    number: str = ""

    def __init__(self, countryCode: str = not None, number: str = not None) -> None:
        self.countryCode = countryCode
        self.number = number

    def info(self) -> str:
        return f"phone number: ({self.countryCode}) {self.number}"
