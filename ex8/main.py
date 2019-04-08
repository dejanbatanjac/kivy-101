from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.uix.anchorlayout import AnchorLayout


# testing the anchor layout with box layout
class Login(App):
    def build(self):
        al = AnchorLayout()

        bl = BoxLayout(orientation="vertical", size_hint=[.8, .8])
        bl.add_widget(TextInput())        

        gl = GridLayout(cols=4, padding=[5,5], spacing=[3])        

        gl.add_widget(Button(text="7"))
        gl.add_widget(Button(text="8"))
        gl.add_widget(Button(text="9"))
        gl.add_widget(Button(text="x"))

        gl.add_widget(Button(text="4"))
        gl.add_widget(Button(text="5"))
        gl.add_widget(Button(text="6"))
        gl.add_widget(Button(text="-"))

        gl.add_widget(Button(text="1"))
        gl.add_widget(Button(text="2"))
        gl.add_widget(Button(text="3"))
        gl.add_widget(Button(text="+"))

        gl.add_widget(Widget()) # empty widget
        gl.add_widget(Button(text="0"))
        gl.add_widget(Button(text="."))
        gl.add_widget(Button(text="="))

        bl.add_widget(gl)

        al.add_widget(bl)

        return al
    

# run the app in here
if __name__ == '__main__':
    Login().run()
