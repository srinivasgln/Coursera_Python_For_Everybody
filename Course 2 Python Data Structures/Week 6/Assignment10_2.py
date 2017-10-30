'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution
by hour of the day for each of the messages. You can pull the hour out from the 'From '
line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour,
print out the counts, sorted by hour as shown below.'''

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
    if not lin.startswith('From '):
        continue
    words=lin.split()
    time=words[5]
    hr=time.split(':')
    hour=hr[0]
    count[hour]=count.get(hour,0)+1
# to print all the emails and the numbers print(count)
lst=list()
for key,val in count.items():
    tup=(key,val)
    lst.append(tup)
lst=sorted(lst)
for key,val in lst:
    print(key,val)
