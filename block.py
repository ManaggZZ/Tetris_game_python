
#! We will use inheritance and make a block class which will be used to make different blocks as child classes
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}     # We will use this dictionary to store the occupied cells in the bounding grid for each rotation state of the block
        self.cell_Size = 30
        self.rotation_state = 0
        
