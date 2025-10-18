from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class ShortUserSchema(BaseModel):
    """ Описание сокращенной структуры пользователя. """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class UserSchema(ShortUserSchema):
    """ Описание структуры пользователя. """
    id: str


class CreateUserRequestSchema(ShortUserSchema):
    """ Описание структуры запроса создания пользователя. """
    password: str


class CreateUserResponseSchema(BaseModel):
    """ Описание структуры ответа создания пользователя. """
    user: UserSchema
