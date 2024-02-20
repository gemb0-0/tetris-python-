from block import block
from position import position

class Lblock(block):
    def __init__(self):
        super().__init__(id=1)
        self.cells={
            0: [position(0, 2), position(1, 0), position(1, 1), position(1, 2)],
            1: [position(0, 1), position(1, 1), position(2, 1), position(2, 2)],
            2: [position(1, 0), position(1, 1), position(1, 2), position(2, 0)],
            3: [position(0, 0), position(0, 1), position(1, 1), position(2, 1)]
        }
        self.move(0,3)

class Iblock(block):
    def __init__(self):
        super().__init__(id=2)
        self.cells={
            0: [position(1, 0), position(1, 1), position(1, 2), position(1, 3)],
            1: [position(0, 2), position(1, 2), position(2, 2), position(3, 2)],
            2: [position(2, 0), position(2, 1), position(2, 2), position(2, 3)],
            3: [position(0, 1), position(1, 1), position(2, 1), position(3, 1)]
        }
        self.move(-1,3)

class Oblock(block):
    def __init__(self):
        super().__init__(id=3)
        self.cells={
            0: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
            1: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
            2: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
            3: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)]
        }
        self.move(0,4)

class Sblock(block):
    def __init__(self):
        super().__init__(id=4)
        self.cells={
            0: [position(0, 1), position(0, 2), position(1, 0), position(1, 1)],
            1: [position(0, 1), position(1, 1), position(1, 2), position(2, 2)],
            2: [position(1, 1), position(1, 2), position(2, 0), position(2, 1)],
            3: [position(0, 0), position(1, 0), position(1, 1), position(2, 1)]
        }
        self.move(0,3)

class Tblock(block):
    def __init__(self):
        super().__init__(id=5)
        self.cells={
            0: [position(0, 1), position(1, 0), position(1, 1), position(1, 2)],
            1: [position(0, 1), position(1, 1), position(1, 2), position(2, 1)],
            2: [position(1, 0), position(1, 1), position(1, 2), position(2, 1)],
            3: [position(0, 1), position(1, 0), position(1, 1), position(2, 1)]
        }
        self.move(0,3)

class Zblock(block):
    def __init__(self):
        super().__init__(id=6)
        self.cells={
            0: [position(0, 0), position(0, 1), position(1, 1), position(1, 2)],
            1: [position(0, 2), position(1, 1), position(1, 2), position(2, 1)],
            2: [position(1, 0), position(1, 1), position(2, 1), position(2, 2)],
            3: [position(0, 1), position(1, 0), position(1, 1), position(2, 0)]
        }
        self.move(0,3)

class Jblock(block):
    def __init__(self):
        super().__init__(id=7)
        self.cells={
            0: [position(0, 0), position(1, 0), position(1, 1), position(1, 2)],
            1: [position(0, 1), position(0, 2), position(1, 1), position(2, 1)],
            2: [position(1, 0), position(1, 1), position(1, 2), position(2, 2)],
            3: [position(0, 1), position(1, 1), position(2, 0), position(2, 1)]
        }
        self.move(0,3)
