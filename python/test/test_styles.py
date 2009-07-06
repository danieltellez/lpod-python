# -*- coding: UTF-8 -*-
# Copyright (C) 2009 Itaapy, ArsAperta, Pierlis, Talend

# Import from the Standard Library
from unittest import TestCase, main

# Import from lpod
from lpod.styles import hex2rgb, rgb2hex


class Hex2RgbTestCase(TestCase):

    def test_color_low(self):
        color = '#012345'
        expected = (1, 35, 69)
        self.assertEqual(hex2rgb(color), expected)


    def test_color_high(self):
        color = '#ABCDEF'
        expected = (171, 205, 239)
        self.assertEqual(hex2rgb(color), expected)


    def test_color_lowercase(self):
        color = '#abcdef'
        expected = (171, 205, 239)
        self.assertEqual(hex2rgb(color), expected)


    def test_color_bad_size(self):
        color = '#fff'
        self.assertRaises(ValueError, hex2rgb, color)


    def test_color_bad_format(self):
        color = '978EAE'
        self.assertRaises(ValueError, hex2rgb, color)


    def test_color_bad_hex(self):
        color = '#978EAZ'
        self.assertRaises(ValueError, hex2rgb, color)



class Rgb2HexTestCase(TestCase):

    def test_color_name(self):
        color = 'violet'
        expected = '#EE82EE'
        self.assertEqual(rgb2hex(color), expected)


    def test_color_tuple(self):
        color = (171, 205, 239)
        expected = '#ABCDEF'
        self.assertEqual(rgb2hex(color), expected)


    def test_color_bad_name(self):
        color = 'dark white'
        self.assertRaises(KeyError, rgb2hex, color)


    def test_color_bad_tuple(self):
        # For alpha channel? ;-)
        color = (171, 205, 238, 128)
        self.assertRaises(ValueError, rgb2hex, color)


    def test_color_bad_low_channel(self):
        color = (171, 205, -1)
        self.assertRaises(ValueError, rgb2hex, color)


    def test_color_bad_high_channel(self):
        color = (171, 205, 256)
        self.assertRaises(ValueError, rgb2hex, color)


    def test_color_bad_value(self):
        color = {}
        self.assertRaises(TypeError, rgb2hex, color)



if __name__ == '__main__':
    main()