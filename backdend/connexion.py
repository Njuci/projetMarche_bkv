import mysql.connector

class Connexion:
    def __init__(self,user,password):
        self.user=user
        self.password=password
        self.db=None
        self.curseur=None
        try:
            self.db = mysql.connector.connect(
            host = 'localhost',
            user = self.user,
            password = self.password,
            database ='b_marche',
            autocommit=True
        )
            self.curseur=self.db.cursor()
        except Exception as e:
            self.db=None
            self.curseur=None
            
    def login(self):
        try:
            if self.db.is_connected():
                 return True
        except Exception as e:
            return False 
    def get_curseur(self):
        return self.curseur    
    def close(self):
        self.curseur.close()





def connection():
    return True