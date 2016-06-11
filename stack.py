#!/usr/bin/python 
#encoding=utf8

stack = []

def pushit():
    stack.append( raw_input("Enter New String:").strip() )


def popit():
    if len( stack ) == 0:
        print "Connot pop from an empty stack!"
    else:
        print "Remvoe [", stack.pop() ,"]"


def viewstack():
    print stack


CMDs = {'u':pushit, 'o':popit, 'v':viewstack}

def showmen():
    pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter Choice:"""

    while True:

        while True:


            try:
                choich = raw_input(pr).strip()[0].lower()
            except ( EOFError, KeyboardInterrupt, IndexError ):
                choich = "q"


            if choich not in 'uovq':
                print "Invalid option, try again."
            else:
                print "\n You picked: [%s]" % choich
                break

        if choich == 'q':
            break;

        CMDs[choich]()



if __name__ == "__main__":
    showmen()

