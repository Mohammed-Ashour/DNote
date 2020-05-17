
'''
Terminal Notes App
- Make a new notes file
- Delete notes 
- Add tags
- retrieve notes using name
- search for note by date, tag, name
- connections between the notes (parent note)
'''
'''
scenario
notes create x --tag msc 
notes edit y --tag Msc
'''


'''
-- Database 
table notes
    args 
        - name
        - tag
        - author
        - date 
        - type



'''


'''
TODO
    - create the database, tables if not existed 
    - check the config file
    - install the required packages

'''
from database import Data
from note_handler import NoteHandeler

#creating the database 
my_data = Data()

x = NoteHandeler()
#x.create_note("bla", "msc")
print("-----")
x.search_by_tag(tag="bla")
#x.open_note("bla14-05-20-18-43-02", "E:\\projects\\Terminal Notes")
#x.delete_note("msc_bla_14-05-20-19-54-38", "E:\projects\Terminal Notes\\")
x.update_note("Bla_Lec3_17-05-20", new_name="Lec2", new_tag = "Bla")