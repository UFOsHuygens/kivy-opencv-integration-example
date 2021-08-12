from kivy.app import App
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.floatlayout import FloatLayout
import cv2

kv = '''
MyFloatLayout:
    Image
        id: img1
'''

class MyFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.cap = cv2.VideoCapture(0)
        ret, img = self.cap.read()
        Clock.schedule_interval(self.update, 1.0/30.0)
        
    def update(self, dt):
        ret, img = self.cap.read()
         
        buf1 = cv2.flip(img, 0)
        buf = buf1.tostring()
         
        texture1 = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
         
        self.ids.img1.texture = texture1

class Kivy(App):
    def build(self):
        return Builder.load_string(kv)


Kivy().run()
