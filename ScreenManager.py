from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

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
            id: 'emailInput'
            text: ""
            size_hint_y: None
            height: self.parent.height * 0.1
            pos_hint: {'x': 0.5, 'y': .9}
            on_text: root.inputChanged(self.text)

        ScrollView:
            size: self.size
            scroll_type: ['bars']
            GridLayout:
                id: grid
                size_hint_y: None
                height: self.minimum_height
                cols: 1

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

    def inputChanged(self, text, *args):
        if text:
            print(int(text))
            self.ids.grid.clear_widgets()
            for i in range(int(text)):
                button = Button(text="B_" + str(i), size_hint_y=None, height=40)
                self.ids.grid.add_widget(button)

    def on_enter(self):
        NUMBER_OF_BUTTONS = 50
        self.ids.grid.clear_widgets()
        
        for i in range(NUMBER_OF_BUTTONS):
            button = Button(text="B_" + str(i), size_hint_y=None, height=40)
            self.ids.grid.add_widget(button)

        # layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # # Make sure the height is such that there is something to scroll.
        # layout.bind(minimum_height=layout.setter('height'))
        # for i in range(100):
        #     btn = Button(text=str(i), size_hint_y=None, height=40)
        #     layout.add_widget(btn)
        # root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        # self.ids.grid.add_widget(layout)
    
    # data = [{'text': str(i), 'is_selected': False} for i in range(100)]

    # args_converter = lambda row_index, rec: {'text': rec['text'],
    #                                         'size_hint_y': None,
    #                                         'height': 25}

    # list_adapter = ListAdapter(data=data,
    #                         args_converter=args_converter,
    #                         cls=ListItemButton,
    #                         selection_mode='single',
    #                         allow_empty_selection=False)

    # list_view = ListView(adapter=list_adapter)

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
        print(sm.current)
        return sm

if __name__ == '__main__':
    TestApp().run()