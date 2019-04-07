from kivy.app import App
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
        return PaintWidget()


# run the app in here
if __name__ == '__main__':
    Paint().run()
