'''
the interface of our app
    - notes create  lec1 --tag master 
    - notes update test_x_21-05-20  --newtag msc
    - notes view lec4 --tag master [--op and]  
    - notes open lec4 --tag master   --month 5
        - view items with indexes
        -ask which one (index) you wanna open
    - notes delete lec4 --tag master --month 5
        - view items with indexes
        -ask which one (index) you wanna delete
    - notes show lec4 --bytag
        - notes show notes --bydate
        -  notes show all --bydate
'''
'''
TODO
    - add the args actions Done
    - add args help msgs Done 
    - config file integration Done

'''

import sys, getopt, argparse
from note_handler import NoteHandeler
from tabulate import tabulate
handler = NoteHandeler()
def arg_handeler(args:list, parser):
    # print(parser.parse_args(args[1:]))
    # print("####")
    # print(type(args))
    if type(args) is not list : raise AssertionError
    if args == []: return False
    if len(args) > 1:  
        p_args = parser.parse_args(args[1:])

        if p_args.command == "create":
            if p_args.name and p_args.tag:
                handler.create_note(p_args.name, p_args.tag)
            else : parser.print_help()

        elif args[1] ==  "open":
            if p_args.name:
                handler.open_note(p_args.name)
            else:
                parser.print_help()

                # run open logic 
        elif args[1] == "update":
            if p_args.name:
                if p_args.newname and p_args.newtag:
                    handler.update_note(p_args.name, p_args.newname, p_args.newtag)
                elif p_args.newtag:
                    handler.update_note(p_args.name, new_tag=p_args.newtag)
                elif p_args.newname:
                    handler.update_note(p_args.name, new_name=p_args.newname)
                else: 
                    parser.print_help()
            else:
                parser.print_help()
            

        elif args[1] ==  "delete":
            if p_args.name:
                handler.delete_note(p_args.name)
            else:
                parser.print_help()
        elif args[1] == "show":
            if p_args.name == "all":
                if p_args.bydate:
                    notes = handler.show_notes(by_date=True)
                elif p_args.byname :
                    notes = handler.show_notes(by_name=True)
                elif p_args.bytag :
                    notes = handler.show_notes(by_name=True)
                else:
                    notes = handler.show_notes()
            else:
                if p_args.bydate:
                    notes = handler.show_notes(p_args.name,by_date=True)
                elif p_args.byname :
                    notes = handler.show_notes(p_args.name, by_name=True)
                elif p_args.bytag :
                    notes = handler.show_notes(p_args.name, by_name=True)
                else:
                    notes = handler.show_notes(p_args.name)
            print(tabulate(notes, headers=["filename", "date", "tag", "path"]))

help_msg = '''

    notes.py <command> [arguments]
    options that you have in this script 
    - notes create lec1 -- tag master 
    - notes update lec2 --tag master --newtag msc
    - notes update lec2 --tag msc --newname lec3 --newtag msc
    - notes view lec4 --tag master [--op and]  
    - notes open lec4 --tag master   --month 5
        - view items with indexes
        -ask which one (index) you wanna open
    - notes delete lec4 --tag master --month 5
        - view items with indexes
        -ask which one (index) you wanna delete

    '''

def main():
    p = argparse.ArgumentParser(add_help=False, description= " notes management system", usage=help_msg)
    # p.add_argument("open")
    # p.add_argument("create")
    # p.add_argument("delete")
    # p.add_argument("edit")
    p.add_argument("command")
    p.add_argument("name")
    p.add_argument("--newname")
    p.add_argument("--tag", action="store")
    p.add_argument("--newtag", action="store")
    p.add_argument("--op", action="store")
    p.add_argument("--month", action="store")
    p.add_argument("--day", action="store")
    p.add_argument("--bytag",  action="store_true")
    p.add_argument("--bydate",  action="store_true")
    p.add_argument("--byname",  action="store_true")

    
    arg_handeler(sys.argv, p)
   # p.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,help=help_msg)

    # opts, args = getoptg.etopt(sys.argv, "hi:o:", ["help", "tag", "newtag", "month"])
    #print(sys.argv, opts, args, sys.argv == args)
    #print(p.parse_args())


main()
