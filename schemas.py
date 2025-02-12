from pydantic import BaseModel


class FormSchema(BaseModel):
    name: str
    phone: int
    age: str
    category: str
    job: str
    motivation: str
    sex: str
