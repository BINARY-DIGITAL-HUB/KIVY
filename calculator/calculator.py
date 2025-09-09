import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
import re
from math import pow

Window.size = (300, 480)

Builder.load_file("layout.kv")


class Calculator(App):
    def build(self):
        return CalController()


class CalController(Widget):

    # controller method for digit button
    def activate_digit(self, digit):

        screen_data = self.ids.screen.text

        if screen_data == "0" or screen_data == "ERROR":
            self.ids.screen.text = f"{digit}"
        else:
            self.ids.screen.text = f"{screen_data}{digit}"

    def activate_clears(self):
        self.ids.screen.text = "0"

    def activate_clear(self):
        digit = self.ids.screen.text
        digit_list = digit[:-1]

        if digit == "0":
            pass
        else:
            self.ids.screen.text = f"{digit_list}"

    def activate_operator(self, operation):
        screen_digit = self.ids.screen.text
        op_list = ["-", "/", "*", "+", "^"]

        if screen_digit == "0" or screen_digit in op_list or screen_digit.strip() == "ERROR":
            self.ids.screen.text = operation
        else:
            self.ids.screen.text = f"{screen_digit}{operation}"

        print(screen_digit[-1])
        if screen_digit[-1:] == ".":
            print(screen_digit[-1])
            self.ids.screen.text = f"{screen_digit}0{operation}"

    def activate_dot(self):
        screen_digit = self.ids.screen.text
        screen_digit = f"{screen_digit}."
        self.ids.screen.text = screen_digit

    def activate_percent(self):
        digit = self.ids.screen.text
        if digit != "0" or digit != "ERROR":
            eval_result = eval(digit)
            result = eval_result / 100
            self.ids.screen.text = f"{result}"

    def activate_power(self):
        self.activate_operator("^")

    def activate_equal(self):
        digit = self.ids.screen.text
        if digit == "ERROR":
            self.ids.screen.text = "0"

        try:
            result = eval(digit.replace("^", "**"))
            str_result = str(result)
            self.ids.screen.text = f'{str_result[:10]}'
            print("RESULT: ", str_result[:10])
        except Exception:
            self.ids.screen.text = f'ERROR'


if __name__ == "__main__":
    Calculator().run()
