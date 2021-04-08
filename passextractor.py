import re


print("""
----------------------------------------------------------
| Type the absolute path to the file                     |
| I am not responsible if you decide to use this for bad |
----------------------------------------------------------""")

def closePrompt():
    prompt = input("Would you like to close this program? (Y/n)\n>>> ")
    if prompt in ['y', 'yes']:
        exit(0)
    elif prompt in ['n', 'no']:
        closePrompt()

file = input("The filepath:\n>>> ")
# /:[a-zA-Z0-9\*\$\.\?\#]+ |/g

with open(file, 'r') as text:
	
	
	
	passwords = re.findall(r"\:[a-zA-Z0-9\*\$\.\?\#]+ \|", text.read())
	pwd = str(passwords).replace(':', '')
	pwd = str(pwd).replace(' |', '')
	pwd = str(pwd).replace(',', '\n')
	pwd = str(pwd).replace('\'', '')
	pwd = str(pwd).replace('[', '')
	pwd = str(pwd).replace(']', '')
print(pwd)

file = file.replace('.txt', '_')
fileName = (file + "pextract")
outputPrompt = input("Would you like to output to a file? (Y/n)\n>>> ")
if outputPrompt in ['y', 'yes']:
	with open(fileName, 'w') as outputFile:
		outputFile.write(pwd)
	print(f"Passwords written successfully to {fileName}.txt")
elif outputPrompt in ['n', 'no']:
	closePrompt()
