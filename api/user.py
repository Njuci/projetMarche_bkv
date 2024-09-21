# users.py
from fastapi import APIRouter
from pydantic import BaseModel
from  backdend.connexion import connection
from models.user_mdl import UserModel
from backdend.user_back import User_Back
router = APIRouter()

class User(BaseModel):
    username: str
    email: str

@router.post("/users/")
def create_user(user: UserModel):
    user_created=User_Back(user.username,user.nom,user.prenom,user.email,user.password,user.role,user.adresse,user.telephone)
    response=user_created.save()
    if response[0]:
        return {"message":"user created","user":user}
    else:
        return {"message":"user  not created","error":response[1]}
    
@router.get("/users/")
def get_user():
    user = User_Back("","","","","","","","").get_all()
    #specifeir le code de retour
    if user[0]:
        rows=user[1]# Assuming your `rows` contains tuples or lists from the database query:
        field_names = ["username", "nom", "prenom", "email", "password", "role", "adresse", "telephone"]

        # Use zip to create a dictionary and pass it to the `UserModel`
        users = [UserModel(**dict(zip(field_names, row))) for row in rows]
        

        return {"message": "user found", "user": users, "count": len(users)}
    else:
        return {"message": "user not found"}
    
@router.get("/users/{username}")
def get_user_by_username(username: str):
    user = User_Back("","","","","","","","").get_by_username(username)
    if user[0]:
        rows=user[1]
        field_names = ["username", "nom", "prenom", "email", "password", "role", "adresse", "telephone"]
        users = [UserModel(**dict(zip(field_names, row))) for row in rows]
        return {"message": "user found", "user": users}
    else:
        return {"message": "user not found"}
    
# Add a new route to update a user
@router.put("/users/{username}")
def update_user(username: str, user: UserModel):
    user_updated = User_Back(user.username, user.nom, user.prenom, user.email, user.password, user.role, user.adresse, user.telephone)
    response = user_updated.save()
    if response[0]:
        return {"message": "user updated", "user": user}
    else:
        return {"message": "user not updated", "error": response[1]}
# Add a new route to delete a user 
@router.delete("/users/{username}")
def delete_user(username: str):
    user_deleted = User_Back(username, "", "", "", "", "", "", "")
    response = user_deleted.delete()
    if response[0]:
        return {"message": "user deleted", "user": username}
    else:
        return {"message": "user not deleted", "error": response[1]}

    
    
    
    
    
    
    
    
    
    
    
