import lyricsgenius as genius

api = genius.Genius("MJkvOvNk7i8qzBkMXk5soOe6Ckyy2Ze5hrDNktljzXxk35pVjvZ1Zr3d3u-luFkW")
artist = api.search_artist('Booba')

print (artist)

# song = api.search_song('Garcimore', artist.name)

# print (song)

# artist.add_song(song)

# print (artist)

artist.save_lyrics('txt')
