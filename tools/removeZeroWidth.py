import os
import sys

import docx
import xlrd
import lxml
#import PyPDF2 as pypdf


ZERO_WIDTH_CHARS = {
    "SPACE" : u'\u200b',
    "NON-JOINER" : u'\u200c',
    "JOINER" : u'\u200d',
    "WORD JOINER" : u'\u2060',
    "NON-BREAK SPACE" : u'\uFEFF',
}

NON_BREAK_SPACE_COUNT = 0


def printUsage():
    print("Use it as follows:")
    print()
    print("python3 removeZeroWidth <inputfile>")
    print()
    print("-inputfile is required")
    print("an outputfile.txt will be created in the same directory.")
    print()
    
def fromtxt(infile, outfile):
    
    with open(infile, mode="rt") as indata,\
         open(outfile, mode="xt") as outdata:
        linenum = 1
        for line in indata:
            for char in ZERO_WIDTH_CHARS:
                if(char == "NON-BREAK SPACE" and NON_BREAK_SPACE_COUNT < 1):
                    NON_BREAK_SPACE_COUNT += 1
                    continue
                line = line.replace(ZERO_WIDTH_CHARS[char], "")
                linenum += 1
                
            outdata.write(line)
            
        
def frompdf(infile, outdata):
    pass    
    
def fromdocx(infile, outfile):
    document = docx.Document(docx=infile)
    for para in document.paragraphs:
        print(para.text)
        break
    
def fromxlsx(infile, outdata):
    pass    
    
   
def fromxml(infile, outdata):
    pass   
    
         

if(__name__ == "__main__"):
    
    argLength = len(sys.argv)
    
    if(argLength != 2):
        print("Unexpected number of arguments. Please give correct number of ar"\
        "guments")
        printUsage()
        sys.exit(1)
    
    else:
        filext = sys.argv[1].split(".")[-1]
        
        outputfile = os.getcwd()+"/outputfile.txt"
        inputfile = sys.argv[1]
        
        if(not os.path.isfile(inputfile)):
            print("Input file not found.")
            sys.exit(1)
            
        filenumber=1
        while(os.path.isfile(outputfile)):
            outputfile = os.getcwd()+"/outputfile"+str(filenumber)+".txt"
            filenumber += 1
      
            
        if(filext == "txt"):
            fromtxt(inputfile, outputfile)
        elif(filext == "pdf"):
            frompdf(inputfile, outputfile)
        elif(filext == "docx"):
            fromdocx(inputfile, outputfile)
        elif(filext == "xlsx"):
            fromxlsx(inputfile, outputfile)
        elif(filext == "xml"):
            fromxml(inputfile, outputfile)
        
        
        

