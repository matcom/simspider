# -*- coding: iso-8859-1 -*-
#
# Copyright (C) 2009  Rene Liebscher
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with 
# this program; if not, see <http://www.gnu.org/licenses/>. 
#

__revision__ = "$Id: GammaOperator.py,v 1.6 2009/09/24 20:32:20 rliebscher Exp $"

from Redist.pyfuzzy.norm.Norm import NormException
from Redist.pyfuzzy.norm.ParametricNorm import ParametricNorm

class GammaOperator(ParametricNorm):

    _range = [ [0.,1.] ]

    def __init__(self,p=0.5):
        ParametricNorm.__init__(self,0,p)

    def __call__(self,*args):
        if len(args) != 2:
            raise NormException("%s is supported only for 2 parameters" % self.__class__.__name__ )
        p = self.p
        x = float(args[0])
        y = float(args[1])
        if x == 0. or y == 0.:
            return 0. if p != 1. else (x or y)
        return x*y*pow((x+y)/(x*y)-1,p)
