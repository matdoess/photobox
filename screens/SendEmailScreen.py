from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from functools import partial

from Helper import Helper
from SendEmail import SendEmail

import settings

class SendEmailScreen(Screen):

    helper = Helper()
    mail = SendEmail()

    # Wird aufgerufen sobald sich im Textfeld etwas aendert
    # schraenkt dann die auswahl der bereits vorhandenen Mailadressen ein
    def inputChanged(self, text, *args):

        mailAddresses = self.helper.getMailAddresses()
        filteredAdrresses = []

        # loop ueber alle bereits vorhandenen Mail Adressen
        for mail in mailAddresses:
            # Wenn ein teilstueck der eingabe in der Mailadresse vorhanden wird die Adresse in das Array der gefilterten adressen hinzugefuegt
            if text in mail:
                filteredAdrresses.append(mail)

        # loescht die Auswahlliste der Emails
        self.ids.grid.clear_widgets()

        # wenn gefilterte Adressen vorhanden
        if filteredAdrresses:
            # loop ueber gefilterte Adressen um diese zur Auswahl in Scrollview anzuzeigen
            for address in filteredAdrresses:
                button = Button(text=address, size_hint_y=None, height=40, font_size=16)
                button.bind(on_press=partial(self.setTextInput, address))
                self.ids.grid.add_widget(button)


    # Wird aufgerufen sobald auf "Senden" gedrueckt wird
    def sendEmail(self, mailAddress):

        # Textfeld mit Emailadresse wieder leeren
        self.ids.emailInput.text = ""

        # prueft ob Emailadresse bereits gespeichert ist, falls nein speichern
        if self.helper.findMailAddressByMail(mailAddress) == None:
            self.helper.addMailAddress(mailAddress)

        mailtext = self.helper.getMailText()
        
        app = App.get_running_app()
        mailimage = app.MAILIMAGE
        app.MAILIMAGE = None

        # Email im Hintergrund verschicken
        mail_thread = threading.Thread(target=self.mail.send, args=(mailAddress,mailtext,mailimage))
        mail_thread.start()

        # Wieder zum Startbildschirm zuruek navigieren
        self.parent.current = 'MenuScreen'

    # Wird aufgerufen wenn Benutzer auf eine Emailadresse aus der Vorschlagsliste klickt
    # schreibt die Auswahl in das Textfeld
    def setTextInput(self, address, *args):
        self.ids.emailInput.text = address
