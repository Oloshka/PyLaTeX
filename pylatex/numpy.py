# -*- coding: utf-8 -*-
"""
    pylatex.numpy
    ~~~~~~~~~~~~~

    This module implements the classes that deals with numpy objects.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

import numpy as np
from pylatex.base_classes import BaseLaTeXClass
from pylatex.package import Package


def format_vec(name):
    return r'\mathbf{' + name + '}'


class Matrix(BaseLaTeXClass):
    def __init__(self, matrix, name='', mtype='p', alignment=None):
        self.mtype = mtype
        self.matrix = matrix
        self.alignment = alignment
        self.name = name

        super().__init__(packages=[Package('amsmath')])

    def dumps(self):
        string = r'\begin{'
        mtype = self.mtype + 'matrix'

        if self.alignment is not None:
            mtype += '*'
            alignment = '{' + self.alignment + '}'
        else:
            alignment = ''

        string += mtype + '}' + alignment
        string += '\n'

        shape = self.matrix.shape

        for (y, x), value in np.ndenumerate(self.matrix):
            if x:
                string += '&'
            string += str(value)

            if x == shape[1] - 1 and y != shape[0] - 1:
                string += r'\\' + '\n'

        string += '\n'

        string += r'\end{' + mtype + '}'

        super().dumps()
        return string
