from pydantic import BaseModel

class DogBase(BaseModel):
    name: str
    height: float
    weight: float
    breed: str
    purpose: str
    speciality: str
    origin: str

class DogCreate(DogBase):
    pass

class Dog(DogBase):
    pass
