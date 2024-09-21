from pydantic import BaseModel, constr

class CategorieModel(BaseModel):
    nom: constr(min_length=1, max_length=50)
    description: Optional[constr(max_length=255)]

    class Config:
        orm_mode = True

# Example usage
categorie = CategorieModel(
    nom="Electronics",
    description="A wide variety of electronic devices."
)

print(categorie)