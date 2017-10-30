'''
Musical Track Database

You can use this code as a starting point for your application:
http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml file to be
used for this assignment. You can export your own tracks from iTunes and create a database,
 but for the database that you turn in for this assignment,
only use the Library.xml data that is provided.

'''

import xml.etree.ElementTree as ET
import sqlite3
dic=dict()
conn = sqlite3.connect('assignmentMT.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

CREATE TABLE Genre(
   id INTEGER NOT NULL PRIMARY KEY
      AUTOINCREMENT UNIQUE,
   name TEXT UNIQUE
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
genList=list()
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) :
         continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre=lookup(entry,'Genre')
    genList.append(genre)

    if name is None or artist is None or album is None :
        continue

    print('Genre Name :\t' ,genre)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre
        (name) VALUES (?)''', (genre,) )
    cur.execute('SELECT id FROM Genre WHERE name=?', (genre,))
    try:
        genre_id=cur.fetchone()[0]
    except:
        genre_id=''

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count,genre_id)
        VALUES ( ?, ?, ?, ?, ? ,?)''',( name, album_id, length, rating, count,genre_id ) )


    conn.commit()

for gn in genList:
    dic[gn]=dic.get(gn,0)+1
print(dic,'\nThe different entries in the dictionary is',len(dic),
        '\n the total sum of entries is',dic.values() )
