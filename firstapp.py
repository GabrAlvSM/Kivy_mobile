from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300,700)

class Programa(App):
    def build(self):

        layout = BoxLayout(orientation = 'vertical')
        cabeca = BoxLayout(orientation = 'horizontal')
        
        texto = Label(text='App', font_size='50px')
        botao1 = Button(text='opt1',font_size='50px')
        botao2 = Button(text='opt2',font_size='50px')
        botao3 = Button(text='opt3',font_size='50px')

        cabeca.add_widget(texto)
        cabeca.add_widget(botao1)
        layout.add_widget(cabeca)
        layout.add_widget(botao2)
        layout.add_widget(botao3)


        return layout

# if (Programa.botao3 == 'click'):
#     texto = Label(text='pew')

if __name__=='__main__':
    Programa().run()