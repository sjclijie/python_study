#!/usr/bin/python

queue = []

def endQ():
    queue.append( raw_input("Enter new string:").strip() )

def deQ():
    if len( queue ) == 0:
        print "Connot pop from an empty queue."
    else:
        print "Removed [ " + queue.pop(0) +" ]"


def view():
    print queue

CMDs = { "e":endQ, "d":deQ, "v":view  }


def showmenu():
    pr = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit
"""
    
    while True:

        while True:

            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = "q"

            if choice not in "edvq":
                print "Invalid option, try again."
            else:
                print "\nYou packed: [%s]" % choice
                break

        if choice == 'q':
            break
        
        CMDs[choice]()




if __name__ == "__main__":
    showmenu()





    












