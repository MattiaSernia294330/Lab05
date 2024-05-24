import flet as ft
from model.studente import Studente


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._corso=None
        self._matricola=None

    def handle_iscritti(self, e):
        if self._corso==None:
            self._view.create_alert("Selezionare un corso")
            return
        self._view.txt_result.controls.clear()
        studenti= self._model.handle_iscritti(self._corso)
        self._view.txt_result.controls.append(ft.Text(f"ci sono {len(studenti)} studenti iscritti al corso:"))
        for studente in studenti:
            self._view.txt_result.controls.append(ft.Text(studente))
        self._view.update_page()
    def handle_matricola(self,e):
        self._matricola=e.control.value
    def handle_studente(self, e):
        if self._matricola==None:
            self._view.create_alert("Selezionare un  numero di matricola")
        studente=self._model.handle_matricola(self._matricola)
        if not isinstance(studente,Studente):
            self._view.create_alert("lo studente non esiste")
            return
        self._view.txt_nome.value=studente.nome
        self._view.txt_cognome.value = studente.cognome
        self._view.update_page()

    def handle_corsi(self, e):
        if self._matricola==None:
            self._view.create_alert("Selezionare un  numero di matricola")
        result=self._model.handle_corsi(self._matricola)
        self._view.txt_result.controls.clear()
        if len(result)==0:
            self._view.create_alert("matricola non esistente")
            return
        for corso in result:
            self._view.txt_result.controls.append(ft.Text(corso))
        self._view.update_page()
    def handle_iscrivi(self,e):
        if self._matricola==None:
            self._view.create_alert("Selezionare un  numero di matricola")
            return
        if self._corso==None:
            self._view.create_alert("Selezionare un corso")
            return
        listacorsi = self._model.handle_corsi(self._matricola)
        self._view.txt_result.controls.clear()
        if len(listacorsi) == 0:
            self._view.create_alert("matricola non esistente")
            return
        for corso in listacorsi:
            if corso.codins==self._corso:
                self._view.create_alert("studente gia iscritto al corso")
        self._model.handle_iscrivi(self._matricola, self._corso)

        pass
    def dd_fill(self):
       return self._model.dd_fill()
    def cambio_corsi(self,e):
        lista=e.control.value.split(" ")
        alfa=lista[len(lista)-1].strip("()")
        self._corso=alfa
