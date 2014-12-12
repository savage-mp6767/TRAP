#WRITTEN IN PYTHON 2.7, NOT PYTHON 3.x.x!!!

from Tkinter import *
import random
root = Tk()

class Game:
    # Create the canvas widget
    def __init__(self):
        self.drawpad = Canvas(root, width = 450,height=600, background='grey')
        self.drawpad.grid(row=0, column=1)

        #game board
        self.gameBoard = [
                        [1,0,0,0,0,0,0,0,0,1],
                        [0,1,0,0,0,0,0,0,1,0],
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
                        [0,1,0,0,0,0,0,0,1,0],
                        [1,0,0,0,0,0,0,0,0,1]
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

        self.currShape = None
        self.direction = 1
        self.animate()

    def InsertAt(self,x,y,tblData):
        curx = 0
        cury = 0
        for row in self.gameBoard:
            cury = cury + 1
            curx = 0
            for col in row:
                curx = curx + 1



    def CreateObj(self,t,x,y):
        if t == "t":
            pass
        elif t == "rl":
            pass
        elif t == "ll":
            pass
        elif t == "lz":
            pass
        elif t == "rz":
            pass
        elif t == "sq":
            pass
        elif t == "li":
            pass
        else:
            return False

    def animate(self):
        print 'animate'
        #clear drawpad
        self.drawpad.delete("all")

        #redraw gameboard
        yy = 0
        xx = 0
        for row in range(len(self.gameBoard)):
            yy = yy + 1
            for col in range(row):
                xx = xx + 1
                print str(xx) + ':' + str(yy)
                if self.gameBoard[row][col] != 0:
                    x = xx * 20
                    y = yy * 20
                    self.drawpad.create_rectangle(x,y,x+20,y+20,fill='red',outline='black')
            

        if currShape != "":
            #control current shape
            pass
        else:
            #create new random shape
            pass
        drawpad.after(10, self.animate)
    
    #Key movements 
    def key(self,event):
        print 'key'

        if currShape != "":
            if event.char =="s":
                pass
            elif event.char =="a" and vals[2]>50:
                pass
            elif event.char =="d" and vals[0]<drawpad.winfo_width() - widths[currShapeF]:
                pass
        else:
            pass

game = Game()
root.bind_all('<Key>', game.key)
#CreateObj(random.choice(shapes))
root.mainloop()