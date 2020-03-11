"""
 Copyright © 2020 Stephan Hagel (sthagel@uw.edu)
 This file is part of the g.bims project.
 This project is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import eyed3


def split_list_by_genre(songlist):
    """
    Takes a list of songs and returns a dictionary with all the genres of
    all the songs as keys and a list with all songs corresponding to that
    genre as entries.
    :param songlist: List of song filenames as strings
    :return: Dictionary with genres as strings as keys and lists of song filenames as entries
    """
    genre_dict = {}
    for song in songlist:
        genre = get_genre_from_song(song)
        if genre not in genre_dict.keys():
            genre_dict[genre] = []
        genre_dict[genre].append(song)

    return genre_dict


def get_genre_from_song(songname):
    """
    Uses eyed3 to get the genre tag from a given song.
    :param songname: A string pointing to the song's mp3 file
    :return: The genre of the song as string
    """
    audiofile = eyed3.load(songname)
    genre = audiofile.tag.genre
    return str(genre)
