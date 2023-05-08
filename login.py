from kivy.lang import Builder
from kivymd.app import MDApp

class LoginPage(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file("login.kv")
    
    def logger(self):
        print("You just clicked Log In button")

    def registration(self):
        print("Registration Button clicked")
    

LoginPage().run()