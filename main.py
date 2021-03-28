from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
# from screen_nav import screen_helper
from lmsbot import mainfunc

class SubjectScreen(Screen):
    pass


class LoginScreen(Screen):
    pass

sn = ScreenManager()
sn.add_widget(SubjectScreen(name='menu'))
sn.add_widget(LoginScreen(name='LoginScreen'))
class AramBotApp(MDApp):

    def submit(self,one,two,three,four):
        self.one = one.text
        self.two = two.text
        self.three = three.text
        self.four = four.text

    def build(self):
        self.theme_cls.primary_palette="Amber"
        self.theme_cls.theme_style='Dark'
        screen = Screen()
        self.help_str = Builder.load_file('settings.kv')
        screen.add_widget(self.help_str)
        return screen

    def login(self, usr, pwd):
        self.usr = usr.text
        self.pwd = pwd.text
        if (len(self.pwd) < 4 or len(self.usr) < 4):
            self.help_str.get_screen('LoginScreen').ids.result.text = 'Failure\ntoo short'
        else:
            self.help_str.get_screen('LoginScreen').ids.result.text = 'Success :)'
            res = mainfunc(self.usr,self.pwd,self.one,self.two,self.three,self.four)
            if res == 1:
                self.help_str.get_screen('LoginScreen').ids.result.text ='wrong login details\ntry again'


AramBotApp().run()
