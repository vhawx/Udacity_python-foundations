##Built in functions

##x = [6, 4, "KEY", 1, 2, "LOCK", 7]
##sliceObj = slice(2, 6, 3) #these are indexies
##print(x[sliceObj])



##Profanity Editor
##Profanity link is now dead

#1. read text file
import urllib.request

def read_text():
    quotes = open(r"C:\Users\vhawxhurst\AppData\Local\Programs\Python\Python36\movie_quotes.txt")
    fileContents = quotes.read()
    print(fileContents)
    quotes.close()
    check_profanity(fileContents)
    #2. check text for curse words

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("Could not scan the document properly")

read_text()




