from pydantic import BaseModel


class TextInput(BaseModel):
    reference: str
    candidate: str