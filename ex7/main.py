from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


# testing the anchor layout with box layout
class Login(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(col=1, orientation="vertical", size_hint=[0.5, 0.4])
        bl.add_widget(TextInput(text="i1"))
        bl.add_widget(Button(text ="b1"))
        bl.add_widget(Button(text ="b2"))
        al.add_widget(bl)
        return al
    

# run the app in here
if __name__ == '__main__':
    Login().run()
