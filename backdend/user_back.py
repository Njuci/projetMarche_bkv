from .connexion import Connexion

class User_Back:
    def __init__(self, username, nom, prenom, email, password, role, adresse, telephone):
        self.username = username
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.role = role
        self.adresse = adresse
        self.telephone = telephone
        self.connection=Connexion('root','3670njci')
    def save(self):
        try:
              # Debugging: Print the telephone value before the insert
            print(f"Debug: Telephone value before insert: {self.telephone}")

            self.connection.get_curseur().execute(
                "Insert into tb_utilisateur(username,nom,prenom,email,password,adresse,telephone) Values(%s,%s,%s,%s,%s,%s,%s) "
                 ,(self.username,self.nom,self.prenom,self.email,self.password,
                   self.adresse,self.telephone)   )
            return True,""
        except Exception as e:
            return False,str(e)
    def get_all(self):
        try:
            self.connection.get_curseur().execute("Select *from tb_utilisateur")
            return True,self.connection.get_curseur().fetchall()
        except Exception as e:
            return False,[]
    # Add a method to get a single user by username
    def get_by_username(self, username):
        try:
            self.connection.get_curseur().execute("Select *from tb_utilisateur where username=%s", (username,))
            return True, self.connection.get_curseur().fetchall()
        except Exception as e:
            return False, []
        
    # Add a method to update a user
    def update(self):
        try:
            self.connection.get_curseur().execute(
                "Update tb_utilisateur set nom=%s, prenom=%s, email=%s, password=%s, role=%s, adresse=%s, telephone=%s where username=%s",
                (self.nom, self.prenom, self.email, self.password, self.role, self.adresse, self.telephone, self.username)
            )
            return True, ""
        except Exception as e:
            return False, str(e)
    # Add a method to delete a user
    def delete(self):
        try:
            self.connection.get_curseur().execute("Delete from tb_utilisateur where username=%s", (self.username,))
            return True, ""
        except Exception as e:
            return False, str(e)
        