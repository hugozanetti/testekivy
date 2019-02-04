from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Tela(GridLayout):
    pass



class LogarApp(App):
    def build(self):
        return Tela()


if __name__ == "__main__":
    LogarApp().run()