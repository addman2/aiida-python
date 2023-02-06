
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

        array = [[bool(array[ii, jj]) for ii in range(array.shape[0])] for jj in range(array.shape[1])]
        self.set_attribute("array", array)
