import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file("my.kv")


class MyApp(App):
	def build(self):
		return Interface()


class Interface(Widget):
	fname = ObjectProperty(None)
	sname = ObjectProperty(None)

	def activate_login(self):
		fn = self.fname.text
		sn = self.sname.text

		print(f"good morning {fn} {sn}")



if __name__ == "__main__":
	MyApp().run()