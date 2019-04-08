from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from functools import partial


# testing the anchor layout with box layout
class Calc(App):


    def append_text(self, b):
        try:

            if(b.text == "C"):
                self.l1.text = "0"
                return

            if(self.l1.text == "0"):
                self.l1.text = ""

            if(self.l1.text == "Err"):
                self.l1.text = ""

            if(b.text != "="):
                self.l1.text += b.text
            else:
                self.l1.text = str(eval(self.l1.text))

        except Exception as e:
            self.l1.text = "Err"
    

    # add on click for every button in gl
    def add_on_press(self, gl):
        for c in gl.children:             
            c.bind(on_press=partial(self.append_text))
            


    def build(self):

        al = AnchorLayout()

        bl = BoxLayout(orientation="vertical", size_hint=[.8, .8])
        self.l1 = Label(multilene=False, font_size=52, text="0")
        bl.add_widget(self.l1)        

        gl = GridLayout(cols=4, padding=[5,5], spacing=[3])        

        gl.add_widget(Button(text="7"))
        gl.add_widget(Button(text="8"))
        gl.add_widget(Button(text="9"))
        gl.add_widget(Button(text="*"))

        gl.add_widget(Button(text="4"))
        gl.add_widget(Button(text="5"))
        gl.add_widget(Button(text="6"))
        gl.add_widget(Button(text="-"))

        gl.add_widget(Button(text="1"))
        gl.add_widget(Button(text="2"))
        gl.add_widget(Button(text="3"))
        gl.add_widget(Button(text="/"))

        gl.add_widget(Button(text="C"))
        gl.add_widget(Button(text="0"))
        gl.add_widget(Button(text="."))
        gl.add_widget(Button(text="="))

        self.add_on_press(gl)

        bl.add_widget(gl)

        al.add_widget(bl)

        return al

    

    

# run the app in here
if __name__ == '__main__':
    Calc().run()
