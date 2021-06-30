from ninja import Schema


class TestSchema(Schema):
    input: str
    x: int

    def result(self):
        return TestResponseSchema(result=self.input * self.x)


class TestResponseSchema(Schema):
    result: str
