import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file("layout.kv")

class MyApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return Controller()
		

class Controller(Widget):
	pass


if __name__ == "__main__":
	MyApp().run()