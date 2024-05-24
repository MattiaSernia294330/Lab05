import flet as ft



class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_corsi = None
        self.btn_iscritti = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_corsi = ft.Dropdown(
            label="corsi",
            width=500,
            hint_text="Selezionare un corso",
            on_change= self._controller.cambio_corsi

        )
        self.txt_matricola=ft.TextField(hint_text="matricola",
                                        width=self._page.window_width * 1 / 3,
                                        on_change= self._controller.handle_matricola)
        self.txt_nome = ft.TextField(hint_text="nome",
                                     read_only=True,
                                     width=self._page.window_width * 1 / 3)
        self.txt_cognome = ft.TextField(hint_text="cognome",
                                        read_only=True,
                                        width=self._page.window_width * 1 / 3)

        corsi=self._controller.dd_fill()
        for corso in corsi:
            self.txt_corsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        # button for the "hello" reply
        self.btn_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_iscritti)
        self.btn_studente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_studente)
        self.btn_corsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handle_corsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
        row1 = ft.Row([self.txt_corsi, self.btn_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2=ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],alignment=ft.MainAxisAlignment.CENTER)
        row3 = ft.Row([self.btn_studente,self.btn_corsi,self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.add(row2)
        self._page.add(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
