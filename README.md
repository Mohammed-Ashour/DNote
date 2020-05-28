# Notes Manager

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
              - notes create lec1 -- tag master 
              - notes update  Bla_Lec3_17-05-20 --newtag msc
              - notes update  Bla_Lec3_17-05-20 --newname lec3 --newtag msc
              - notes show lec4 --bytag
              - notes show notes --bydate
              - notes show all --bydate
              - notes open Bla_Lec3_17-05-20
              - notes delete Bla_Lec3_17-05-20
              - notes zip all
              - notes zip notes --tag msc
              - notes restore <folder_path>   #restores all the backed-up notes from your un-zipped backup folder 
     ```

## Installation
run
```
python setup.py build
python setup.py install
```
## License

This project is licensed under the MIT License 

