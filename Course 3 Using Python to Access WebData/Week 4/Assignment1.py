'''Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a
Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below, and parse the data,
extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum
 for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_22077.html (Sum ends with 91)
You do not need to save these files to your folder since your program will read the data directly
from the URL. Note: Each student will have a distinct data url for the assignment -
so only use your own data url for analysis.'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print('For sample data, enter http://py4e-data.dr-chuck.net/comments_42.html \n for actual data, enter http://py4e-data.dr-chuck.net/comments_22077.html')
url = input('Enter the link- ')

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
total=0
for tag in tags:
    locN=tag.contents[0]
    conv=float(locN)
    total=total+conv
print(total)
