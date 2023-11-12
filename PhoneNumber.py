class PhoneNumber:
    countryCode: str = ""
    number: str = ""

    def __init__(
            self,
            countryCode: str,
            number: str
    ) -> None:
        self.countryCode = countryCode
        self.number = number

    def info(self) -> str:
        return ("country code:", self.countryCode, "number:", self.number)
