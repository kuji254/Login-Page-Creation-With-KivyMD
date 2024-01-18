from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.size = (310, 580)

class Slope(MDApp):
    def build(self):
        screen_manger = ScreenManager()
        screen_manger.add_widget(Builder.load_file("main.kv"))
        screen_manger.add_widget(Builder.load_file("login.kv"))
        screen_manger.add_widget(Builder.load_file("signup.kv"))
        return screen_manger

Slope().run()
