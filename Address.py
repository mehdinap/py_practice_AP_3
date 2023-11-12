class Address:
    zipCode: str = ""
    country: str = ""
    city: str = ""
    email: str = ""

    def __init__(
            self,
            zCode: str,
            country: str,
            city: str,
            email: str = None
    ) -> None:
        self.zipCode = zCode
        self.country = country
        self.city = city
        self.email = email

    def info(self) -> str:
        return ("zip code:", self.zipCode, "\ncountry:", self.country,
                "\ncity:", self.city, "\nemail:", self.email)
