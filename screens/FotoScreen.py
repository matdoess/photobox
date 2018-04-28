from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label

from time import sleep
from os import access, R_OK
from os.path import isfile

from elements import FotoImage

import settings

class FotoScreen(Screen):

    def on_pre_enter(self):
        app = App.get_running_app()
        fromtakefoto = app.FROMTAKEFOTO
        fromtaskfoto = app.FROMTASKFOTO
        self.ids.sendEmailButton.disabled = True    
        
        if fromtaskfoto:
            app.FROMTASKFOTO = False
            self.ids.ButtonTakeFoto.text = settings.myList['config']['text']['repeat_task']
        else:
            self.ids.ButtonTakeFoto.text = settings.myList['config']['text']['take_photo']

        if fromtakefoto:
            self.ids.FotoImageContainer.clear_widgets()
            fotoimage = FotoImage.FotoImage(source='img/camera_icon.png')
            self.ids.FotoImageContainer.add_widget(fotoimage)
            
            label = Label(
                text = settings.myList['config']['text']['image_is_loading'],
                font_size=20
            )
            self.ids.FotoImageContainer.add_widget(label)

        else:
            self.ids.FotoImageContainer.clear_widgets()
            fotoimage = FotoImage.FotoImage(source='img/camera_icon.png')
            self.ids.FotoImageContainer.add_widget(fotoimage)
            app.MAILIMAGE = None
        
        taskshort = app.TASK_SHORT
        tasklong = app.TASK_LONG
        if tasklong and not fromtaskfoto:
            
            boxLayout = InnerBoxLayout(
                orientation = 'vertical',
                padding = 20
            )
            
            label = Label(
                text = settings.myList['config']['text']['your_task'],
                size_hint_y = None,
                height = self.parent.height * 0.1,
                pos=(100, 100),
                font_size=20
            )
            
            self.ids.FotoImageContainer.clear_widgets()
            fotoimage = FotoImage.FotoImage(source='img/camera_icon.png')
            self.ids.FotoImageContainer.add_widget(fotoimage)
            
            tasklabel = TaskLabel(
            text = tasklong,
            font_size=32
            )

            taskstupid = Label(
            text = settings.myList['config']['text']['ready_for_photo'],
            font_size=20
            )
            
            boxLayout.add_widget(label)
            boxLayout.add_widget(tasklabel)
            boxLayout.add_widget(taskstupid)
            self.ids.FotoImageContainer.add_widget(boxLayout)
            print(app.TASK_SHORT)

            
    def on_enter(self):

        app = App.get_running_app()
        print(app.TASK_SHORT)
        taskLong = app.TASK_LONG if app.TASK_LONG != None else ""
        taskShort = app.TASK_SHORT
        fromtakefoto = app.FROMTAKEFOTO
        counter = 0
        
        if fromtakefoto:
            
            app.FROMTAKEFOTO = False
            isResizeInprogress = app.SM.get_screen('TakeFotoScreen').ThreadCheck()
            sleep(2)
            while (isResizeInprogress and counter < 15):
                print(counter)
                print(isResizeInprogress)
                counter += 1
                sleep(0.5)
                isResizeInprogress = app.SM.get_screen('TakeFotoScreen').ThreadCheck()

            thumbnailimage = app.SM.get_screen('TakeFotoScreen').res.getName()

            if isfile(thumbnailimage) and access(thumbnailimage, R_OK):
                self.ids.sendEmailButton.disabled = False   
                fotoimage = FotoImage.FotoImage(source=thumbnailimage)
            else:
                fotoimage = FotoImage(source=settings.myList['config']['images']['error_no_photo'])

            self.ids.FotoImageContainer.clear_widgets()
            self.ids.FotoImageContainer.add_widget(fotoimage)
            app.MAILIMAGE = thumbnailimage  