from ninja import Schema


class CountrySchema(Schema):
    id: int
    name: str
    full_name: str
    numcode: int
    alfa2: str
