from kivy.uix.screenmanager import Screen
from kivy.app import App

class MenuScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        app.TASK_LONG = None
        app.TASK_SHORT = None