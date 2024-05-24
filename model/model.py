from database.corso_DAO import Corso_DAO
from database.studente_DAO import StudenteDAO
class Model:
    def __init__(self):
        pass
    def dd_fill(self):
        return Corso_DAO().dd_fill()
    def handle_iscritti(self, corso):
        return StudenteDAO().handle_iscritti(corso)
    def handle_matricola(self, matricola):
        return StudenteDAO().handle_matricola(matricola)
    def handle_corsi(self,matricola):
        return Corso_DAO().handle_corsi(matricola)
    def handle_iscrivi(self, matricola, corso):
        return StudenteDAO().handle_iscrivi(matricola, corso)
