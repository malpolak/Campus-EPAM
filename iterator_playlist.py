class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title):
        self.songs.append(title)

    def __iter__(self):
        return PlaylistIterator(self)


class PlaylistIterator:
    def __init__(self, playlist):
        self.songs = playlist.songs
        self._cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor < len(self.songs):
            song = self.songs[self._cursor]
            self._cursor += 1
            print(self._cursor)
            return song

        raise StopIteration


playlist = Playlist()

playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
playlist.add_song("Song D")
playlist.add_song("Song E")

for song in playlist:
    print(song)

#way of working

iterator = iter(playlist)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

"""
# StopIteration was raised because the iterator reached the end of the playlist.
# The playlist contains only a limited number of songs, and after all items
# were returned by next(), Python raised StopIteration to signal that there
# are no more elements left to iterate over.
#
# This is normal behavior for iterators in Python.
"""
