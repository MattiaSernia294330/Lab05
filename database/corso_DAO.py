# Add whatever it is needed to interface with the DB Table corso
import mysql.connector
from database.DB_connect import get_connection
from model.corso import Corso


class Corso_DAO:
    @staticmethod
    def dd_fill():
        cnx = get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query= """SELECT c.*
                FROM corso c"""
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], ["pd"]))
            cursor.close()
        cnx.close()
        return result
    @staticmethod
    def handle_corsi(matricola):
        cnx = get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query="""SELECT c.*
                FROM corso c, iscrizione i 
                WHERE c.codins = i.codins and i.matricola =%s"""
            cursor.execute(query, (matricola,))
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], ["pd"]))
            cursor.close()
        cnx.close()
        return result