import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class Loginview(GridLayout):
	def __init__(self, **kwargs):
		super(Loginview, self).__init__(**kwargs)

		# define one row
		self.cols = 1
		self.row_force_default = True
		self.row_default_height = 100
		self.col_force_default = True
		self.col_default_width = 300

		# two row grid system
		self.top_layout = GridLayout(
			row_force_default = True,
			row_default_height = 50,
			col_force_default = True,
			col_default_width = 300
		)
		self.top_layout.cols = 2
		# self.top_layout.row_force_default = True
		# self.top_layout.row_default_height = 40
		# self.top_layout.col_force_default = True
		# self.top_layout.col_default_width = 100

		# row one 
		self.label_fn = Label(text="First Name")
		# self.text_fn = TextInput(multiline=False , size_hint_x=None, width= 200,
		# 	size_hint_y=None, height=50)
		self.text_fn = TextInput(multiline=False)
		self.top_layout.add_widget(self.label_fn)
		self.top_layout.add_widget(self.text_fn)


		# row two 
		self.label_sn = Label(text="Last Name")
		self.txt_lastname = TextInput(multiline=False)
		self.top_layout.add_widget(self.label_sn)
		self.top_layout.add_widget(self.txt_lastname)


		# add the top layout
		self.add_widget(self.top_layout)


		# add button to single colum grid
		# self.login_button = Button(text="Login", font_size=32,
		# 	size_hint_y=None, height=50, size_hint_x =None, width=200)
		self.login_button = Button(text="Login", font_size=10)
		self.add_widget(self.login_button)

		# set action to login button 
		self.login_button.bind(on_press=self.display_infomation)


	def display_infomation(self, instance):
		fn = self.text_fn.text
		ln =  self.txt_lastname.text
		self.add_widget(Label(text=f"You name is {fn} {ln}" , font_size=20))
		self.refactor_input()

	def refactor_input(self):
		self.txt_lastname = ""
		self.text_fn = ""

class MyApp(App):
	def build(self):
		return Loginview()


if __name__ == "__main__":
	app = MyApp()
	app.run()