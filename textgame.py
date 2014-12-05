class MapCell():
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.id = parent.GetCellID()
        self.neighbors = []
        self.left = ""
        self.right = ""
        self.up = ""
        self.down = ""
    
    def SetNeighbor(self,side,cell):
        if side == 'left':
            self.left = cell
            cell.right = self
        elif side == 'right':
            self.right = cell
            cell.left = self
        elif side == 'up':
            self.up = cell
            cell.down = self
        elif side == 'down':
            self.down = cell
            cell.up = self
    
    def GetNeighbor(self,side): #up down left right
        if side == 'left':
            return self.left
        elif side == 'right':
            return self.right
        elif side == 'up':
            return self.up
        elif side == 'down':
            return self.down

class Map():
    def __init__(self):
        self.cells = []
        self.currcell = ""
    
    def AddCell(self,cell):
        if len(self.cells) == 0:
            self.currcell = cell
            
        self.cells.append(cell)
    
    def GetCellID(self):
        return len(self.cells) + 1
        
    def GetCellByID(self,i):
        for c in self.cells:
            if c.id == i:
                return c
    
    def MainLoop(self):
        print self.currcell.name
        print 'left or right?'
        inp = raw_input()
        if inp == 'left':
            self.currcell = self.currcell.GetNeighbor('left')
        elif inp == 'right':
            self.currcell = self.currcell.GetNeighbor('right')
        elif inp == 'up':
            self.currcell = self.currcell.GetNeighbor('up')
        elif inp == 'down':
            self.currcell = self.currcell.GetNeighbor('down')
        self.MainLoop()
        
game = Map()
center = MapCell("center (0,0)",game)
left = MapCell("leftofcenter (-1,0)",game)
right = MapCell("rightofcenter (1,0)",game)
up = MapCell("abovecenter (0,1)",game)
down = MapCell("belowcenter (0,-1)",game)

center.SetNeighbor('left',left)
center.SetNeighbor('right',right)
center.SetNeighbor('up',up)
center.SetNeighbor('down',down)

game.AddCell(center)
game.AddCell(left)
game.AddCell(up)
game.AddCell(down)
game.MainLoop()