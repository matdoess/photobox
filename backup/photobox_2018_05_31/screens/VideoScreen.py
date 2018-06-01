from kivy.uix.screenmanager import Screen
from kivy.app import App

from kivy.uix.label import Label

from elements import FotoImage

import settings

class TaskLabel(Label):
    pass

class VideoScreen(Screen):
    
    def on_pre_enter(self):
        app = App.get_running_app()
        fromtakevideo = app.FROMTAKEVIDEO
        app.FROMTAKEVIDEO = None
        if fromtakevideo:
            self.ids.VideoScreenContainer.clear_widgets()
            fotoimage = FotoImage.FotoImage(source='img/video_icon.png')
            self.ids.VideoScreenContainer.add_widget(fotoimage)
            
            label = TaskLabel(
            text = settings.myList['config']['text']['thanks_for_photo'],
            font_size=20
            )
            self.ids.VideoScreenContainer.add_widget(label)
        else:
            self.ids.VideoScreenContainer.clear_widgets()
            fotoimage = FotoImage.FotoImage(source='img/video_icon.png')
            self.ids.VideoScreenContainer.add_widget(fotoimage)
            
            label = TaskLabel(
            text = settings.myList['config']['text']['video_message'],
            font_size=20
            )
            self.ids.VideoScreenContainer.add_widget(label)
