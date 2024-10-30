from typing import Optional
import math

import data

# Write your functions for each part in the space below.

# Part 1
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)
    def __eq__(self, other) -> bool:
        return (other is self or
            type(other) == Point and
            math.isclose(self.x, other.x) and
            math.isclose(self.y, other.y))
class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right
    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)

def create_rectangle(point1:Point, point2:Point)->Rectangle:
    left_x = min(point1.x,point2.x)
    right_x = max(point1.x,point2.x)
    top_y = max(point1.y,point2.y)
    bottom_y = min(point1.y,point2.y)

    top_left = data.Point(left_x,top_y)
    bottom_right = data.Point(right_x, bottom_y)
    return Rectangle(top_left, bottom_right)
#the function's purpose is to identify the top left and bottom right corners of a rectangle given two points
#the inputs are two points
#the output is a Rectangle with its top left and bottom right coordinates
#the parameters are type Point
#a Rectangle is returned

# Part 2
class Duration:
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds
    def __repr__(self) -> str:
        return 'Duration({}, {})'.format(self.minutes, self.seconds)
def shorter_duration_than(duration1:Duration, duration2:Duration)->bool:
    duration1_seconds=duration1.minutes*60+duration1.seconds
    duration2_seconds=duration2.minutes*60+duration2.seconds
    if duration1_seconds<duration2_seconds:
        return True
    else:
        return False
#the function's purpose is to compare the durations of two things (e.g. songs)
#the inputs are two durations
#the outputs are True (if first duration is shorter than the second) and False (if otherwise)
#the parameters are type Duration
#a boolean is returned

# Part 3
class Song:
    def __init__(self, artist: str, title: str, duration:Duration):
        self.artist = artist
        self.title = title
        self.duration = duration
class Duration:
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds

def songs_shorter_than(songs:list[Song], length:Duration)->list[Song]:
    length_seconds = length.minutes*60+length.seconds
    return [song for song in songs if (song.duration.minutes*60+song.duration.seconds)<length_seconds]

#the function's purpose is to return a list of songs with a shorter duration than the specified upper bound
#the inputs are songs and the song lengths
#the output is a list of songs with a shorter duration than the limit
#the parameters are type list[Song] and Duration
#a list[Song] is returned

# Part 4
class Duration:
    def __init__(self, minutes:int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds
    def __repr__(self) -> str:
        return 'Duration({}, {})'.format(self.minutes, self.seconds)
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)
class Song:
    def __init__(self, artist: str, title: str, duration: Duration):
        self.artist = artist
        self.title = title
        self.duration = duration
    def __repr__(self):
        return "Song('{}', '{}', {})".format(self.artist, self.title,
            self.duration)
    def __eq__(self, other):
        return (self is other or
                type(other) == Song and
                self.artist == other.artist and
                self.title == other.title and
                self.duration == other.duration)
def running_time(songs:list[Song], num: list[int])->Duration:
    total_minutes = 0
    total_seconds = 0
    for idx in range(0,len(songs)):
        song_length=songs[idx].duration
        total_minutes = total_minutes + song_length.minutes
        total_seconds = total_seconds + song_length.seconds
    total_duration = Duration(total_minutes,total_seconds)
    return total_duration
#the function's purpose is to return the total running time for a given playlist
#the input is a list of songs and a list of integers numbering the songs
#the output is the total running time for the playlist
#the parameters are type list[Song] and list[int]
#a Duration object is returned

# Part 5
def validate_route(links:list[list[str]],route:list[str])->bool:
    for idx in range(len(route)-1):
        first_city=route[idx]
        second_city=route[idx+1]

        valid_link = False #check if there is link between consecutive cities
        for link in links:
            if first_city==link[0] and second_city==link[1]:
                valid_link = True
            else:
                return False
    return True
#the function's purpose is to check if a route between two cities is valid (they are connected)
#the input is city links and city names
#the output is true or false
#the parameters are type list[list[str]] and list[str]
#boolean is returned

# Part 6
def longest_repetition(nums:list[int])->Optional[int]:
    if len(nums)==0:#in case of an empty list
        return None
    longest=1 #longest contiguous repetition
    idx=0 #idx where the longest contiguous repetition starts
    current_length=1 #length of current rep
    current_idx=0 #idx where the current repetition starts
    for idx in range(0, len(nums)):
        if nums[idx]==nums[idx+1]: #comparing two numbers next to each other
            current_length=current_length+1
        else:
            if current_length>longest: #finding the longest repetition
                longest=current_length
                idx=current_idx
        return idx
#the function's purpose is to find the longest contiguous repetition of a number in a list
#the input is a list of integers
#the output is an index where the longest contiguous repetition begins
#the parameter is type list[int]
#an index or None are returned