from kivy.app import App
from kivymd.app import MDApp
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from playsound import playsound
from kivy.utils import get_color_from_hex

from time import strftime


class ClockApp(MDApp):
    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.sw_started:
            if self.sw_seconds<=5:
                self.sw_seconds += nap

        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

        m, s = divmod(self.sw_seconds, 60)
        a=self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
                                        (int(m), int(s), int(s * 100 % 100)))
        
        if a==f"00:05.[size=40]00[/size]":
            self.sound=SoundLoader.load("sound3.wav")
            self.sound.play()

    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    ClockApp().run()
    

