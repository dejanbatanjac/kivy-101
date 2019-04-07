from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

# widgets are GUI elements (primitive as well non primitive), 
# but also widgets are different layouts and behaviours. 
# even the screen manager is a widget...

# we create a non primitive widget in here
class PaintWidget(Widget): 

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,1,0,1)
            rad = 30
            Ellipse(pos=(touch.x - rad/2, touch.y - rad/2), size=(rad,rad))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=rad/2 )

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

# we must have at least one app with the build method defined
class Paint(App):
    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text="Save", on_press=self.save, size=(100,50)))
        parent.add_widget(Button(text="Clear", on_press=self.clear, size=(100,50), pos=(100,0)))
        return parent

    def save(self, instance):
        self.painter.export_to_png("image.png")

        
    def clear(self, instance):
        self.painter.canvas.clear()


# run the app in here
if __name__ == '__main__':
    Paint().run()
