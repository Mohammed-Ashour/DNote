'''
-- Database 
table notes
    args 
        - name
        - tag
        - date 
        - type
Note File naming system Msc_subject_date

'''
import sqlite3
from datetime import datetime
import os 
#if not os.path.exists('notes.db'):


class Data(object):
    def __init__(self):
        try:
            self.conn = sqlite3.connect("notes.db")
            self.cursor = self.conn.cursor()
        except ConnectionError as err :
            raise err

        try:
            self.cursor.execute( '''CREATE TABLE IF NOT EXISTS my_notes
                (name text PRIMARY KEY ,  date text, tag text, path text)''')
            self.conn.commit()

        except ConnectionError as err :
            self.close_conn()
            raise err

        
         

    def create(self, name, tag, path, time):
        '''
        creates a note as a record in the my_notes table
        '''
        
        note = (name, time, tag, path)
        try:
            self.cursor.execute('INSERT INTO my_notes VALUES (?,?,?,?)', note )
            self.conn.commit()
        except ConnectionError as err:
            self.close_conn()
            raise err

    def display(self):
        '''
        display all the records in the my_notes table
        '''
        try:
            data = self.cursor.execute('SELECT * FROM my_notes' ).fetchall()
            return data
        except ConnectionError as err:
            self.close_conn()
            raise err

    def search_by_tag(self, tag, mode= "like"):
        q = ""
        if mode == "like":
            q = '''SELECT * FROM my_notes WHERE tag LIKE ?'''
        else:
            q = '''SELECT * FROM my_notes WHERE tag = ?'''
        try:
            tag = "%" + tag + "%"
            tag = (tag,)
            data = self.cursor.execute(q, tag).fetchall()
            return data
        except ConnectionError as err:
            self.close_conn()
            raise err
        
    def search_by_name(self, name, mode="like"):

        q = ""
        if mode == "like":
            q = '''SELECT * FROM my_notes WHERE name LIKE %?%'''
        else:
            q = '''SELECT * FROM my_notes WHERE name = ?'''
        try:
            name = (name,)
            data = self.cursor.execute(q, name).fetchall()
            return data
        except ConnectionError as err:
            self.close_conn()
            raise err

    def update(self, file_name, new_name = None, new_tag = None):
        
        if not new_name and not new_tag:
            print("Nothing updated!!")
            return True
        elif new_name and not new_tag:
            try:
                note = (new_name, file_name)
                self.cursor.execute('''UPDATE my_notes SET name = ? WHERE name = ? ''', note)
                self.conn.commit()
            except ConnectionError as err:
                raise err
        # elif new_tag and not new_name:
        #     #when we change the tag, we change part of the name
        #      try:
        #         #new_file_name = new_tag + "_" +  "_".join(file_name.split("_")[1:])
        #         note = (new_tag, new_name, file_name)
        #         self.cursor.execute('''UPDATE my_notes SET tag = ?, name = ? WHERE name = ? ''', note)
        #         self.conn.commit()
        #     except ConnectionError as err:
        #         raise err
        elif new_tag and new_name:
            try:
                #new_file_name = new_tag + "_" + new_name +"_".join(file_name.split("_")[2:])
                note = (new_tag, new_name, file_name)
                self.cursor.execute('''UPDATE my_notes SET tag = ?, name = ? WHERE name = ? ''', note)
                self.conn.commit()
            except ConnectionError as err:
                raise err
        else:
            raise ConnectionError

        pass
    def delete(self, file_name):
        note = (file_name,)
        try:
            self.cursor.execute('DELETE FROM my_notes WHERE name = ? ', note )
            self.conn.commit()
            print(file_name + " is Deleted from the database")
        except ConnectionError as err:
            self.close_conn()
            raise err
    def close_conn(self):
        self.conn.close() 