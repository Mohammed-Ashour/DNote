'''
the interface of our app
    - notes create lec1 --tag master 
    - notes edit lec2 --tag master --newtag msc
    - notes view lec4 --tag master [--op and]  
    - notes open lec4 --tag master   --month 5
        - view items with indexes
        -ask which one (index) you wanna open
    - notes delete lec4 --tag master --month 5
        - view items with indexes
        -ask which one (index) you wanna delete
'''
'''
TODO
    - add the args actions
    - add args help msgs
    - config file integration
    


'''

import sys, getopt, argparse

def arg_handeler(args:list):
    if args is not list : raise AssertionError
    if args == []: return False
    if len(args) > 0:
        if args[1] == "create":
                # run the create logic
                pass
        elif args[1] ==  "open":
                # run open logic 
                pass
        elif args[1] == "edit":
            pass

        elif args[1] ==  "delete":
            pass

            

def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("open")
    p.add_argument("create")
    p.add_argument("delete")
    p.add_argument("edit")
    p.add_argument("--tag")
    p.add_argument("--newtag")
    p.add_argument("--op")
    p.add_argument("--month")
    p.add_argument("--day")
    help_msg = '''
    options that you have in this script 
    - notes create lec1 --tag master 
    - notes edit lec2 --tag master --newtag msc
    - notes view lec4 --tag master [--op and]  
    - notes open lec4 --tag master   --month 5
        - view items with indexes
        -ask which one (index) you wanna open
    - notes delete lec4 --tag master --month 5
        - view items with indexes
        -ask which one (index) you wanna delete

    '''
    p.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,help=help_msg)

    opts, args = getopt.getopt(sys.argv, "hi:o:", ["help", "tag", "newtag", "month"])
    print(sys.argv, opts, args, sys.argv == args)
    print(p.parse_args())


main()
# from prompt_toolkit import prompt

# if __name__ == '__main__':
        
#     answer = prompt('Give me some input: ')
#     print('You said: %s' % answer)