from kivy.app import App
##from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

##class TutorialApp(App):
##    def build(self):
##        return Button(text='Hallo Barbara!',
##                      background_color=(0, 0, 1, 1),  # List of
##                                                      # rgba components
##                      font_size=120)
##    pass

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(text='default',
                      font_size=150,
                      size_hint_y=None,
                      height=200)
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',
                  font_size=150)
        
        f.add_widget(s)
        s.add_widget(l)
        
        b.add_widget(t)
        b.add_widget(f)
        
        t.bind(text=l.setter('text'))
        return b
##    pass

if __name__ == "__main__":
    TutorialApp().run()
