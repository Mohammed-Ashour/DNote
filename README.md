# DNote (Death-Note)

![Death Note Footage](./dnote.jpg)

This a simple notes app that enables you to manage, add, delete, search and filter via your notes in your machine using your command line and your favorite editor using simple commands 

## Features
- Using a naming system that keeps your notes organized by tag and date `tag_name_date`
- Using a Sqlite database to help in searching and tracking your notes
- uses simple commands to help you do whatever you want easily 
- using a help docs
- Backup all your notes or (Filtered ones) in a zip folder **(new)**
- Restore all your backed-up notes from your un-zipped backup folder **(new)**

    ```
              notes.py <command> [arguments]
              options that you have in this script 
              - dnote create lec1 -- tag master 
              - dnote update  Bla_Lec3_17-05-20 --newtag msc
              - dnote update  Bla_Lec3_17-05-20 --newname lec3 --newtag msc
              - dnote show lec4 --bytag
              - dnote show notes --bydate
              - dnote show all --bydate
              - dnote open Bla_Lec3_17-05-20
              - dnote delete Bla_Lec3_17-05-20
              - dnote zip all
              - dnote zip notes --tag msc
              - dnote restore <folder_path>   #restores all the backed-up notes from your un-zipped backup folder 
     ```

## Installation
run
```
python setup.py build
python setup.py install
```
## License

This project is licensed under the MIT License 

