'''7.1 Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''

name=input('Enter the name of the file you would like to open:')
try:
    handl=open(name)
except:
    print('Not valid entry!')
    quit()

for l1 in handl:
    l1=l1.rstrip()
    print(l1.upper())
