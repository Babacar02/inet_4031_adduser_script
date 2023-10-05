#!/usr/bin/python2
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^\s*#', line)
        fields = line.strip().split(':') #strip any whitespace and split into 
                                         # into an array
        if match or len(fields) !=5: #checks if the length of fields is not equal to 5
                                     #if the length is not equal to 5 that means we dont have 
                                     #the correct number of elements.
            continue    #the continue here is for the For loop. so if the line
                        #starts with a # or does NOT have five fields, we skip it

        username = fields[0]
        password = fields[1]

        gecos   = "%s %s,,," % (fields[3],fields[2])

        groups  = fields[4].split(',') #the string that is in the fields[4] will will be split
                                       # by adding a comma between. 
        print( "==> Setting the password for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)  # allows us to excute shell commands
        print("==> Setting the passowrd for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)
        for group in groups: #this for loop is looping over the groups variable to print it out formatted by username,group.
            if group != '-':
                print "==> Assigning %s to the %s group..." % (username,group)
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)


if __name__ == '__main__': #remember to use double underlines here
    main()
