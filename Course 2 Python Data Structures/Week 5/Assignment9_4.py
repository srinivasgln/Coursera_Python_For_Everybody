'''9.4 Write a program to read through the mbox-short.txt and
figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines
as the person who sent the mail. The program creates a Python dictionary that
maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a
maximum loop to find the most prolific committer.'''

fname = input("Enter file name: ")
try:
    #fh = open(fname)
    if len(fname) <= 1 :
        fname = "mbox-short.txt"
        fh = open(fname)
except:
    print('invalid entry!')
    quit()
count=dict()
for lin in fh:
    lin=lin.rstrip()
    if not lin.startswith('From:'):
        continue
    words=lin.split()
    email=words[1]
    count[email]=count.get(email,0)+1
# to print all the emails and the numbers print(count)
bcount=None
bemail=None
for key,no in count.items():
    if bcount is None or no>bcount:
        bcount=no
        bemail=key
print(bemail,bcount)
