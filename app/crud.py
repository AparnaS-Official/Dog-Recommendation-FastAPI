from typing import List, Optional
from app.models import Dog, DogCreate
from app.database import dog_db


def get_dogs() -> List[Dog]:
    return list(dog_db.values())


def get_dog(dog_name: str) -> Optional[Dog]:
    return dog_db.get(dog_name)


def create_dog(dog: DogCreate) -> Dog:
    dog_db[dog.name] = dog.model_dump()
    return Dog(**dog.model_dump())


def update_dog(dog_name: str, dog: DogCreate) -> Optional[Dog]:
    if dog_name in dog_db:
        dog_db[dog_name] = dog.model_dump()
        return Dog(**dog.model_dump())
    return None


def delete_dog(dog_name: str) -> Optional[Dog]:
    return dog_db.pop(dog_name, None)


def filter_dogs_by_purpose(purpose: str) -> List[Dog]:
    return [Dog(**dog) for dog in dog_db.values() if dog['purpose'] == purpose]


def filter_dogs_by_origin(origin: str) -> List[Dog]:
    return [Dog(**dog) for dog in dog_db.values() if dog['origin'] == origin]


def filter_dogs_by_speciality(speciality: str) -> List[Dog]:
    return [Dog(**dog) for dog in dog_db.values() if dog['speciality'] == speciality]


def filter_dogs_by_breed(breed: str) -> List[Dog]:
    return [Dog(**dog) for dog in dog_db.values() if breed.lower() in dog['breed'].lower()]


def get_available_purposes() -> List[str]:
    return list(set(dog['purpose'] for dog in dog_db.values()))


def get_available_origins() -> List[str]:
    return list(set(dog['origin'] for dog in dog_db.values()))


def get_available_specialities() -> List[str]:
    return list(set(dog['speciality'] for dog in dog_db.values()))


def get_available_breeds() -> List[str]:
    return ["Pure", "Hybrid"]
