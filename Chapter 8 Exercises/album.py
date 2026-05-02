# 8-7: Album

""" 
This program creates a function called make_album() that will store the following information about any album:
   1. Artist name
   2. Album title
   3. (Optional) Number of songs (on the album)
"""

"""
TO-DO:
    1. Function signature should be make_album(artist_name, album_name, num_of_songs=None)
    2. Store artist_name and album_name in a dictionary about the album
    3. If an argument is given for num_of_songs, this should also be stored in the dictionary
    4. Return the dictionary
    5. Create at least (4) total albums; (1) must include number of songs
    6. Print each album and the information about the album (using the dictionary that was returned)
"""

def make_album(artist_name, album_name, num_of_songs=None):
    album = {'artist name': artist_name, 'album name': album_name}
    if num_of_songs:
        album['number of songs'] = num_of_songs

    return album

# 1st album
album = make_album('lil uzi vert', 'luv is rage 2')
print(album)

# 2nd album
album = make_album('michael jackson', 'thriller')
print(album)

# 3rd album
album = make_album('sabrina carpenter', "short 'n sweet")
print(album)

# 4th album (with number of songs)
album = make_album('maroon 5', 'overexposed (deluxe)', 15)
print(album)