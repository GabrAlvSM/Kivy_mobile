from turtle import left
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from matplotlib.pyplot import margins

Window.size = (400,800)

class Application(App):
    def build(self):

        layout = BoxLayout(orientation="vertical")
        header = BoxLayout(orientation='vertical')
        main = BoxLayout(orientation='horizontal')
        main_left = BoxLayout(orientation='vertical')
        main_right = BoxLayout(orientation='horizontal')
        main_empty = BoxLayout()

        elemento1 = Label(text='Nome')
        text_input = TextInput()
        button_save = Button(text='Salvar')
        button_left1 = Button(text='L1')
        button_left2 = Button(text='L2')
        button_right1 = Button(text='R1')
        button_right2 = Button(text='R2')

        header.add_widget(elemento1)
        header.add_widget(text_input)

        layout.add_widget(header)
        layout.add_widget(main)

        main.add_widget(main_left)
        # main.add_widget(main_empty)
        main.add_widget(main_right)

        main_left.add_widget(button_left1)
        main_left.add_widget(button_left2)

        main_right.add_widget(button_right1)
        main_right.add_widget(button_right2)

        # layout.add_widget(button_save)

        return layout
    
if __name__ == '__main__':
    Application().run()