'''Extracting Data from XML

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from
that URL using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and the other is the
actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_22079.xml (Sum ends with 13)
You do not need to save these files to your folder since your program will
read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment -
so only use your own data url for analysis.'''

#sample Data :http://py4e-data.dr-chuck.net/comments_42.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = 'http://py4e-data.dr-chuck.net/comments_22079.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
#results = tree.findall('comments/comment')
x=list();a=list()
y=list();
for item in tree.findall('comments/comment'):
    x.append(int(item.find('count').text))
    a.append(item.find('name').text)
    #print('Count value is',item.find('count').text)
print('the total sum by method one is', sum(x))

print('============')
print('method 2 \n')
for item in tree.findall('.//count'):
    y.append(int(item.text))
    #print('Count value is',item.text)
print('the total sum by method two is \n', sum(y))
#print(sum(x),sum(y))
print('--------------------------')
print('The list of names found are', a)
