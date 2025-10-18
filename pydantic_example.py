from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     address: Address
#     is_active: bool = True

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")

user_data = {
    'id': 1,
    'name': 'Alice',
    'email': "alice@example.com",
    'isActive': True
}


# model_dump() - для получения словаря из объекта модели
# model_dump_json() - для получения json-строки из объекта модели
user = User(**user_data)
print(user.model_dump())
