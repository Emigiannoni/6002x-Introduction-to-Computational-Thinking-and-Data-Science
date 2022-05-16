# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 11:36:04 2022

@author: Emi
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    
    list = []
    
    total_size = 0
    
    counter = 0
    
    if songs[0][2] < max_size:
    
        list.append(songs[0][0])
        total_size += songs[0][2]
    
    else:
        
        return list
    
    for song_i in songs:
        
        best_choice = song_i
        
        if best_choice[0] not in list:
            
            for song_j in songs:
                
                if best_choice[2] < song_j[2]:
                    
                    pass
                
                elif song_j[0] not in list:
                    
                    best_choice = song_j
        
        if best_choice[0] not in list:      

            total_size += best_choice[2]
            
            if total_size <= max_size:
            
                list.append(best_choice[0])
            
            else:
                
                return list
        
    for song in songs:
        
        if song[0] not in list and total_size + song[2] <= max_size:
            
            total_size += song[2]
            
            list.append(song[0])
    
    return list


print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20))
print(song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 20))
print(song_playlist([('z', 0.1, 9.1), ('a', 4.4, 4.0), ('b', 2.7, 1.2), ('cc', 3.5, 7.7), ('ddd', 5.1, 6.9)], 14))
print(song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 2.7, 1.2), ('cc', 3.5, 7.7), ('ddd', 5.1, 6.9)], 5.4))
print(song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 5.4))