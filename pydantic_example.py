from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = Field(alias="isActive")

user = User(
    id=1,
    name='Alice',
    email='alice@example.com',
    address={"city": "New York", "zip_code": "10001"}
    )
print(user.model_dump())
print(user.model_dump_json())