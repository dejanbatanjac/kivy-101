from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

# widgets are GUI elements (primitive as well non primitive), 
# but also widgets are different layouts and behaviours. 
# even the screen manager is a widget...

# we create a non primitive widget in here
class PaintWidget(Widget): 
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(0,1,0,1)
            self.line = Line(points=(), width=10)

    def on_touch_down(self, touch):
    	self.line.points += (touch.x, touch.y)

# we must have at least one app with the build method defined
class Paint(App):
    def build(self):
        return PaintWidget()


# run the app in here
if __name__ == '__main__':
    Paint().run()
