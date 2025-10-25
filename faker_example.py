from faker import Faker


fake = Faker('ru_RU')

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}

print(user_data)
