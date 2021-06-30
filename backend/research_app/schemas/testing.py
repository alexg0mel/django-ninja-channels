from pydantic import BaseModel


class TestSchema(BaseModel):
    input: str
    x: int


class TestResponseSchema(BaseModel):
    result: str
