from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Video'
            on_press:
                root.manager.current = 'video'
                root.manager.transition.direction = 'left'
        Button:
            text: 'Foto'
            on_press:
                root.manager.current = 'foto'
                root.manager.transition.direction = 'left'
        Button:
            text: 'Aufgabe'
            on_press:
                root.manager.current = 'task'
                root.manager.transition.direction = 'left'
        TextInput:
            text: "foobar"

<VideoScreen>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'Test label'
            size_hint_y: None
            height: self.parent.height * 0.1
            canvas.before: 
                Color: 
                    rgb: 0, 1, 0
                Rectangle: 
                    pos: self.pos 
                    size: self.size 
        Label:
            text: 'Label in der Mitte'
            canvas.before: 
                Color: 
                    rgb: 0, 0, 1
                Rectangle: 
                    pos: self.pos 
                    size: self.size 
        Button:
            text: 'Back to menu'
            size_hint_y: None
            height: self.parent.height * 0.1
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'

<FotoScreen>:
    BoxLayout:
        Button:
            text: 'Back to menu'
            size_hint_y: None
            height: self.parent.height * 0.1
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'

<TaskScreen>:
    BoxLayout:
        Button:
            text: 'Back to menu'
            size_hint_y: None
            height: self.parent.height * 0.1
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'
""")

# Declare screens
class MenuScreen(Screen):
    pass

class FotoScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

class TaskScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FotoScreen(name='foto'))
sm.add_widget(VideoScreen(name='video'))
sm.add_widget(TaskScreen(name='task'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()