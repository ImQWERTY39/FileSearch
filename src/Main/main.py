from Functions.Miscellaneous import *
from Functions.SearchFiles import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class MainWidgets(GridLayout):
    pass


class FileSearch(App):
    def build(self):
        self.title = "File Search"
        self.icon = "Images\\icon.png"


if __name__ == "__main__":
    FileSearch().run()