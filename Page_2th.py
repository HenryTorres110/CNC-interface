from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 

Builder.load_file("Page_2th.kv")

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
