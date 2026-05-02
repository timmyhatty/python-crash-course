# 8-8: Users albums

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
    5. Create a while loop that allows the user to enter the artist name, album title, and (optional) number of songs
        - Make sure there is a way to break out of the loop
    6. Print each album and the information about the album (using the dictionary that was returned)
"""

def make_album(artist_name, album_name, num_of_songs=None):
    album = {'artist name': artist_name, 'album name': album_name}
    if num_of_songs:
        album['number of songs'] = num_of_songs

    return album

QUIT = "/"
print('User Albums')
print('-----------')
print("Enter '/' at any time to quit")

while True:
    print()
    user_artist_name = input("Enter the artist's name: ")
    if user_artist_name == QUIT:
        break
    user_artist_album = input("Enter the name of the album: ")
    if user_artist_album == QUIT:
        break
    num_of_songs = input("Enter the number of songs (or press enter to skip): ")
    if num_of_songs == QUIT:
        break
    
    if num_of_songs:
        album = make_album(user_artist_name, user_artist_album, num_of_songs)
        print(album)
    else:
        album = make_album(user_artist_name, user_artist_album)
        print(album)
    