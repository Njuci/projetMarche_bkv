# categorie.py
from fastapi import APIRouter
from pydantic import BaseModel
from  backdend.connexion import connection
from models.categorie_mdl import CategorieModel
from backdend.categorie_back import Categorie_Back
router = APIRouter()

class Categorie(BaseModel):
    nom: str
    description: str

@router.post("/categories/")
def create_categorie(categorie: CategorieModel):
    categorie_created=Categorie_Back(categorie.nom,categorie.description)
    response=categorie_created.save()
    if response[0]:
        return {"message":"categorie created","categorie":categorie}
    else:
        return {"message":"categorie  not created","error":response[1]}
    
@router.get("/categories/")
def get_categorie():
    categorie = Categorie_Back("","")
    if categorie[0]:
        rows=categorie[1]
        field_names = ["id", "nom", "description"]
        categories = [CategorieModel(**dict(zip(field_names, row))) for row in rows]
        return {"message": "categorie found", "categorie": categories, "count": len(categories)}
    else:
        return {"message": "categorie not found"}
    
@router.get("/categories/{id}")
def get_categorie_by_id(id: int):
    categorie = Categorie_Back("","")
    if categorie[0]:
        rows=categorie[1]
        field_names = ["id", "nom", "description"]
        categories = [CategorieModel(**dict(zip(field_names, row))) for row in rows]
        return {"message": "categorie found", "categorie": categories}
    else:
        return {"message": "categorie not found"}
    
# Add a new route to update a categorie
@router.put("/categories/{id}")
def update_categorie(id: int, categorie: CategorieModel):
    categorie_updated = Categorie_Back(categorie.nom, categorie.description)
    response = categorie_updated.save()
    if response[0]:
        return {"message": "categorie updated", "categorie": categorie}
    else:
        return {"message": "categorie not updated", "error": response[1]}
# Add a new route to delete a categorie
@router.delete("/categories/{id}")
def delete_categorie(id: int):
    categorie = Categorie_Back("","")
    if categorie[0]:
        return {"message": "categorie deleted"}
    else:
        return {"message": "categorie not deleted"}
    
@router.get("/categories/nom/{nom}")
def get_categorie_by_nom(nom: str):
    categorie = Categorie_Back("","")
    if categorie[0]:
        rows=categorie[1]
        field_names = ["id", "nom", "description"]
        categories = [CategorieModel(**dict(zip(field_names, row))) for row in rows]
        return {"message": "categorie found", "categorie": categories}
    else:
        return {"message": "categorie not found"}
    