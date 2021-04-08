import re
import datetime
# ---------------------------------------------------------------------------------
"""import os


counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = input("What are you looking for?:> ")
thisdir = os.getcwd()
for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
    for file in f:
        filepath = os.path.join(r, file)
        if inp in file:
        	counter += 1
        	print(os.path.join(r, file))
print(f"trovati {counter} files.")"""
# ----------------------------------------------------------------------------------

def closePrompt():
    prompt = input("Would you like to close this program? (Y/n)\n>>> ")
    if prompt in ['y', 'yes']:
        exit(0)
    elif prompt in ['n', 'no']:
        closePrompt()

print("""
----------------------------------------------------------
| Put your target file in the same folder as this file   |
| This is not magic! If it doesn't work, it doesn't work |
| I am not responsible if you decide to use this for bad |
| You have to input the name of the txt file EXAMPLE:    |
| filename42069.txt                                      |
----------------------------------------------------------""")
file = input("The filename:\n>>> ")
with open(file, 'r') as text:




    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text.read())
email = str(emails).replace(',', '\n')
email = str(email).replace('\'', '')
email = str(email).replace('[', '')
email = str(email).replace(']', '')
print(email)

now = datetime.datetime.now()
now = now.strftime("%d-%m-%Y %H-%M")
now = str(now).replace(':', '_')
now = now.replace(' ', '_')
print(now)
file = file.replace('.txt', '_')
fileName = str(file + "eextract" + now)
fileName = fileName.replace('.', '_')
print(fileName)
outPrompt = input("Would you like to output to a text file? (Y/n)\n>>> ")
if outPrompt.lower() in ['y', 'yes']:
    with open(fileName, 'w') as outputFile:
        outputFile.write(email)
    print("Extracted Emails written successfully to " + fileName + ".txt")
elif outPrompt.lower() in ['n', 'no']:
    closePrompt()
