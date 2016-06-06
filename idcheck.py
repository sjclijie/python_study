#!/usr/bin/python
#encoding=utf8

import string

alphas = string.letters + "_"
nums = string.digits

myInput = raw_input("Identifier to test? ")

if len(myInput) > 1:

    if myInput[0] not in alphas:
        print  '''Invalid: first symbol must be alphabetic'''

    else:

        for otherChar in myInput[1:]:

            if otherChar not in alphas + nums:

                print """Invalid: remaining symbols must be alphanumeric"""
                break

        else:
            print """okay as an identifier"""




