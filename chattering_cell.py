# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:56:40 2021

@author: ramabg
"""

import izhikevich_cells as izh

class cCell(izh.izhCell):
    """ this class models the behavior of a chattering cell
    """
    
    
    def __init__(self, stimVal):
        """ reassigns the values based on the chattering cell equation
        """
        
        super().__init__(stimVal)
        
        # Define Neuron Parameters
        self.celltype = "chattering cell"
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = 0.03
        self.b = -5
        self.c = -40
        self.d = 150
        self.vpeak = 25
        self.stimVal = stimVal
    

myCell = cCell(4000)
myCell.simulate()

if __name__ == "__main__":
    izh.plotMyData(myCell)
    

