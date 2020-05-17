
import os 
import time
import pathlib
#from note import Note
from database import Data
from datetime import datetime

data_obj = Data()


'''
File naming  = tag_name_date

TODO
    - edit function

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
        time = now.strftime("%d-%m-%y")
        #need to check if it's already exists in the database
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
        
    def update_note(self, name, new_name=None, new_tag=None):
        try:
            data = data_obj.search_by_name(name, mode="strict")
            flag = len(list(data)) == True
            print(list(data))
            name_split = name.split("_")
            print(new_name, name_split[1])
            if new_name and (name_split[1] == new_name):
                print("You are using the same old name")
                return False
            
            for i in data: print(i)
            if flag:
                print("---------------")
               
                new_file_name = ""
                if new_name and not new_tag :
                    new_file_name = "_".join((name_split[0], new_name, name_split[2]))
                    if data_obj.search_by_name(new_file_name, mode="strict"):
                        print("The Name is already taken for a previous note, plz choose another name!")
                        return False
                    data_obj.update(name, new_name=new_file_name)
                elif new_tag and not new_name:
                    new_file_name = "_".join((new_tag, name_split[1], name_split[2]))
                    if data_obj.search_by_name(new_file_name, mode="strict"):
                        print("The Name is already taken for a previous note, plz choose another name!")
                        return False
                    data_obj.update(name, new_name=new_file_name, new_tag=new_tag)
                elif new_name and new_tag:
                    new_file_name = "_".join((new_tag, new_name, name_split[2]))
                    if data_obj.search_by_name(new_file_name, mode="strict"):
                        print("The Name is already taken for a previous note, plz choose another name!")
                        return False
                    data_obj.update(name, new_name=new_file_name, new_tag=new_tag)
                    print(list(data))
                os.rename(str(pathlib.Path(list(data)[0][-1], name).with_suffix(".txt")),\
                    str(pathlib.Path(list(data)[0][-1], new_file_name).with_suffix(".txt")))
        except ConnectionError as err:
            raise err
       
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
            



