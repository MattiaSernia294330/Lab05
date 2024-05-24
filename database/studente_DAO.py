# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
import mysql.connector
from model.studente import Studente
class StudenteDAO:
    @staticmethod
    def handle_iscritti(corso):
        cnx = get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query="""SELECT s.*
                FROM studente s, iscrizione i
                WHERE i.codins =%s and i.matricola =s.matricola """
            cursor.execute(query, (corso,))
            for row in cursor:
                result.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))
            cursor.close()
        cnx.close()
        return result
    @staticmethod
    def handle_matricola(matricola):
        cnx = get_connection()
        result = None
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query="""SELECT s.*
                FROM studente s
                WHERE s.matricola=%s"""
            cursor.execute(query, (matricola,))
            row = cursor.fetchone()
            if row!=None:
                result=Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"])
            cursor.close()
        cnx.close()
        return result
    @staticmethod
    def handle_iscrivi(matricola, corso):
        cnx = get_connection()
        if cnx is None:
            print("errore connessione")
            return
        cursor = cnx.cursor()
        query="""INSERT INTO iscrizione
            (matricola, codins)
            values(%s, %s)"""
        cursor.execute(query, (matricola, corso))
        cnx.commit()
        cursor.close()
        cnx.close()