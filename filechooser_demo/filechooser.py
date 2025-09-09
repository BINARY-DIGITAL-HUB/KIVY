import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




class LoginWindow(Screen):
	pass

class HomeWindow(Screen):
	pass


class Home(ScreenManager):
	pass


kv = Builder.load_file("layout.kv")

class MyApp(App):
	def build(self):
		return kv



if __name__ == "__main__":
	 MyApp().run()