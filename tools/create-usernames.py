# This script is able to create usernames that can be used for brute force attacks
# from given names
# Names can be provided from the command line or from a text file
# Assumptions: 
# 1. Usernames will only contain small alphabets with different combination of first
# and last name
# 2. Middle name is not used in the username

import sys
import os
import os.path

usernames = []
outFilename = ""

def write2file(list: unameList, str: filepath) -> int:
    ''' Write list of usernames to a txt file ''''
    try:
        with open(filepath, "w") as usernames:
            for uname in usernames:
                usernames.write(uname)
    except:
        print("Something went wrong while writing the output file.")
        return -2
    return 0
       
def createUnames(str: name) -> int:
    ''' create usernames from fullname '''
    
    fullname = name.lower().split()
    if(len(fullname) == 2):
        fname, lname = fullname[0], fullname[1]
    elif(len(fullname) == 3):
        fname, lname = fullname[0], fullname[2]
    else:
        username.append(fullname[0])
    
    username.append(fname)
    username.append(fname+lname)
    username.append(fname+lname[0])
    username.append(fname[0]+lname)
    username.append(fname+"."+lname)
    username.append(fname[0]+"."+lname)
    username.append(fname+"."+lname[0])
    username.append(lname)
    username.append(lname+fname)
    username.append(lname+"."+fname)
    username.append(lname+fname[0])
    username.append(lname+"."+fname[0])
    username.append(lname[0]+fname)
    username.append(lname[0]+"."+fname)
    
    return writeToFile(username, outFilename)
     

if(__name__ == "__main__"):
    params = list(sys.argv)
    
    outFilename = input("Enter the path to outptut file:")
    if(os.path.isfile(outFilename)):
        print("File already exists... ")
        print("Data will be over-written")
        
    if(len(params) < 3):
        raise ValueError("Insufficient paramters")
    if(params[1] == "-f"):
        filePath = params[2]
        try:
            with open(filePath, "r") as nameList:
                name = nameList.readline()
                createUnames(name)
        except:
             print("Something wrong with file at :", filePath)
    else:
        for nameIndex in range(1, len(params)):
            createUnames(sys.argv[nameIndex])
        
