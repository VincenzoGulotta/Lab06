from database.DB_connect import get_connection
from model.automobile import Automobile
from UI.alert import AlertManager

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        lista_automobili = []
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM automobile"""
            cursor.execute(query)
            for row in cursor:
                lista_automobili.append(row)
            cnx.close()
        except Exception as e:
            raise e
        return lista_automobili

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        lista_automobili = []
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM automobile WHERE modello = %s"""
            cursor.execute(query, (modello,))
            for row in cursor:
                lista_automobili.append(row)
            cnx.close()
        except Exception as e:
            raise e
        return lista_automobili

    def cerca_automobili_per_marca(self, marca) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param marca: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e marca indicato oppure None
        """
        lista_automobili = []
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM automobile WHERE marca = %s"""
            cursor.execute(query, (marca,))
            for row in cursor:
                lista_automobili.append(row)
            cnx.close()
        except Exception as e:
            raise e
        return lista_automobili
