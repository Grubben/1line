#!/Users/amc/.pyenv/versions/3.8.2/bin/python

import os
from sys import argv


olwd = os.getcwd()

cwd = '~/.1line'
path = cwd



os.chdir(path)

ls = os.listdir()
# To take the first element in ls: ".DS_Store"
ls.pop(0)

# A list of all the possible commands
commands = ['commands','add', 'list', 'read', 'open', 'remove']
# A list of all the words the user can't use
forbidden = ['commands', 'add', 'list', 'read', 'open','remove', 'exit', 'leave']


class Machine(object):
    def __init__(self):
        """The __init__ is really not needed this time. I want it there"""
        self.title = ""


    def index(self):
        """The first front of the program. Directs the program to go where it needs to go"""
        try: # See if the user gave a second argv. Should be impossible to go wrong but one never knows
            key = argv[1]
        except: # Hard to happen but will print this if no key-word is given
            print("No key-word given") #
        else: #
            if key == 'commands':
                self.lister(2, commands)
            if key == 'add':
                self.adding()
            elif key == 'list':
                self.lister(1)
            elif key == 'read':
                self.reader()
            elif key == 'open':
                self.open()
            elif key == 'remove':
                self.remover()
            elif key not in forbidden and key in ls:
                self.scroll(key)
            else:
                print("Unknown key-word. Try adding a new scroll.")

    def lister(self, num=2, list=ls):
        """A general function that prints items from a list with given inded"""
        for i in list:
            print(" " * num + i)


    def adding(self):
        """Make a new scroll"""
        try:
            title = argv[2]
        except:
            print("No name given. The scroll needs a title!")
        else:
            if title not in forbidden and title not in ls:
                print("A new parchment. It's title:", title)
                print("remember, to leave write 'exit' or press 'ctrl-c'")
                #self.title = title
                self.scroll(title)
            elif title in ls:
                print("A scroll with that name has already been created.")
                print("Choosing that scroll.")
                self.scroll(title)
            else:
                print("Cannot use key-word as a title of a scroll.")


    def scroll(self, var):
        """There's probably a better way but this module just opens the scroll. Exists since there are many way to arrive at this module, that come with different 'var's"""
        self.scroll = open(var, 'a')
        self.write_loop()


    def write_loop(self):
        """A loop that asks for input and writes it to the scroll"""
        line = input("> ")
        if line == 'exit':
            self.closer()
        elif line == '':
            # This should be optional or up to the user. I'm not sure myself if it's a good idea.
            self.scroll.write('\n' * 2)
            self.write_loop()
        else:
            self.scroll.write(line)
            self.scroll.write("\n")
            self.write_loop()

    def closer(self):
        """Closes the opened file"""
        self.scroll.close()
        self.lastwords()


    def reader(self):
        """Reads the specified file"""
        try:
            name = argv[2]
        except:
            print("No scroll chosen. Must be one of these:")
            self.lister()
        else:
            file = open(name, 'r+')
            #print("\n")
            print(file.read())


    def open(self):
        """
        A command to open the designated scroll using the system
        Had to use os.system() because os.subprocess wouldn't work
        """
        try:
            name = argv[2]
        except:
            # Will open the directory
            os.system("open ~/.1line")
        else:
            open = 'open '
            c = open + name
            # Will open the file
            os.system(c)

    def remover(self):
        """Command to remove a scroll. Makes sure the user wants to do this"""
        try:
            name = argv[2]
        except:
            print("One must be specified for removal")
            self.lister()
        else:
            wo = input("Are you sure you want to remove {}: ".format(name))
            #wo = input
            #wo = str(wo)
            if wo.lower() == 'y':
                remove = 'rm '
                c = remove + name
                # Will open the file
                os.system(c)
                print("Removed '{}'".format(name))
            else:
                pass


    def lastwords(self):
        print("\x1B[3m1line is all you need\x1B[23m")



# Making an instance of the class. NOT NEEDED but I want to gain practice
liner = Machine()


# the length of the argv list
larg = len(argv)

# if there is only word given, which is the script, ...
if larg == 1:
    #print("\x1B[1mThe line-by-line Program\x1B[0m")
    print("\x1B[4mThe line-by-line Program\x1B[0m")

    #print("Possible Commands:")
    print("possible actions:")
    liner.lister(3, commands)

# if there is more than word given. All the other commands basically
elif larg > 1:
    liner.index()

# Not sure if this is NEEDED but it's here so the user comes back to the same working-directory he was working on before calling 1line
os.chdir(olwd)
