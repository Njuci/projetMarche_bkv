from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UserModel(BaseModel):
    username: constr(min_length=1, max_length=50)
    nom: Optional[constr(max_length=50)]
    prenom: Optional[constr(max_length=50)]
    email: EmailStr
    password: constr(min_length=1, max_length=50)
    role: constr(min_length=1, max_length=50)
    adresse: Optional[constr(max_length=50)]
    telephone: Optional[constr(max_length=50)]

    class Config:
        orm_mode = True

# Example usage
user = UserModel(
    username="johndoe",
    nom="Doe",
    prenom="John",
    email="johndoe@example.com",
    password="securepassword",
    role="vendeur",
    adresse="123 Main St",
    telephone="123-456-7890"
)

print(user)