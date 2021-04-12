import re
import datetime
import getopt, sys

# Removes the first option (the file name)
argumentList = sys.argv[1:]

# Options
options = "hi:o:"

# Long Options
long_options = ["Help", "Input =", "Output ="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("Usage: python3 unsheathe.py -[h,i] -[o]\n-h  Displays this help message\n-i specifies input file path\n-o specifies output file path")
             
        elif currentArgument in ("-i", "--Input"):
            print ("Displaying file_name:", sys.argv[0])
             
        elif currentArgument in ("-o", "--Output"):
            print (("Outputting to output file: (% s)") % (currentValue))

except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

inputFile = sys.argv[2]

outputFile1 = sys.argv[4]


print("""
----------------------------------------------------------
| Put your target file in the same folder as this file   |
| This is not magic! If it doesn't work, it doesn't work |
| I am not responsible if you decide to use this for bad |
| You have to input the name of the txt file EXAMPLE:    |
| filename42069.txt                                      |
----------------------------------------------------------""")
with open(inputFile, 'r') as text:




    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text.read())
email = str(emails).replace(',', '\n')
email = str(email).replace('\'', '')
email = str(email).replace('[', '')
email = str(email).replace(']', '')
print(email)

with open(outputFile1, 'w') as outputFile:
    outputFile.write(email)
print("Extracted Emails written successfully to " + outputFile1)


