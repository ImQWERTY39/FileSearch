from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import os


class MainWidgets(GridLayout):
    def findFile(path, file_name, file_ext):
        paths = ""

        for currect_path, folders, files in os.walk(path):
            for files_ in files:
                f_name, f_ext = os.path.splitext(files_)

                if((file_name == f_name and file_ext == file_ext) or (file_name == "*" and file_ext == f_ext) or
                (file_name == f_name and file_ext == ".*" or file_name == "*" and file_ext == ".*")):
                    paths += f"{currect_path}\\{f_name}{f_ext}\n"
            
        paths = paths.strip()

        if paths == "":
            paths = "No files found"
        
        return paths


    def search(self):
        path = self.ids.path.text
        file = self.ids.file.text

        if(not os.path.exists(path)):
            if "Enter a valid path" in self.ids.list.text :
                self.ids.list.text += "!"
            
            else:
                self.ids.list.text = "Enter a valid path"
        
        else:
            file_name, file_ext = os.path.splitext(file)
            
            self.ids.list.text = MainWidgets.findFile(path, file_name, file_ext)


class FileSearch(App):
    def build(self):
        self.title = "File Search"
        self.icon = "Images\\icon.png"


if __name__ == "__main__":
    FileSearch().run()