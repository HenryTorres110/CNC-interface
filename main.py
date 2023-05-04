from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for ii in range(0, 100):
            b = Button(text=str(ii), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


#class GridLayoutExample(GridLayout):
    #pass
class BoxLayoutLogIn(BoxLayout):
    pass

class BoxLayout0thPage(BoxLayout):
    pass

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




class BoxLayoutExample(BoxLayout):
    quantity = StringProperty(str(0))
    total = 0
    status = StringProperty("Stopped")
    status_color = StringProperty("red")
    slider_value = StringProperty(str(0))
    slider_status = BooleanProperty(True)
    text_input_str = StringProperty("# Counts")

    def on_button_click_add(self):
        self.total += 1
        self.quantity= str(self.total)

    def on_button_click_minus(self):
        if self.total > 0:
            self.total -= 1
            self.quantity= str(self.total)

    def on_toggle_button(self, toggle_button):
        #print("Toggle State: ", toggle_button.state)
        if toggle_button.state == "normal":
            toggle_button.text = "OFF"
            self.status = "Stopped"
            self.status_color = "red"
            self.slider_status = True
        else:
            toggle_button.text = "ON"
            self.status = "Running"
            self.status_color = "green"
            self.slider_status = False
        print(self.slider_status)

    def on_slider_value(self, widget, value):
        self.slider_value = str(int(value))
        # print(self.slider_value)

    def on_text_validate(self, text_input):
        self.text_input_str = text_input.text



class AnchorLayoutExample(AnchorLayout):
    pass


class CNC_MACHINEApp(App):
    pass


CNC_MACHINEApp().run()




