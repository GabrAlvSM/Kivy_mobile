from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (500,500)

class Caixas_grid(App):
    def build(self):

        layout = BoxLayout(orientation = 'vertical')
        header = BoxLayout(orientation = 'horizontal')
        body = BoxLayout(orientation='horizontal')

        body = GridLayout(cols=4)

        self.texto = Label(text='Texto')
        
        self.n1 = Button(text='1')
        self.n2 = Button(text='2')
        self.n3 = Button(text='3')
        self.n4 = Button(text='4')
        self.n5 = Button(text='5')
        self.n6 = Button(text='6')
        self.n7 = Button(text='7')
        self.n8 = Button(text='8')
        self.n9 = Button(text='9')
        self.n0 = Button(text='0')
        self.kplus = Button(text='+')
        self.kminus = Button(text='-')
        self.kmult = Button(text='*')
        self.kdiv = Button(text='/')
        self.kcomma = Button(text=',')

        self.n1.bind(on_press = self.imprimir)
        self.n2.bind(on_press = self.imprimir)
        self.n3.bind(on_press = self.imprimir)
        self.n4.bind(on_press = self.imprimir)
        self.n5.bind(on_press = self.imprimir)
        self.n6.bind(on_press = self.imprimir)
        self.n7.bind(on_press = self.imprimir)
        self.n8.bind(on_press = self.imprimir)
        self.n9.bind(on_press = self.imprimir)
        self.n0.bind(on_press = self.imprimir)
        self.kplus.bind(on_press = self.imprimir)
        self.kminus.bind(on_press = self.imprimir)
        self.kmult.bind(on_press = self.imprimir)
        self.kcomma.bind(on_press = self.imprimir)
        
        devs = Label(text='Made by Alv')

        devs.size_hint_y=(.2)

        header.add_widget(self.texto)

        body.add_widget(self.n1)
        body.add_widget(self.n2)
        body.add_widget(self.n3)
        body.add_widget(self.n4)
        body.add_widget(self.n5)
        body.add_widget(self.n6)
        body.add_widget(self.n7)
        body.add_widget(self.n8)
        body.add_widget(self.n9)
        body.add_widget(self.n0)

        layout.add_widget(header)
        layout.add_widget(body) 
        layout.add_widget(devs)    

        return layout
    
    def imprimir(self,event):
        num = int(event.text)
        print(num)
        


if __name__ == '__main__':
    Caixas_grid().run()