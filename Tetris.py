#WRITTEN IN PYTHON 2.7!!!

from Tkinter import *
import random
root = Tk()


#tetro class containing all information about the tetromino and it's child rects
class Tetro:
    def __init__(self,x,y):
        self.children = []
        #top left corner
        self.origin_x = x 
        self.origin_y = y 

    def AddChildBlock(self,poly,x,y):
        self.children.append([x,y]) #tuple - (3,3) (2,3,4)

    def GetChildren(self):
        return self.children

    def GetChild(self,idx):
        return self.children[idx]

    def SetPos(self,x,y):
        self.origin_x = x
        self.origin_y = y

        i = 0
        for block in children:
            i = i + 1
            block[1] = self.origin_x + i * 50
            block[2] = self.origin_y + i * 50

    def GetPos(self):
        return [self.origin_x,self.origin_y]

    def Draw(self,drawpad):
        for child in self.children:
            drawpad.create_rectangle(child[0],child[1],child[0] + 25, child[1] + 25, fill='red', outline='black')

class Game:
    # Create the canvas widget
    def __init__(self):
        self.drawpad = Canvas(root, width = 300,height=600, background='grey')
        self.drawpad.grid(row=0, column=1)

        #game board
        self.gameBoard = [
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]
                    ]

        #create the shapes

        self.shapetypes = ['t','rl','ll','lz','rz','sq','li']

        self.shapes = {}
        self.shapes['t'] = [[1,1,1],     #   # # #
                            [0,1,0]]    #     #

        self.shapes['rl'] = [[1,0],      #   #
                            [1,0],      #   #
                            [1,1]]      #   # #

        self.shapes['ll'] = [[0,1],      #     #
                            [0,1],      #     #
                            [1,1]]      #   # #

        self.shapes['lz'] = [[1,1,0],    #   # # 
                            [0,1,1]]    #     # #

        self.shapes['rz'] = [[0,1,1],    #   
                            [1,1,0]]    #

        self.shapes['sq'] = [[1,1],      #
                            [1,1]]      #

        self.shapes['li'] = [[1],        #
                            [1],        #
                            [1],        #
                            [1]]        #

        self.currShapeF = "" #current shape name
        #widths = {}
        #widths['t']=150
        #widths['rl']=100
        #widths['ll']=100
        #widths['lz']=150
        #widths['rz']=150
        #widths['sq']=100
        #widths['li']=50

        self.currShape = ""
        self.direction = 1
        self.animate()

    def GetBlockByCoord(self,x,y):
        for yy in range(0,16):
            for xx in range(0,10):
                if yy == y:
                    if xx == x:
                        return gameboard[xx][yy]

    def SetBlockByCoord(self,x,y,val):
        for yy in range(0,16):
            for xx in range(0,10):
                if yy == y:
                    if xx == x:
                        gameboard[xx][yy] = val

    def ShapeToBlock(self,shape):
        drawpad = self.drawpad
        temp = Tetro(0,0)
        xi = 0
        yi = 0
        for x in self.shapes[str(shape)]:
            xi = xi + 1
            for y in x:
                yi = yi + 1
                if y == 1:
                    temp.AddChildBlock(int(xi), int(yi), drawpad.create_rectangle(int(xi) * 25, int(yi) * 25, int(xi) * 25 + 25, int(yi) * 25 + 25, fill='red'))
       
        return temp

    def ShapeToGameboard(self,shape,ox,oy):
        for y in range(0,16):
            for x in range(0,10):
                if y == oy:
                    if x == ox:
                        for sy in self.shapes[str(shape)]:
                            for sx in sy:
                                self.gameboard[sy][sx] = sx #possibly need to do int(sy) bc sy is table?


    def CreateObj(self,t):
        drawpad = self.drawpad
        currshape = self.currShape
        if t == "t":
            currShape = self.ShapeToBlock("t")
            drawpad.move(currShape,225,-350)
            currShapeF = "t"
        elif t == "rl":
            currShape = self.ShapeToBlock("rl")
            drawpad.move(currShape,100,-70)
            currShapeF = "rl"
        elif t == "ll":
            currShape = self.ShapeToBlock("ll")
            drawpad.move(currShape,-125,-255)
            currShapeF = "ll"
        elif t == "lz":
            currShape = self.ShapeToBlock("lz")
            drawpad.move(currShape,-260,-350)
            currShapeF = "lz"
        elif t == "rz":
            currShape = self.ShapeToBlock("rz")
            drawpad.move(currShape,0, -20)
            currShapeF = "rz"
        elif t == "sq":
            currShape = self.ShapeToBlock("sq")
            drawpad.move(currShape,225,-400)
            currShapeF = "sq"
        elif t == "li":
            currShape = self.ShapeToBlock("li")
            drawpad.move(currShape,-300, -400)
            currShapeF = "li"
        else:
            return False


        #drawpad.move(shape1Square,225,-400)
        #drawpad.move(shape2Rectangle,-300, -400)
        #drawpad.move(t,225,-350)
        #drawpad.move(rl,100,-70)
        #drawpad.move(ll,-125,-255)
        #drawpad.move(lz,-260,-350)
        #drawpad.move(rz,0, -20)

    def animate(self):
        print 'animate'
        direction = self.direction
        currShape = self.currShape
        drawpad = self.drawpad
        #print(self.gameBoard)
        # Gets Coordinates of currShape
        if currShape != "":
            l = self.currShape.GetPos()
            print l
            if l[0] < 16:
                currShape.SetPos(currShape.GetPos()[0]-1,currShape.GetPos()[1]-1)
            if l[3] < drawpad.winfo_height(): 
                direction = 1
            else:
                direction = 0
                currShape = ""
            print(currShape.GetPos())
            currShape.SetPos(currShape.GetPos()[0]-1,currShape.GetPos()[1]-1)
            print(currShape.GetPos())
            currShape.ShapeToGameboard(currShapeF,currShape.GetPos()[0],currShape.GetPos()[1])
            # Wait for 1 millisecond, then recursively call our animate function
        else:
            self.CreateObj(random.choice(self.shapetypes))
        drawpad.after(1, self.animate)
    
    #Key movements 
    def key(self,event):
        print 'key'
        drawpad = self.drawpad
        currShape = self.currShape

        if currShape != "":
            vals = list(currShape.GetPos())
            print vals
            if event.char =="s":
                currshape.SetPos(vals[0],vals[1] + 1)
            elif event.char =="a" and vals[2]>50:
                currshape.SetPos(vals[0] - 1,vals[1])
            elif event.char =="d" and vals[0]<drawpad.winfo_width() - widths[currShapeF]:
                currshape.SetPos(vals[0] + 1,vals[1])
        else:
            pass
        # Kick off our animation

game = Game()
root.bind_all('<Key>', game.key)
#CreateObj(random.choice(shapes))
root.mainloop()