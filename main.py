# app/main.py

from fastapi import FastAPI, HTTPException
from typing import List
from app.models import Dog, DogCreate
from app.crud import (
    get_dogs, get_dog, create_dog, update_dog, delete_dog,
    filter_dogs_by_purpose, filter_dogs_by_origin, filter_dogs_by_speciality, filter_dogs_by_breed
)
from app.enum.Purpose_enum import PurposeEnum
from app.enum.Origin_enum import OriginEnum
from app.enum.Speciality_enum import SpecialityEnum
from app.enum.Breed_enum import BreedEnum

app = FastAPI()


@app.get("/dogs", response_model=List[Dog])
def read_dogs():
    return get_dogs()


@app.get("/dogs/{dog_name}", response_model=Dog)
def read_dog(dog_name: str):
    dog = get_dog(dog_name)
    if dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dog


@app.post("/dogs", response_model=Dog)
def create_dog_entry(dog: DogCreate):
    return create_dog(dog)


@app.put("/dogs/{dog_name}", response_model=Dog)
def update_dog_entry(dog_name: str, dog: DogCreate):
    updated_dog = update_dog(dog_name, dog)
    if updated_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return updated_dog


@app.delete("/dogs/{dog_name}", response_model=Dog)
def delete_dog_entry(dog_name: str):
    deleted_dog = delete_dog(dog_name)
    if deleted_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return deleted_dog


@app.get("/by_purpose", response_model=List[Dog])
def get_dogs_by_purpose(purpose: PurposeEnum):
    return filter_dogs_by_purpose(purpose.value)


@app.get("/by_origin", response_model=List[Dog])
def get_dogs_by_origin(origin: OriginEnum):
    return filter_dogs_by_origin(origin.value)


@app.get("/by_speciality", response_model=List[Dog])
def get_dogs_by_speciality(speciality: SpecialityEnum):
    return filter_dogs_by_speciality(speciality.value)


@app.get("/by_breed", response_model=List[Dog])
def get_dogs_by_breed(breed: BreedEnum):
    return filter_dogs_by_breed(breed.value)
