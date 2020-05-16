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
            conn = sqlite3.connect("notes.db")
            self.cursor = conn.cursor()
        except err as ConnectionError:
            raise err

        try:
            self.cursor.execute( '''CREATE TABLE IF NOT EXISTS my_notes
                (name text PRIMARY KEY ,  date text, tag text, path text)''')
            conn.commit()

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
            conn.commit()
        except ConnectionError as err:
            self.close_conn()
            raise err

    def display(self):
        '''
        display all the records in the my_notes table
        '''
        try:
            data = self.cursor.execute('SELECT * FROM my_notes' )
            return data
        except ConnectionError as err:
            self.close_conn()
            raise err

    def search_by_tag(self, tag):
        try:
            tag = "%" + tag + "%"
            tag = (tag,)
            data = self.cursor.execute('''SELECT * FROM my_notes WHERE tag LIKE ?''', tag)
            return data
        except ConnectionError as err:
            self.close_conn()
            raise err
        
    def search_by_name(self, name):
        try:
            name = "%" + name +"%"
            name = (name,)
            data = self.cursor.execute('''SELECT * FROM my_notes WHERE name LIKE %?%''', name)
            return data
        except ConnectionError as err:
            self.close_conn()
            raise err

    def delete(self, file_name):
        note = (file_name,)
        try:
            self.cursor.execute('DELETE FROM my_notes WHERE name = ? ', note )
            conn.commit()
            print(file_name + " is Deleted from the database")
        except ConnectionError as err:
            self.close_conn()
            raise err
    def close_conn(self):
        conn.close() 