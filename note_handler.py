
import os 
import time
import pathlib
#from note import Note
from database import Data
from datetime import datetime

data_obj = Data('notes')


'''
File naming  = tag_name_date

'''
class NoteHandeler(object):
    '''
    Handles the note file and it's connection with the database
    
    '''
    def __init__(self, name="note", tag=None):
        self.name = name
        self.tag = tag
    
    def create_note(self, name, tag):
        #new_note = Note(name, tag)
        now = datetime.now()
        time = now.strftime("%d-%m-%y-%H-%M-%S")
        filename = tag + "_" + name + "_" + time
        with open(filename+".txt", "w") as f:
            f.write(str(time))
        path = os.getcwd()
        data_obj.create(filename, tag, path, time)
        data_obj.display()
        

    def search_by_tag(self,tag):
        notes = data_obj.search_by_tag(tag)
        for i in notes:
            print(i)
            if self.check_if_exists(i[0], i[3]):
                print("Exists")
            else :
                print("Deleted!!")

    def search_by_name(self,name):
        notes = data_obj.search_by_tag(name)
        for i in notes:
            print(i)
            if self.check_if_exists(i[0], i[3]):
                print("Exists")
            else :
                print("Deleted!!")

    def delete_note(self, name, path):
        print("------fd----")
        if self.check_if_exists(name, path):
            full_path = str(pathlib.Path(path, name).with_suffix(".txt"))
            os.remove(full_path)
            data_obj.delete(name)
            print("File Deleted!!")
        else : 
            print("The file doesn't exist!!")
            return False
        
    def edit_note(self, parameter_list):
        pass
    
    def check_if_exists(self,name, path):
        total_path = pathlib.Path(path, name).with_suffix(".txt")
        print(">>")
        print(total_path)
        if os.path.exists(total_path):
            return True
        else:
            return False

    def open_note(self, name, path):
        if self.check_if_exists(name, path):
            os_string = "notepad.exe " + str(pathlib.Path(path, name).with_suffix(".txt"))
            os.system(os_string)
        else : 
            print("The file doesn't exist!!")
            return False
            

    pass


