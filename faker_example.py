from faker import Faker

fake = Faker("ru_Ru")

print(fake.name())
print(fake.address())
print(fake.email())

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

print(user_data)