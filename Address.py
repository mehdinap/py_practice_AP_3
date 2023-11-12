class Address:
    zipCode: str = ""
    country: str = ""
    city: str = ""

    def __init__(self, zCode: str = not None, country: str = not None, city: str = not None) -> None:
        self.zipCode = zCode
        self.country = country
        self.city = city

    def info(self) -> str:
        return f"address: {self.zipCode} - {self.country} - {self.city}"
