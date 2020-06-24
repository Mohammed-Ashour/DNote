
import os 
import time
import pathlib
#from note import Note
from database import Data
from datetime import datetime
import json 
from zipfile import ZipFile
import glob
data = ""
with open(str(pathlib.Path(pathlib.Path(__file__).parent.absolute(), "config").with_suffix(".json")) ) as json_file:
    data = json.load(json_file)
edit_prog = data["edit_prog"]

data_obj = Data()


'''
File naming  = tag_name_date

TODO
    - edit function DONE
    -  Re-implement delete  functionality to use the path from the database not from the user DONE
    - add intelegant search (like) if we doesn't find the file

'''
class NoteHandeler(object):
    '''
    Handles the note file and it's connection with the database
    
    '''
    def __init__(self, name="note", tag=None):
        self.name = name
        self.tag = tag
    
    def show_notes(self, name=None, by_date=False, by_name=False, by_tag=False):
        if name:
            if by_date:
                return data_obj.display(name,by_date=True)
            elif by_name:
                return data_obj.display(name,by_name=True)
            elif by_tag:
                return data_obj.display(name,by_tag=True)
            else: 
                return data_obj.display(name,by_name=True)
        else:
            if by_date:
               return data_obj.display(by_date=True)
            elif by_name:
                return data_obj.display(by_name=True)
            elif by_tag:
                return data_obj.display(by_tag=True)
            else:
                return data_obj.display(by_name=True)
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
        self.open_note(filename)
        

    # def search_by_tag(self,tag):
    #     notes = data_obj.search_by_tag(tag)
    #     for i in notes:
    #         # print(i)
    #         if self.check_if_exists(i[0], i[3]):
    #             print("Exists")
    #         else :
    #             print("Deleted!!")

    # def search_by_name(self,name):
    #     notes = data_obj.search_by_tag(name)
    #     for i in notes:
    #         print(i)
    #         if self.check_if_exists(i[0], i[3]):
    #             print("Exists")
    #         else :
    #             print("Deleted!!")

    def delete_note(self, name):
        #name here is the file name without extension 
        #print("------fd----")
        notes = data_obj.search_by_name(name,mode="exact")
        if len(notes) > 1:
            print(notes)
        elif len(notes) == 1 :
            path = notes[0][-1]
            if self.check_if_exists(name, path):
                full_path = str(pathlib.Path(path, name).with_suffix(".txt"))
                os.remove(full_path)
                data_obj.delete(name)
                print("File Deleted!!")
            else : 
                print("The file doesn't exist!!")
                return False
        else : 
            print("The file doesn't exist!!")
            return False
    def zip_notes(self, tag=None):
        now = datetime.now()
        time = now.strftime("%d-%m-%y")
        zip_file_location = pathlib.Path(os.getcwd(), "notes_"+time+".txt").with_suffix(".zip")
        notes = None
        if tag:
            notes = data_obj.search_by_tag(tag, mode="like") 
            
        else:
            notes = self.show_notes()

        with ZipFile(zip_file_location , 'w') as zip_notes:
            for i in notes:
                path = i[-1]
                name = i[0]
                if self.check_if_exists(name, path):
                    full_path =  str(pathlib.Path(path, name).with_suffix(".txt"))
                    zip_notes.write(full_path)
                else : 
                    print(path + name + "Not found!!")
                    continue
            print("Done..")

    def update_note(self, name, new_name=None, new_tag=None):
        try:
            data = data_obj.search_by_name(name, mode="exact")
            flag = len(list(data)) == True
            #print(list(data))
            name_split = name.split("_")
            #print(new_name, name_split[1])
            if new_name and (name_split[1] == new_name):
                print("You are using the same old name")
                return False
            
            # for i in data: print(i)
            if flag:
                # print("---------------")
               
                new_file_name = ""
                if new_name and not new_tag :
                    new_file_name = "_".join((name_split[0], new_name, name_split[2]))
                    if data_obj.search_by_name(new_file_name, mode="exact"):
                        print("The Name is already taken for a previous note, plz choose another name!")
                        return False
                    data_obj.update(name, new_name=new_file_name)
                elif new_tag and not new_name:
                    new_file_name = "_".join((new_tag, name_split[1], name_split[2]))
                    if data_obj.search_by_name(new_file_name, mode="exact"):
                        print("The Name is already taken for a previous note, plz choose another name!")
                        return False
                    data_obj.update(name, new_name=new_file_name, new_tag=new_tag)
                elif new_name and new_tag:
                    new_file_name = "_".join((new_tag, new_name, name_split[2]))
                    if data_obj.search_by_name(new_file_name, mode="exact"):
                        print("The Name is already taken for a previous note, plz choose another name!")
                        return False
                    data_obj.update(name, new_name=new_file_name, new_tag=new_tag)
                    # print(list(data))
                os.rename(str(pathlib.Path(list(data)[0][-1], name).with_suffix(".txt")),\
                    str(pathlib.Path(list(data)[0][-1], new_file_name).with_suffix(".txt")))
        except ConnectionError as err:
            raise err
       
    def check_if_exists(self,name, path):
        total_path = pathlib.Path(path, name).with_suffix(".txt")
        if os.path.exists(total_path):
            return True
        else:
            return False
    
    def resotre(self, folder):
        '''
        - takes a folder of already backed-up notes, 
        - parse it for txt file with the naming convention tag_name_date.txt
        - and adds it to the database

        '''
        for filename in glob.iglob(str(pathlib.Path(folder, "**", "*_*_*.txt")), recursive=True):
            filename_head_tail = os.path.split(filename)
            path = filename_head_tail[0]
            filename = filename_head_tail[1].split(".")[0]
            tag = filename.split("_")[0]
            date = filename.split("_")[-1]
            data_obj.create(filename,tag, path, date)
        


    def open_note(self, name):
        notes = data_obj.search_by_name(name,mode="exact")
        if len(notes) > 1:
            print(notes)
        elif len(notes) == 1 :
            path = notes[0][-1]
            if self.check_if_exists(name, path):
                os_string = edit_prog + " " + str(pathlib.Path(path, name).with_suffix(".txt"))
                os.system(os_string)
            else : 
                print("The file doesn't exist!!")
                return False
        else : 
                print("The file doesn't exist!!")
                return False



