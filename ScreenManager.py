from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
# from kivy.uix.screenmanager.CardTransition import CardTransition

from Helper import Helper

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file("./templates/ScreenManager.kv")

# Declare screens
class MenuScreen(Screen):

    helper = Helper()

    def inputChanged(self, text, *args):

        mailAddresses = self.helper.getMailAddresses()
        filteredAdrresses = []


        for address in mailAddresses:
            if text in address:
                filteredAdrresses.append(address)

        self.ids.grid.clear_widgets()

        for mail in filteredAdrresses:
            button = Button(text=mail, size_hint_y=None, height=40, font_size=16)
            self.ids.grid.add_widget(button)

    def on_enter(self):

        mailAddresses = self.helper.getMailAddresses()

        self.ids.grid.clear_widgets()
        
        for address in mailAddresses:
            button = Button(text=address, size_hint_y=None, height=40, font_size=16)
            self.ids.grid.add_widget(button)


class FotoScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

class TaskScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=WipeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FotoScreen(name='foto'))
sm.add_widget(VideoScreen(name='video'))
sm.add_widget(TaskScreen(name='task'))


class ScreenManagerApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    screenManagerApp = ScreenManagerApp()
    screenManagerApp.run()