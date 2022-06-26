from kivy.app import App
from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


Window.clearcolor = (224/255, 224/255, 224/255, 1)
Window.title = "Randomizer"

class Numbers(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="0", size_hint=(2, 3), pos_hint={'center_x': .5, 'center_y': .5},
                           color=(0/255, 0/255, 0/255, 1))

    def button1_pressed(self, *args):
        self.label.text = f"{str(randint(11, 99))} * {str(randint(11, 99))}"

    def button2_pressed(self, *args):
        self.label.text = f"{str(randint(101, 999))} * {str(randint(101, 999))}"

    def button3_pressed(self, *args):
        self.label.text = f"{str(randint(101, 999))} * {str(randint(11, 99))}"

    def btn_reset(self, *args):
        self.label.text = "0"

    def build(self):
        box = BoxLayout(orientation='vertical')
        btn_1 = Button(
                        text="Two-sign numbers", on_press=self.button1_pressed,
                        pos_hint={'center_x': .5, 'center_y': .5},
                        )
        btn_2 = Button(
                       text="Three-sign numbers", on_press=self.button2_pressed,
                       pos_hint={'center_x': .5, 'center_y': .4},
                       )
        btn_3 = Button(
                        text="Mixed numbers", on_press=self.button3_pressed,
                        pos_hint={'center_x': .5, 'center_y': .3},
        )
        btn_4 = Button(text="Reset", on_press=self.btn_reset,
                       pos_hint={'center_x': .5, 'center_y': .2},
                       )
        box.add_widget(self.label)
        box.add_widget(btn_1)
        box.add_widget(btn_2)
        box.add_widget(btn_3)
        box.add_widget(btn_4)


        return box


if __name__ == '__main__':
    Numbers().run()
