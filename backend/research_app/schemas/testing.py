import datetime
from ninja import Schema


class TestSchema(Schema):
    input: str
    x: int

    def result(self):
        return TestResponseSchema(result=self.input * self.x)


class TestResponseSchema(Schema):
    result: str


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)
