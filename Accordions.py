
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image


Builder.load_file('Accordions.kv')
# Builder.load_string(''' copy builder file text here ''')
class  AccordionsPanel(Widget):
    pass

class  accord(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return  AccordionsPanel()

if __name__ == '__main__':
    accord().run()

