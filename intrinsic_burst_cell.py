# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:27:08 2021

@author: ramabg
"""

import izhikevich_cells as izh

class ibCell(izh.izhCell):
    """this class models the behavior of an intrinsically bursting cell
    """    
    def __init__(self, stimVal):
        """ reassigns the values based on the intrins. bursting cell equation
        """
        
        super().__init__(stimVal)
        
        # Define Neuron Parameters
        self.celltype = "intrinsically bursting"
        self.C = 150
        self.vr = -75
        self.vt = -45
        self.k = 1.2
        self.a = 0.01
        self.b = -5
        self.c = -56
        self.d = 130
        self.vpeak = 50
        self.stimVal = stimVal
    

myCell = ibCell(4000)
myCell.simulate()

if __name__ == "__main__":
    izh.plotMyData(myCell)
    

