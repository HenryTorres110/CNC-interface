from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 

Builder.load_file("Page_1th.kv")

class BoxLayoutFirstPage(BoxLayout):
    slider_one_text = StringProperty("0")
    slider_two_text = StringProperty("0")
    switch_one_text_color = StringProperty("red")
    switch_two_text_color = StringProperty("red")
    switch_three_text_color = StringProperty("red")
    switch_four_text_color = StringProperty("red")

    def on_active_switch_one(self, switch):
        print("Switch_1: ", str(switch.active))
        if switch.active: 
            self.switch_one_text_color = "green"
        else: 
            self.switch_one_text_color = "red"

    def on_active_switch_two(self, switch):
        print("Switch_2: ", str(switch.active))
        if switch.active:
            self.switch_two_text_color = "green"
        else:
            self.switch_two_text_color = "red"

    def on_active_switch_three(self, switch):
        print("Switch_3: ", str(switch.active))
        if switch.active:
            self.switch_three_text_color = "green"
        else:
            self.switch_three_text_color = "red"

    def on_active_switch_four(self, switch):
        print("Switch_4: ", str(switch.active))
        if switch.active: 
            self.switch_four_text_color = "green"
        else: 
            self.switch_four_text_color = "red"

    def on_slider_value_one(self, slider, value):
        self.slider_one_text = str(int(value))
    
    def on_slider_value_two(self, slider, value):
        self.slider_two_text = str(int(value))

    def on_button_click_stop(self):
        print("Stop button clicked")

    def on_button_click_motor_off(self):
        print("Motor Off button clicked")

    def on_button_click_servo(self):
        print("Servo button clicked")

    def on_button_click_home_axis(self):
        print("Home Axis button clicked")