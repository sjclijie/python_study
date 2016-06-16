#!/usr/bin/python
#coding=utf8
__author__ = 'Jaylee'

db = {}

def new_user():
    prompt = "login desired: "

    while True:
        name = raw_input( prompt )
        if db.has_key( name ):
            prompt = "name taken, try another: "
            continue
        break

    pwd = raw_input("password: ")

    db[name] = pwd

def old_user():
    name = raw_input("login: ")
    pwd = raw_input("password: ")

    password = db.get( name )

    if password == pwd:
        print "welcome back, ", name
    else:
        print "login incorrect"

def print_user():
    print db

def show_menu():
    pr = """
(N)ew User Login
(E)xisting User Login
(P)rint User
(Q)uit
"""
    while True:

        while True:

            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            if choice in "nepq":
                print "You choice [%s]" % choice
                break
            else:
                print "Invalid option, try again"

        if choice == 'q':
            print "Bye Bye ~~!"
            break;
        elif choice == 'n':
            new_user()
        elif choice == 'e':
            old_user()
        elif choice == 'p':
            print_user()


if __name__ == "__main__":
    show_menu()




