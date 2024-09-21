from .connexion import Connexion

class Categorie_Back:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.connection = Connexion('root', '3670njci')

    def save(self):
        try:
            self.connection.get_curseur().execute(
                "Insert into tb_categorie(nom,description) Values(%s,%s)",
                (self.nom, self.description)
            )
            return True, ""
        except Exception as e:
            return False, str(e)

    def get_all(self):
        try:
            self.connection.get_curseur().execute("Select *from tb_categorie")
            return True, self.connection.get_curseur().fetchall()
        except Exception as e:
            return False, []

    def get_by_id(self, id):
        try:
            self.connection.get_curseur().execute("Select *from tb_categorie where id=%s", (id,))
            return True, self.connection.get_curseur().fetchall()
        except Exception as e:
            return False, []

    def update(self):
        try:
            self.connection.get_curseur().execute(
                "Update tb_categorie set nom=%s, description=%s where id=%s",
                (self.nom, self.description, self.id)
            )
            return True, ""
        except Exception as e:
            return False, str(e)

    def delete(self):
        try:
            self.connection.get_curseur().execute("Delete from tb_categorie where id=%s", (self.id,))
            return True, ""
        except Exception as e:
            return False, str(e)
        
    def get_by_nom(self, nom):
        try:
            self.connection.get_curseur().execute("Select *from tb_categorie where nom=%s", (nom,))
            return True, self.connection.get_curseur().fetchall()
        except Exception as e:
            return False, []
        
    def get_by_description(self, description):
        try:
            self.connection.get_curseur().execute("Select *from tb_categorie where description=%s", (description,))
            return True, self.connection.get_curseur().fetchall()
        except Exception as e:
            return False, []