from threading import Thread
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import os


class MainWidgets(GridLayout):
    paths = ""

    def findFile(self, path, file_name, file_ext):
        self.ids.list.text = ""

        for currect_path, folders, files in os.walk(path):
            for files_ in files:
                f_name, f_ext = os.path.splitext(files_)

                if((file_name == f_name and file_ext == file_ext) or (file_name == "*" and file_ext == f_ext) or
                (file_name == f_name and file_ext == ".*" or file_name == "*" and file_ext == ".*")):
                    self.ids.list.text += f"{currect_path}\\{f_name}{f_ext}\n"

        if self.ids.list.text == "":
            self.ids.list.text = "No files found" 


    def search(self):
        path = self.ids.path.text
        file = self.ids.file.text

        self.ids.list.text = ""

        if(not os.path.exists(path)):
            if "Enter a valid path" in self.ids.list.text :
                self.ids.list.text += "!"
            
            else:
                self.ids.list.text = "Enter a valid path"
        
        else:
            self.ids.list.text = "Searching..."
            file_name, file_ext = os.path.splitext(file)
            
            t = Thread(target = MainWidgets.findFile, args = (self, path, file_name, file_ext))
            t.start()

            self.ids.list.text = MainWidgets.paths


class FileSearch(App):
    def build(self):
        self.title = "File Search"
        self.icon = "Images\\icon.png"

    def on_stop(self):
        os._exit(0)


if __name__ == "__main__":
    FileSearch().run()