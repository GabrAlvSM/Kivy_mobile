from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (500,700)

class Caixas(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')
        cabeca = BoxLayout(orientation='horizontal')
        footer = BoxLayout(orientation='horizontal')

        cabeca.size_hint= (1, .4)
        footer.size_hint= (1.0,0.3)

        cabeca_button1= Button(text='btn1')
        switch1 = Switch()
        button2= Button(text='btn2')
        slider1 = Slider()
        # button2.size_hint= (1.0,0.2)
        button3= Button(text='btn3', background_color=(1,.1,.1,1))
        button4= Button(text='btn4', background_color=(.2,1,0.2,1))
        # button4.size_hint= (1.0,0.3)
        
        cabeca.add_widget(cabeca_button1)
        cabeca.add_widget(switch1)
        
        layout.add_widget(cabeca)
        layout.add_widget(slider1)
        layout.add_widget(button2)
        
        footer.add_widget(button3)
        footer.add_widget(button4)
        
        layout.add_widget(footer)
        return layout
    
if __name__ == '__main__':
    Caixas().run()