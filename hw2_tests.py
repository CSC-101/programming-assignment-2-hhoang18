from typing import Tuple

import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1=data.Point(5,6)
        point2=data.Point(2,5)
        result = hw2.create_rectangle(point1, point2)
        expected = hw2.Rectangle(data.Point(2, 6), data.Point(5, 5))
        self.assertEqual(expected, result)
    def test_create_rectangle_2(self):
        point1=data.Point(3,3)
        point2=data.Point(4,4)
        result = hw2.create_rectangle(point1, point2)
        expected = hw2.Rectangle(data.Point(3, 4), data.Point(4, 3))
        self.assertEqual(expected, result)

    # Part 2
    def test_shorter_duration_1(self):
        duration1 = data.Duration(2,10)
        duration2 = data.Duration(3,10)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(expected, result)

    def test_shorter_duration_2(self):
        duration1 = data.Duration(4,10)
        duration2 = data.Duration(3,10)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(expected, result)

    # Part 3
    def test_songs_shorter_than_1(self):
        songs = [data.Song("Taylor Swift", "Cruel Summer", data.Duration(2,58)),
                 data.Song("Sabrina Carpenter","Espresso",data.Duration(2,55))]
        length = data.Duration(2,57)
        result = hw2.songs_shorter_than(songs, length)
        expected = [data.Song("Sabrina Carpenter","Espresso",data.Duration(2,55))]
        self.assertEqual(expected, result)

    def test_songs_shorter_than_2(self):
        songs = [data.Song("Beyonce", "Halo", data.Duration(4, 20)),
                 data.Song("Lizzy McAlpine", "Ceilings", data.Duration(3, 2))]
        length = data.Duration(3, 14)
        result = hw2.songs_shorter_than(songs, length)
        expected = [data.Song("Lizzy McAlpine", "Ceilings", data.Duration(3, 2))]
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time_1(self):
        songs = [data.Song("Beyonce", "Halo", data.Duration(4, 20)),
                 data.Song("Lizzy McAlpine", "Ceilings", data.Duration(3, 2))]
        num = [0,1]
        result = hw2.running_time(songs, num)
        expected = data.Duration(7,22)
        self.assertEqual(expected.minutes, result.minutes)
        self.assertEqual(expected.seconds, result.seconds)

    def test_running_time_2(self):
        songs = [data.Song("Beyonce", "Halo", data.Duration(4, 20)),
                 data.Song("Sabrina Carpenter", "Espresso", data.Duration(2, 5))]
        num = [0, 1]
        result = hw2.running_time(songs, num)
        expected = data.Duration(6, 25)
        self.assertEqual(expected.minutes, result.minutes)
        self.assertEqual(expected.seconds, result.seconds)

    # Part 5
    def test_validate_route_1(self):
        links = [['san jose','campbell'],['campbell','los gatos']]
        valid_route = ['san jose','campbell','los gatos']
        result = hw2.validate_route(links, valid_route)
        expected = False
        self.assertEqual(expected, result)

    def test_validate_route_2(self):
        links = [['san jose','campbell']]
        valid_route = ['san jose','campbell']
        result = hw2.validate_route(links, valid_route)
        expected = True
        self.assertEqual(expected, result)

    # Part 6
    def test_longest_repetition_1(self):
        nums = [1,1,1,1,2,2]
        result = hw2.longest_repetition(nums)
        expected = 0
        self.assertEqual(expected, result)

    def test_longest_repetition_2(self):
        nums = [2,2,2,2,3]
        result = hw2.longest_repetition(nums)
        expected = 0
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
