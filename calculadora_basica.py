from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (500,500)

class Caixas_grid(App):
    def build(self):
    
        layout = BoxLayout(orientation = 'vertical')
        header = BoxLayout(orientation = 'horizontal')
        body = BoxLayout(orientation = 'horizontal')
        body_num = BoxLayout(orientation='horizontal')
        body_ops = BoxLayout(orientation = 'vertical')

        # body_num.size_hint = (1.0, 0.8)
        body_ops.size_hint = (0.3, 1)


        body_num = GridLayout(cols=3)


        self.display = Label(text='', font_size='35px')
        
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
        self.kdot = Button(text='.')

        self.kres = Button(text='=')
        self.kres.size_hint = (1.0, 0.3)

        self.zerar = Button(text='C')
        self.zerar.size_hint = (1.0, 0.2)

        self.zerar.bind(on_press = self.limpar)

        self.n1.bind(on_press = self.armazenar)
        self.n2.bind(on_press = self.armazenar)
        self.n3.bind(on_press = self.armazenar)
        self.n4.bind(on_press = self.armazenar)
        self.n5.bind(on_press = self.armazenar)
        self.n6.bind(on_press = self.armazenar)
        self.n7.bind(on_press = self.armazenar)
        self.n8.bind(on_press = self.armazenar)
        self.n9.bind(on_press = self.armazenar)
        self.n0.bind(on_press = self.armazenar)

        self.kdiv.bind(on_press = self.armazenar)
        self.kmult.bind(on_press = self.armazenar)
        self.kminus.bind(on_press = self.armazenar)
        self.kplus.bind(on_press = self.armazenar)

        self.kdot.bind(on_press = self.armazenar)

        self.kres.bind(on_press = self.calcular)
        
        devs = Label(text='Made by Alv')
        devs.size_hint_y=(.2)



        header.add_widget(self.display)

        body_num.add_widget(self.n7)
        body_num.add_widget(self.n8)
        body_num.add_widget(self.n9)
        body_num.add_widget(self.n4)
        body_num.add_widget(self.n5)
        body_num.add_widget(self.n6)
        body_num.add_widget(self.n1)
        body_num.add_widget(self.n2)
        body_num.add_widget(self.n3)
        body_num.add_widget(self.n0)
        
        body_ops.add_widget(self.kdiv)
        body_ops.add_widget(self.kmult)
        body_ops.add_widget(self.kminus)
        body_ops.add_widget(self.kplus)

        body.add_widget(body_num)
        body.add_widget(body_ops)

        layout.add_widget(header)
        layout.add_widget(self.zerar)
        layout.add_widget(body) 
        layout.add_widget(self.kres)
        layout.add_widget(devs)    

        return layout
    
    def imprimir(self,event):
        self.display.text = event.text
        print(event.text)

    def limpar(self,event):
        self.display.text = ''

    def armazenar(self,event):
        self.display.text += event.text


    def calcular(self,event):
        
        if '+' in self.display.text:
            num = self.display.text.split('+')
            
            res = float(num[0]) + float(num[1])  
            
        elif ('-' in self.display.text):
            num = self.display.text.split('-')

            res = float(num[0]) - float(num[1])
            

        elif ('*' in self.display.text):
            num = self.display.text.split('*')

            res = float(num[0]) * float(num[1])

        elif ('/' in self.display.text):
            num = self.display.text.split('/')

            res = float(num[0]) / float(num[1])

        self.display.text = str(res)

        
if __name__ == '__main__':
    Caixas_grid().run()
