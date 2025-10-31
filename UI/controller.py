import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value                      # Ricevo da View il valore inserito dell'utente
                                                                                            # in input_responsabile
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"     # Modifico in View il nome del responsabile
                                                                                            # che viene mostrato in txt._responsabile
        self._view.update()

    def mostra_auto(self, e):
        # In teoria qui devo chiamare self._view.lista_auto
        lista_auto = self._model.get_automobili()
        try:
            lista_auto = self._model.get_automobili()
            self._view.lista_auto.controls.clear()
            for item in lista_auto:
                marca = item["marca"]
                modello = item["modello"]
                anno = item["anno"]
                self._view.lista_auto.controls.append(ft.Text(f"{marca}, {modello}, {anno}"))
                self._view.update()
        except Exception as e:
            self._view.show_alert("Controlla di aver inserito un database compatibile")


    def cerca_auto_modello(self, e):
        modello = self._view.input_modello_auto.value
        try:
            lista_auto = self._model.cerca_automobili_per_modello(modello)
            self._view.lista_auto_ricerca.controls.clear()
            for item in lista_auto:
                marca = item["marca"]
                modello = item["modello"]
                anno = item["anno"]
                self._view.lista_auto_ricerca.controls.append(ft.Text(f"{marca}, {modello}, {anno}"))
            self._view.update()
        except Exception as e:
            self._view.show_alert("Controlla di aver inserito un database compatibile")

    def cerca_auto_marca(self, e):
        marca = self._view.input_marca_auto.value
        try:
            lista_auto = self._model.cerca_automobili_per_marca(marca)
            self._view.lista_auto_ricerca.controls.clear()
            for item in lista_auto:
                marca = item["marca"]
                modello = item["modello"]
                anno = item["anno"]
                self._view.lista_auto_ricerca.controls.append(ft.Text(f"{marca}, {modello}, {anno}"))
            self._view.update()
        except Exception as e:
            self._view.show_alert("Controlla di aver inserito un database compatibile")

    # Altre Funzioni Event Handler
