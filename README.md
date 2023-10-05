# inet_4031_adduser_script
Python Script for Adding Users/Groups to a System

## Description Section: 

This Python script is designed to read user/group data from an input file, read it line by line and
then adds the user to the system. 

imports are important because they allow us to access functions from different libraries. Without importing "re" or "sys" we would get an error. 
The # in the input file is just a comment and our code will look at that line and won't read it because it starts with a hashtag. 
Regex or regular expression is used to locate or validate specific strings or patterns of text in a sentence. 


## Operation Selection: 

## Input File Specification

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

example:
babacar03:mypass:Dia:Babacar: admins, reviewers 

## Running the Script

1) Before running make sure that the script file is executable which it should be already.
     type >>> $ chmod a+x create-users.py
2) The command to run the file:
   
      "sudo ./create-users.py < create-users.input"
   or: 
      "cat create-users.input | sudo ./create-users.py"

4) This file is using version python2.
   
