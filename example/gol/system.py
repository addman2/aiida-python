# -*- coding: utf-8 -*-

from PIL.BmpImagePlugin import BmpImageFile
from PIL import Image
from aiida.orm import Data


class GOLSystem(Data):
    """
    This is a data node for Conway's Game of Life
    """
    def __init__(self, array=None, **kwargs):
        """
        :param array: numpy array of booleans, True = alive, False = dead
        """

        super(Data, self).__init__(**kwargs)

        if isinstance(array, BmpImageFile):
            array = array.convert('1')
            width, height = array.size
            array = [[bool(array.getpixel((ii, jj))) for ii in range(width)]
                     for jj in range(height)]
        else:
            array = [[bool(array[ii, jj]) for ii in range(array.shape[0])]
                     for jj in range(array.shape[1])]

        self.set_attribute('array', array)

    def as_array(self):
        return self.get_attribute('array')

    def get_dimensions(self):
        array = self.as_array()
        return len(array[0]), len(array)

    def get_bitmap(self):
        width, height = self.get_dimensions()
        array = self.as_array()
        img = Image.new('1', (width, height), 0)
        for ii in range(width):
            for jj in range(height):
                img.putpixel((ii, jj), int(array[ii][jj]))
        return img
