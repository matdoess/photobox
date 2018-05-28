from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.app import App

from functools import partial
import threading

from Helper import Helper
from SendEmail import SendEmail

import settings

import random
from shutil import copyfile
from os import listdir
from os.path import isfile, join

class GalleryScreen(Screen):
    imagepath = 'pics/mail/'

    def on_enter(self):
        self.ids.carouselid.clear_widgets()
        image_files = [f for f in listdir(self.imagepath) if isfile(join(self.imagepath, f))]
        print(image_files)
        image_files.sort(reverse=True)
        for image in image_files:
            #src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
            #image = AsyncImage(source=src, allow_stretch=True)
            #self.ids.carouselid.add_widget(image)
            #print(image_files)
            fullimage = self.imagepath + image
            print(fullimage)
            imageobject = AsyncImage(source=fullimage, allow_stretch=True)
            self.ids.carouselid.add_widget(imageobject)
