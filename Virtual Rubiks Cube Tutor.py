from tkinter import *
from Cube_Solver import solve
from Rotations import makeMove
from Cross_Solver_Wrapper import solveCross
import random,time,copy

class Cube(object):
    def __init__(self,cube,isDrawingEntire,startX,startY,length):
        self.cube = cube
        self.isDrawingEntire = isDrawingEntire
        self.startX = startX
        self.startY = startY
        self.length = length
    def draw(self,canvas):
        def drawTop(canvas,startX,startY,length,colors):
            for i in range(3):
                x = startX + i * length / 3
                y = startY
                for j in range(3):
                    increment1 = (j+1) * (length / 2**0.5 / 3 /2)
                    increment2 = (j) * (length / 2**0.5 / 3/2)
                    (x1,y1) = (x + increment1, y - increment1)
                    (x2,y2) = (x+increment2,y-increment2)
                    (x3,y3) = (x+length/3+increment2,y-increment2)
                    (x4,y4) = (x+length/3+increment1,y-increment1)
                    canvas.create_polygon((x1,y1),(x2,y2),(x3,y3),(x4,y4),fill = colors[i * 3 + j])
            
            for i in range(4):
                x = startX + length / 2 / 3 / 2**0.5 * i
                y = startY - length/ 2  / 3 / 2**0.5 * i
                (x1,y1) = (x,y)
                (x2,y2) = (x+length,y)
                canvas.create_line((x1,y1),(x2,y2), fill = "grey",width = 1)
            for i in range(4):
                x = startX + length / 3 * i
                y = startY
                (x1,y1) = (x,y)
                (x2,y2) = (x + length/ 2 / 2**0.5, y - length/2/ 2**0.5)
                canvas.create_line((x1,y1),(x2,y2),fill = "grey",width = 1)
        def drawFront(canvas,startX,startY,length,colors):
            for i in range(3):
                x = startX + i * length / 3
                y = startY
                for j in range(3):
                    increment1 = j * length / 3
                    increment2 = (j+1) * length / 3
                    (x1,y1) = (x,y+increment1)
                    (x2,y2) = (x,y+increment2)
                    (x3,y3) = (x+length/3,y+increment2)
                    (x4,y4) = (x+length/3, y+increment1)
                    canvas.create_polygon((x1,y1),(x2,y2),(x3,y3),(x4,y4),fill = colors[i * 3 + j])
            for i in range(4):
                x = startX + i * length / 3
                y = startY
                (x1,y1) = (x,y)
                (x2,y2) = (x,y + length)
                canvas.create_line((x1,y1),(x2,y2), fill = "grey",width = 1)
            for i in range(4):
                x = startX 
                y = startY + i * length / 3
                (x1,y1) = (x,y)
                (x2,y2) = (x+ length,y)
                canvas.create_line((x1,y1),(x2,y2), fill = "grey",width = 1)
        def drawRight(canvas,startX,startY,length,colors):
            startX += length
            for i in range(3):
                x = startX
                y = startY + i * length / 3
                for j in range(3):
                    increment1 = (j+1) * (length / 2**0.5 / 3 /2)
                    increment2 = (j) * (length / 2**0.5 / 3/2)  
                    (x1,y1) = (x+increment2,y-increment2)
                    (x2,y2) = (x +increment2, y+length/3-increment2 )
                    (x3,y3) = (x + increment1,y + length / 3 - increment1)
                    (x4,y4) = (x+increment1, y - increment1)
                    canvas.create_polygon((x1,y1),(x2,y2),(x3,y3),(x4,y4),fill = colors[i * 3 + j])
            for i in range(4):
                x= startX
                y = startY + i *length / 3
                (x1,y1) = (x,y)
                (x2,y2) = (x + length / 2 / 2**0.5, y - length / 2 / 2**0.5)
                canvas.create_line((x1,y1),(x2,y2), fill = "grey",width = 1)
            for i in range(4):
                x = startX + length / 2 / 3 / 2**0.5 * i
                y = startY - length / 2 / 3 / 2**0.5 * i
                (x1,y1) = (x,y)
                (x2,y2) = (x, y+length)
                canvas.create_line((x1,y1),(x2,y2), fill = "grey",width = 1)

        def drawLeft(canvas,startX,startY,length,colors):
            startX -= 300
            startY -= 0
            drawRight(canvas,startX,startY,length,colors)

        def drawDown(canvas,startX,startY,length,colors):
            startX -= 30
            startY += 300
            drawTop(canvas,startX,startY,length,colors)

        def drawBack(canvas,startX,startY,length,colors):
            startX += 300
            startY -= 125
            drawFront(canvas,startX,startY,length,colors)
        
        def transferToRight(colors):
            return colors

        def transferToTop(colors):
            result = []
            for i in [6,3,0,7,4,1,8,5,2]:
                result.append(colors[i])
            return result
        def transferToFront(colors):
            result = []
            for i in [0,3,6,1,4,7,2,5,8]:
                result.append(colors[i])
            return result
        def transferToLeft(colors):
            result = []
            for i in [2,1,0,5,4,3,8,7,6]:
                result.append(colors[i])
            return result
        def transferToDown(colors):
            return transferToFront(colors)
        def transferToBack(colors):
            result = []
            for i in [2,5,8,1,4,7,0,3,6]:
                result.append(colors[i])
            return result

        startX = self.startX
        startY = self.startY
        length = self.length
        if self.isDrawingEntire:
            drawTop(canvas,startX,startY,length,transferToTop(self.cube["up"]))
            drawFront(canvas,startX,startY,length,transferToFront(self.cube["front"]))
            drawRight(canvas,startX,startY,length,transferToRight(self.cube["right"]))
            drawLeft(canvas,startX,startY,length,transferToLeft(self.cube["left"]))
            drawDown(canvas,startX,startY,length,transferToDown(self.cube["down"]))
            drawBack(canvas,startX,startY,length,transferToBack(self.cube["back"]))
        else:
            drawTop(canvas,startX,startY,length,transferToTop(self.cube["up"]))
            drawFront(canvas,startX,startY,length,transferToFront(self.cube["front"]))
            drawRight(canvas,startX,startY,length,transferToRight(self.cube["right"]))


def generateARandomCube(isDemo):
    cube = dict()
    cube["front"] = ["blue"]*9
    cube["up"] = ["orange"] *9
    cube["left"] = ["white"]*9
    cube["right"] = ["yellow"]*9
    cube["back"] = ["green"]*9
    cube["down"] = ["red"]*9
    for i in range(20):
        move = random.choice(["F","F2","F'","R","R2","R'","L","L'","L2","B","B2","B'","U","U2","U'","D","D2","D'"])
        makeMove(cube,move)
    rubik = Cube(cube,isDemo,100,275,200)
    return rubik


#########################################################################






def init(data):
    data.mode = 1
    data.Rubik = generateARandomCube(False)
    data.counterInMode2 = 0
    data.currentColorInMode3  = "red"
    data.faceToBeSelectedInMode3 = 0
    data.faceEnteringStatus = ["white"] * 9
    data.cube = dict()
    data.demonstrationCube = None
    data.currentStepInMode6 = 1
    data.solution = None
    data.solutionCube = None
    data.curPointerInMode14 = 0
    data.startingCube = dict()
    data.image1 = PhotoImage(file = "notation1.gif")
    data.image2 = PhotoImage(file = "notation2.gif")
    data.image3 = PhotoImage(file = "notation3.gif")
    data.challengeCubeInMode16 = generateARandomCube(True)
    data.challengeCubeInMode16.startX = 200
    data.challengeCubeInMode16.startY = 225
    data.totalStepsInMode16 = []
    data.solutionCubeInMode17 = Cube(data.challengeCubeInMode16.cube,True,500,175,168)
    data.curPointerInMode17 = 0
    data.startingCubeInMode17 = copy.deepcopy(data.challengeCubeInMode16.cube)

def mousePressed(event, data):
    if data.mode ==   1: mousePressed1(event,data) 
    elif data.mode == 2: mousePressed2(event,data)
    elif data.mode == 3: mousePressed3(event,data)
    elif data.mode == 4: mousePressed4(event,data)
    elif data.mode == 5: mousePressed5(event,data)
    elif data.mode == 6: mousePressed6(event,data)
    elif data.mode == 7: mousePressed7(event,data)
    elif data.mode == 8: mousePressed8(event,data)
    elif data.mode == 9: mousePressed9(event,data)
    elif data.mode == 10: mousePressed10(event,data)
    elif data.mode == 11: mousePressed11(event,data)
    elif data.mode == 12: mousePressed12(event,data)
    elif data.mode == 14: mousePressed14(event,data)
    elif data.mode == 13: mousePressed13(event,data)
    elif data.mode == 15: mousePressed15(event,data)
    elif data.mode == 16: mousePressed16(event,data)
    elif data.mode == 17: mousePressed17(event,data)

def keyPressed(event, data):
    if data.mode == 1: pass
    elif data.mode == 2:keyPressed2(event,data)
    elif data.mode == 6:keyPressed6(event,data)
    elif data.mode == 16:keyPressed16(event,data)

def timerFired(data):
    if data.mode == 1: pass
    elif data.mode == 2:timerFired2(data)


def redrawAll(canvas, data):
    if data.mode ==   1: redrawAll1(canvas,data)
    elif data.mode == 2: redrawAll2(canvas,data)
    elif data.mode == 3: redrawAll3(canvas,data)
    elif data.mode == 4: redrawAll4(canvas,data)
    elif data.mode == 5: redrawAll5(canvas,data)
    elif data.mode == 6: redrawAll6(canvas,data)
    elif data.mode == 7: redrawAll7(canvas,data)
    elif data.mode == 8: redrawAll8(canvas,data)
    elif data.mode == 9: redrawAll9(canvas,data)
    elif data.mode == 10: redrawAll10(canvas,data)
    elif data.mode == 11: redrawAll11(canvas,data)
    elif data.mode == 12: redrawAll12(canvas,data)
    elif data.mode == 14: redrawAll14(canvas,data)
    elif data.mode == 13: redrawAll13(canvas,data)
    elif data.mode == 15: redrawAll15(canvas,data)
    elif data.mode == 16: redrawAll16(canvas,data)
    elif data.mode == 17: redrawAll17(canvas,data)

####################################
# Mode 1: The Welcome Screen
####################################

def mousePressed1(event,data):
    def findRegion(x,y):
        if 725 <=  x <= 1075 and 200 <= y <= 300:
            return "Start_From_Scrartch"
        elif 725 <=  x <= 1075 and 350 <= y <= 450:
            return "Load_Your_Progress"
        elif 725 <=  x <= 1075 and 500 <= y <= 600:
            return "Ready"

    if findRegion(event.x,event.y) == "Start_From_Scrartch":
        data.mode = 2
    elif findRegion(event.x,event.y) == "Load_Your_Progress":
        load(data)

    elif findRegion(event.x,event.y) == "Ready":
        data.mode = 15

def load(data):
    def stringToDict(dictStr):
        result = dict()
        for c in dictStr.split(","):
            for d in range(len(c.split(".")[:-1])):
                if d == 0:
                    result[c.split(".")[:-1][d]] = []
                else:
                    result[c.split(".")[:-1][0]].append(c.split(".")[:-1][d])
        return result

    def stringTo2dList(listStr,data):
        def stringTo1dList(subList):
            result = []
            elems = subList.split("*")[:-1]
            for elem in elems:
                result.append(elem)
            return result

        result = []
        for subList in listStr:
            result.append(stringTo1dList(subList))
        return copy.deepcopy([[]])* (data.currentStepInMode6 - 1) + result
    saved = readFile("save.txt").split(";")
    data.currentStepInMode6 = int(saved[0])
    data.Rubik = Cube(copy.deepcopy(stringToDict(saved[1])),True,500,200,168)
    data.startingCube = copy.deepcopy(stringToDict(saved[2]))
    data.solution = copy.deepcopy(stringTo2dList(saved[3:-1],data))
    data.solutionCube = Cube(data.startingCube,True,500,175,168)
    data.mode = 6

def redrawAll1(canvas,data):
    def drawTheBasics(canvas):
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        for i in range(len("Virtual Rubik's Cube Tutor")):
            canvas.create_text(325+i*25,75,text = "Virtual Rubik's Cube Tutor"[i],font = "Chalkduster 30 bold", fill = random.choice(["red","tan","orange","green","cyan","salmon"]))    
    drawTheBasics(canvas)
    data.Rubik.draw(canvas)
    # draw the buttons
    canvas.create_rectangle((725,200),(1075,300),width = 2 , fill = "grey")
    canvas.create_text((900,250),text = "Start from Scratch",font = "Phosphate 30 ", fill = "red")

    canvas.create_rectangle((725,350),(1075,450),width = 2 , fill = "grey")
    canvas.create_text((900,400),text = "Load Your Progress",font = "Phosphate 30 ", fill = "red")

    canvas.create_rectangle((725,500),(1075,600),width = 2 , fill = "grey")
    canvas.create_text((900,550),text = "Ready To Take The Challenge?",font = "Phosphate 23 ", fill = "red")




#######################################################
# Mode 2: The Screen after hitting start from scratch #
#######################################################


def mousePressed2(event,data):
    def findRegion(x,y):
        if 525<=x<=725 and 575<=y <= 625:
            return "Get_Started"
    if findRegion(event.x,event.y) == "Get_Started":
        data.mode = 3


def timerFired2(data):
    
    if data.counterInMode2 > 500:
        pass
    else:
        data.counterInMode2 += 1

def keyPressed2(event,data):
    data.counterInMode2 = 500

def redrawAll2(canvas,data):

    def length(n,word):
        n -= 1
        result = n
        for i in range(n):
            result+=len(word.split("\n")[i])
        return result
    Words = "Welcome!\nHave you ever dreamed of solving\na Rubik’s cube on your own\nbut never managed to do it?\nThis app would help you realize your dream!"
    if data.counterInMode2 < len(Words):
        lines= 1
        for  i in range(data.counterInMode2):
            canvas.create_rectangle((0,0),(1300,700),fill = "black")
            if  Words[i] != "\n":
                for j in range(lines-1):
                    canvas.create_text((1300/2,100*(j+1)),text = Words.split("\n")[j],font = "Noteworthy 40",fill = "red")
                canvas.create_text((1300/2,100*(lines )),text = Words.split("\n")[lines-1][:(i - length(lines,Words))],font = "Noteworthy 40",fill = "red")

                
            else:
                for j in range(lines-1):
                    canvas.create_text((1300/2,100*(j+1)),text = Words.split("\n")[j],font = "Noteworthy 40",fill = "red")
                canvas.create_text((1300/2,100*(lines )),text = Words.split("\n")[lines-1][:(i - length(lines,Words))],font = "Noteworthy 40",fill = "red")
                lines += 1

    else:
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        for i in range(len(Words.split("\n"))):
            canvas.create_text((1300/2,100*(i+1)),text =Words.split("\n")[i] ,font = "Noteworthy 40",fill = "red")
        #draw the buttons
        canvas.create_rectangle((525,575),(775,625),fill = "grey")
        canvas.create_text((650,600),text = "Get Started!",font = "Optima 30",fill = "black")


#########################################
# Mode 3: The input the cube mode       #
#########################################

def mousePressed3(event,data):
    def findRegion(x,y):
        if 890 <= x<= 1010 and  625 <= y <= 675:
            # Finished Region
            return "Finished"
        elif 150 <= x<= 450 and 250 <= y <= 300:
            return "Choose"
        elif 800 <= x <= 1100 and 300 <= y <= 600:
            return "Blocks"
    if findRegion(event.x,event.y) == "Finished":
        if data.faceToBeSelectedInMode3 == 5:
            data.cube["down"] = data.faceEnteringStatus
            data.Rubik = Cube(data.cube,True,500,200,168)
            data.solutionCube = Cube(data.cube,True,500,175,168)
            data.startingCube = copy.deepcopy(data.Rubik.cube)
            data.mode = 4
            data.solution = solve(data.Rubik.cube)
        else:
            
            if data.faceToBeSelectedInMode3 == 2:
                data.cube["up"] = data.faceEnteringStatus
            else:
                data.cube[["Front","Back","Top","Left","Right","Bottom"][data.faceToBeSelectedInMode3].lower()] = data.faceEnteringStatus
            data.faceToBeSelectedInMode3 += 1
            data.faceEnteringStatus = ["white"] * 9

    elif findRegion(event.x,event.y) == "Choose":
        index = (event.x - 150 ) // 50
        data.currentColorInMode3 = ["red","blue","orange","white","yellow","green"][index]
    elif findRegion(event.x,event.y) == "Blocks":
        i = (event.y - 300 ) // 100
        j = (event.x - 800 ) // 100
        data.faceEnteringStatus[i*3+j] = data.currentColorInMode3


def redrawAll3(canvas,data):
    def drawTheBasics(canvas,data):
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        canvas.create_text((1300/2,100),text = "Tell me what your cube looks like:", font = "Herculanum 30",fill = "sky blue")
        canvas.create_text((300,200),text = "Choose the color:", font = "Herculanum 30",fill = "sky blue")
        color = ["red","blue","orange","white","yellow","green"]
        for i in range(6):
            canvas.create_rectangle((150+i*50,250),(150+(i+1)*50,300),fill = color[i])
        canvas.create_text((300,450),text = "Currently selected color:", font = "Herculanum 30",fill = "sky blue")
        canvas.create_rectangle((230,500),(350,620),fill = data.currentColorInMode3)
        canvas.create_text((900,200),text = "Face to be entered:", font = "Herculanum 30",fill = "sky blue")
        canvas.create_text((1100,200),text = ["Front","Back","Top","Left","Right","Bottom"][data.faceToBeSelectedInMode3], font = "Herculanum 30",fill = "magenta")
        startX = 800
        startY = 300
        for i in range(3):
            x = startX
            y = startY + i * 100
            for j in range(3):
                (x1,y1) = (x + j*100,y)
                (x2,y2) = (x + (j+1)*100,y+100)
                canvas.create_rectangle((x1,y1),(x2,y2),fill = data.faceEnteringStatus[i*3+j])
        canvas.create_rectangle((890,625),(1010,675),fill = "grey")
        canvas.create_text((950,650),text  = "Finished!",font = "Eurostile 20")     
    
    drawTheBasics(canvas,data)

    
###############################
# Mode 4: The Tutorial Page   #
###############################

def mousePressed4(event,data):
    def findRegion(x,y):
        if 550<=x<=650 and 650<=y<=675:
            return "get"
    if findRegion(event.x,event.y) == "get":
        data.mode = 5

def redrawAll4(canvas,data):
    canvas.create_text(20,20,anchor = W, text = "Before the tutorial, let me first introduce you some basics of rotation notation for solving the cube:",font = "Chalkboard 20")
    canvas.create_image(20,70,anchor = NW , image = data.image1)
    canvas.create_image(600,70,anchor = NW , image = data.image2)
    canvas.create_image(600,335,anchor = NW , image = data.image3)
    canvas.create_rectangle(550,650,650,675,fill = "salmon")
    canvas.create_text((600,662.5),text = "Get it!",font = "Eurostile 20")


###############################
# Mode 5: The First Step      #
###############################

def mousePressed5(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll5(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["white","blue","white","blue","blue","blue","white","blue","white"]
        cube["left"] = ["white","blue","white","white","blue","white","white","white","white"]
        cube["right"] = ["white","blue","white","white","blue","white","white","white","white"]
        cube["front"] = ["white","blue","white","white","blue","white","white","white","white"]
        cube["back"] = ["white","blue","white","white","blue","white","white","white","white"]
        cube["down"] = ["white"] * 9
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((300,50),text = "First Step: Make a cross on the top", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")


###############################
# Mode 6: The Rotation Mode   #
###############################


def keyPressed6(event,data):
    if event.keysym == "r":
        makeMove(data.Rubik.cube,"R")
    elif event.keysym == "t":
        makeMove(data.Rubik.cube,"R'")
    elif event.keysym == "e":
        makeMove(data.Rubik.cube,"R2")
    elif event.keysym == "l":
        makeMove(data.Rubik.cube,"L")
    elif event.keysym == "k":
        makeMove(data.Rubik.cube,"L'")
    elif event.keysym == "j":
        makeMove(data.Rubik.cube,"L2")
    elif event.keysym == "b":
        makeMove(data.Rubik.cube,"B")
    elif event.keysym == "v":
        makeMove(data.Rubik.cube,"B'")
    elif event.keysym == "n":
        makeMove(data.Rubik.cube,"B2")
    elif event.keysym == "f":
        makeMove(data.Rubik.cube,"F")
    elif event.keysym == "g":
        makeMove(data.Rubik.cube,"F'")
    elif event.keysym == "h":
        makeMove(data.Rubik.cube,"F2")
    elif event.keysym == "d":
        makeMove(data.Rubik.cube,"D")
    elif event.keysym == "s":
        makeMove(data.Rubik.cube,"D'")
    elif event.keysym == "a":
        makeMove(data.Rubik.cube,"D2")
    elif event.keysym == "u":
        makeMove(data.Rubik.cube,"U")
    elif event.keysym == "y":
        makeMove(data.Rubik.cube,"U'")
    elif event.keysym == "i":
        makeMove(data.Rubik.cube,"U2")
    elif event.keysym == "2":
        makeMove(data.Rubik.cube,"X")
    elif event.keysym == "1":
        makeMove(data.Rubik.cube,"X'")
    elif event.keysym == "3":
        makeMove(data.Rubik.cube,"X2")
    elif event.keysym == "5":
        makeMove(data.Rubik.cube,"Y")
    elif event.keysym == "4":
        makeMove(data.Rubik.cube,"Y'")
    elif event.keysym == "6":
        makeMove(data.Rubik.cube,"Y2")
    elif event.keysym == "8":
        makeMove(data.Rubik.cube,"Z")
    elif event.keysym == "7":
        makeMove(data.Rubik.cube,"Z'")
    elif event.keysym == "9":
        makeMove(data.Rubik.cube,"Z2")
    elif event.keysym == "o":
        makeMove(data.Rubik.cube,"M")
    elif event.keysym == "p":
        makeMove(data.Rubik.cube,"M'")
    elif event.keysym == "q":
        makeMove(data.Rubik.cube,"M2")


def timerFired6(data):
    pass


def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def save(data):#data.currentStepinmode6 data.Rubik.cube data.startingCube data.solution[data.curstep:]
    def dictToString(cube):
        result = ""
        for surface in cube:
            result += surface+"."
            for color in cube[surface]:
                result += color + "."
            result += ","
        return result
    def listToString(L):
        result = ""
        for color in L:
            result += color + "*"
        return result

    contentsToWrite = str(data.currentStepInMode6) + ";" + dictToString(data.Rubik.cube) +";"+ dictToString(data.startingCube) +";"
    for i in range(data.currentStepInMode6 -1,len(data.solution)):
        contentsToWrite += listToString(data.solution[i]) + ";"
    #+ listToString(data.solution[data.currentStepinmode6-1:])
    writeFile("save.txt",contentsToWrite)

def mousePressed6(event,data):
    def findRegion(x,y):
        if 50<= x<=200 and 575<=y<=625:
            return "dunno"
        elif 300<=x<=450 and 575<=y<=625:
            return "skip"
        elif 550<=x<=700 and 575<= y <= 625:
            return "proceed"
        elif 25<=x<=125 and 25<=y<=75:
            return "save"
        elif 175 <= x <= 275 and 25 <= y <= 75:
            return "reset"
    if findRegion(event.x,event.y) == "dunno":
        data.solutionCube.cube = copy.deepcopy(data.startingCube)
        data.mode = 14
    elif findRegion(event.x,event.y) == "skip":
        data.curPointerInMode14 = 0
        data.isFinishedInMode6 = False
        data.currentStepInMode6 += 1
        if data.currentStepInMode6 == 1:
            data.mode = 7
        else:
            data.mode = data.currentStepInMode6+5
        finishThisStep(data)
        data.startingCube = copy.deepcopy(data.Rubik.cube)
    elif findRegion(event.x,event.y) == "save":
        save(data)
    elif findRegion(event.x,event.y) == "proceed":
        if data.isFinishedInMode6:
            data.curPointerInMode14 = 0
            data.currentStepInMode6 += 1
            if data.currentStepInMode6 == 1:
                data.mode = 7
            else:
                data.mode = data.currentStepInMode6+5

            data.isFinishedInMode6 = False
    elif findRegion(event.x,event.y) == "reset":
        data.Rubik.cube = copy.deepcopy(data.startingCube)

def finishThisStep(data): 
    data.Rubik.cube = copy.deepcopy(data.startingCube)
    for move in data.solution[data.currentStepInMode6-2]:
        makeMove(data.Rubik.cube,move)


def redrawAll6(canvas,data):
    def isFinishedCurrentStep(data):
        if data.currentStepInMode6 == 1:
            cube = data.Rubik.cube
            return cube["front"][4] == cube["front"][1] and cube["back"][4] == cube["back"][1] and cube["left"][4] == cube["left"][1] and cube["right"][4] == cube["right"][1] and [cube["up"][1],cube["up"][3],cube["up"][4],cube["up"][5],cube["up"][7]] == [cube["up"][4]]*5
        elif data.currentStepInMode6 == 2:
            cube = data.Rubik.cube
            return [cube["up"][4]]*9 == cube["up"] and cube["front"][:3] == [cube["front"][4]]*3 and cube["back"][:3] == [cube["back"][4]]*3 and cube["left"][:3] == [cube["left"][4]]*3 and cube["right"][:3] == [cube["right"][4]]*3
        elif data.currentStepInMode6 == 3:
            cube = data.Rubik.cube
            return [cube["down"][4]]*9 == cube["down"] and cube["front"][3:] == [cube["front"][4]]*6 and cube["back"][3:] == [cube["back"][4]]*6 and cube["left"][3:] == [cube["left"][4]]*6 and cube["right"][3:] == [cube["right"][4]]*6
        elif data.currentStepInMode6 == 4:
            cube = data.Rubik.cube
            return [cube["down"][4]]*9 == cube["down"] and cube["front"][3:] == [cube["front"][4]]*6 and cube["back"][3:] == [cube["back"][4]]*6 and cube["left"][3:] == [cube["left"][4]]*6 and cube["right"][3:] == [cube["right"][4]]*6 and [cube["up"][1],cube["up"][3],cube["up"][4],cube["up"][5],cube["up"][7]] == [cube["up"][4]]*5
        elif data.currentStepInMode6 == 5:
            cube = data.Rubik.cube
            return [cube["down"][4]]*9 == cube["down"] and cube["front"][3:] == [cube["front"][4]]*6 and cube["back"][3:] == [cube["back"][4]]*6 and cube["left"][3:] == [cube["left"][4]]*6 and [cube["up"][4]]*9 == cube["up"]
        elif data.currentStepInMode6 == 6:
            cube = data.Rubik.cube
            return [cube["up"][4]]*9 == cube["up"] and [cube["down"][4]]*9 == cube["down"] and [cube["left"][0]]+cube["left"][2:] == [cube["left"][4]]*8 and [cube["right"][0]]+cube["right"][2:] == [cube["right"][4]]*8 and [cube["front"][0]]+cube["front"][2:] == [cube["front"][4]]*8 and [cube["back"][0]]+cube["back"][2:] == [cube["back"][4]]*8
        elif data.currentStepInMode6 == 7:
            cube = data.Rubik.cube
            return [cube["up"][4]]*9 == cube["up"] and [cube["down"][4]]*9 == cube["down"] and [cube["left"][4]]*9 == cube["left"] and [cube["right"][4]]*9 == cube["right"] and [cube["front"][4]]*9 == cube["front"] and [cube["back"][4]]*9 == cube["back"]

    def drawBasics(canvas,data):
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        canvas.create_text((1000,100),text = "Press r to do R or t to do R' or e to do R2",font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,150),text = "Press l to do L or k to do L' or j to do L2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,200),text = "Press b to do B or v to do B' or n to do B2",font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,250),text = "Press f to do F or g to do F' or h to do F2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,300),text = "Press d to do D or s to do D' or a to do D2",font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,350),text = "Press u to do U or y to do U' or i to do U2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,400),text = "Press 2 to do X or 1 to do X' or 3 to do X2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,450),text = "Press 5 to do Y or 4 to do Y' or 6 to do Y2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,500),text = "Press 8 to do Z or 7 to do Z' or 9 to do Z2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,550),text = "Press o to do M or p to do M' or q to do M2", font = "Century 20",fill = "lawn green")
        canvas.create_rectangle((50,575),(200,625),fill = "grey")
        canvas.create_text((125,600),text = "Can't Solve it?",font = "Eurostile 15")
        canvas.create_rectangle((300,575),(450,625),fill = "grey")
        canvas.create_text((375,600),text = "Skip this step",font = "Eurostile 15")
        canvas.create_rectangle((25,25),(125,75),fill=  "grey")
        canvas.create_text((75,50),text = "Save", font = "Eurostile 15")
        canvas.create_rectangle((175,25),(275,75),fill=  "grey")
        canvas.create_text((225,50),text = "Reset", font = "Eurostile 15")

        if isFinishedCurrentStep(data):
            data.isFinishedInMode6 = True
            canvas.create_rectangle((550,575),(700,625),fill = "grey")
            canvas.create_text((625,600),text = "Proceed to next step" if data.currentStepInMode6 != 7 else "Hooray!", font = "Eurostile 15")
            
    drawBasics(canvas,data)
    data.Rubik.startX = 200
    data.Rubik.startY = 200
    data.Rubik.draw(canvas)

###############################
# Mode 7: The Second Step     #
###############################

def mousePressed7(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll7(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["left"] = ["blue","blue","blue","white","blue","white","white","white","white"]
        cube["right"] = ["blue","blue","blue","white","blue","white","white","white","white"]
        cube["front"] = ["blue","blue","blue","white","blue","white","white","white","white"]
        cube["back"] = ["blue","blue","blue","white","blue","white","white","white","white"]
        cube["down"] = ["white"] * 9
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((300,50),text = "Second Step: Finish the top layer", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")


###############################
# Mode 8: The Third Step      #
###############################

def mousePressed8(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll8(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["white"] * 9
        cube["left"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["right"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["front"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["back"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["down"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((460,40),text = "Third Step: Turn the cube upside down and finish the middle layer", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")

##############################
# Mode 9: The Fourth Step    #
##############################

def mousePressed9(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll9(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["white","blue","white","blue","blue","blue","white","blue","white"] 
        cube["left"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["right"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["front"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["back"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["down"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((300,50),text = "Fourth Step: Make a cross on the top", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")


##############################
# Mode 10: The Fifth Step    #
##############################

def mousePressed10(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll10(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["left"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["right"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["front"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["back"] = ["white","white","white","blue","blue","blue","blue","blue","blue"]
        cube["down"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((300,50),text = "Fifth Step: Finish the top", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")

##############################
# Mode 11: The Sixth Step    #
##############################

def mousePressed11(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll11(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["left"] = ["blue","white","blue","blue","blue","blue","blue","blue","blue"]
        cube["right"] = ["blue","white","blue","blue","blue","blue","blue","blue","blue"]
        cube["front"] = ["blue","white","blue","blue","blue","blue","blue","blue","blue"]
        cube["back"] = ["blue","white","blue","blue","blue","blue","blue","blue","blue"]
        cube["down"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((525,50),text = "Sixth Step: Put all the corner blocks of the first layer to the right place", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")

##############################
# Mode 12: The Last Step     #
##############################

def mousePressed12(event,data):
    def findRegion(x,y):
        if 500<=x<=650 and 575<=y<=625:
            return "Try"
    if findRegion(event.x,event.y) == "Try":
        data.mode = 6

def redrawAll12(canvas,data):
    def generateModel():
        cube = dict()
        cube["up"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["left"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["right"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["front"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["back"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        cube["down"] = ["blue","blue","blue","blue","blue","blue","blue","blue","blue"]
        return cube
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text((300,50),text = "Seventh Step: Finish the entire cube", font = "Chalkboard 30",fill = "tomato")
    data.demonstrationCube = Cube(generateModel(),True,500,200,168)
    data.demonstrationCube.draw(canvas)
    canvas.create_rectangle((500,575),(650,625),fill = "grey")
    canvas.create_text((575,600),text = "Give it a try!", font = "Hannotate 20")

#######################################
# Mode 14: The solution demo mode     #
#######################################

def mousePressed14(event,data):
    def findRegion(x,y):
        if 1050<=x<=1250 and 450<=y<=600:
            return "next"
        elif 50 <=x<=250 and 450<=y<=600:
            return "prev"
        elif 50 <= x<=150 and 50 <=y<=100:
            return "back"
    if findRegion(event.x,event.y) == "next":
        if data.curPointerInMode14 < len(data.solution[data.currentStepInMode6-1]) - 1:
            data.curPointerInMode14 += 1
    elif findRegion(event.x,event.y) == "prev":
        if data.curPointerInMode14 > 0:
            data.curPointerInMode14 -= 1
    elif findRegion(event.x,event.y) == "back":
            data.mode = 6

def redrawAll14(canvas,data):
    def drawBasics(canvas,data):
        solution = data.solution[data.currentStepInMode6-1]
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        if data.curPointerInMode14 < len(solution) - 1:
            canvas.create_polygon((1050,500),(1150,500),(1150,450),(1250,525),(1150,600),(1150,550),(1050,550),fill = "salmon")
        if data.curPointerInMode14 > 0:
            canvas.create_polygon((50,525),(150,450),(150,500),(250,500),(250,550),(150,550),(150,600),fill = "salmon")
        canvas.create_text((675,575),text = solution[data.curPointerInMode14],font = "Kaiti 150 bold",fill = "slate blue")
        canvas.create_rectangle((50,50),(150,100),fill = "grey")
        canvas.create_text((100,75),text = "Back",font = "Eurostile 30")
    drawBasics(canvas,data)
    for move in data.solution[data.currentStepInMode6-1][:data.curPointerInMode14+1]:
        makeMove(data.solutionCube.cube,move)
    data.solutionCube.draw(canvas)
    for move in list(reversed(data.solution[data.currentStepInMode6-1][:data.curPointerInMode14+1])):
        makeMove(data.solutionCube.cube,move)
        makeMove(data.solutionCube.cube,move)
        makeMove(data.solutionCube.cube,move)


########################
# Mode 13: The Finale  #
########################

def mousePressed13(event,data):
    def findRegion(x,y):
        if 550<=x<=750 and 625 <= y <= 675:
            return "restart"
    if findRegion(event.x,event.y) == "restart":
        init(data)


def redrawAll13(canvas,data):
    canvas.create_rectangle((0,0),(1300,700),fill = "black")
    canvas.create_text(650,50,text = "Good Job!",font = "Optima 40",fill = "orange red")
    canvas.create_text(650,150,text = "You have just solved the first Rubik's cube in your life!",font = "Optima 40",fill = "orange red")
    canvas.create_text(650,250,text = "Hope you enjoy the whole process!",font = "Optima 40",fill = "orange red")
    canvas.create_text(650,350,text = "Keep practising and see if you can finally beat the world record!",font = "Optima 40",fill = "orange red")
    canvas.create_text(650,450,text = "Current World Record: 5.25s",font = "Optima 40",fill = "orange red")
    canvas.create_text(650,550,text = "Good Luck!",font = "Optima 40",fill = "orange red")
    canvas.create_rectangle((550,625),(750,675),fill = "grey")
    canvas.create_text((650,650),text = "Back To Main Menu",font = "Eurostile 20")

####################################################
# Mode 15: The Intro to button 3 in the main menu  #
####################################################

def mousePressed15(event,data):
    def findRegion(x,y):
        if 550<=x<=750 and 575 <= y <= 625:
            return "Ready"
    if findRegion(event.x,event.y) == "Ready":
        data.mode = 16

def redrawAll15(canvas,data):
    canvas.create_rectangle(0,0,1300,700,fill = "black")
    canvas.create_text(650,50, text = "In this mode,", font = "Chalkboard 30",fill = "violet")
    canvas.create_text(650,150, text = "you will be given a randomly generated cube", font = "Chalkboard 30",fill = "violet")
    canvas.create_text(650,250, text = "Your goal is to make a cross on the top in as few steps as possible (no more than 9 steps)", font = "Chalkboard 30",fill = "violet")
    canvas.create_text(650,350, text = "As you may notice, there is no formula to solve the cross", font = "Chalkboard 30",fill = "violet")
    canvas.create_text(650,450, text = "So the challenge should not be easy", font = "Chalkboard 30",fill = "violet")
    canvas.create_rectangle(550,575,750,625,fill = "grey")
    canvas.create_text(650,600, text = "Ready to Go >", font = "Eurostile 30",fill = "black")

################################################
# Mode 16: Playground for the challenge mode   #
################################################



def keyPressed16(event,data):
    if event.keysym == "r":
        makeMove(data.challengeCubeInMode16.cube,"R")
        data.totalStepsInMode16.append("R")
    elif event.keysym == "t":
        makeMove(data.challengeCubeInMode16.cube,"R'")
        data.totalStepsInMode16.append("R'")
    elif event.keysym == "e":
        makeMove(data.challengeCubeInMode16.cube,"R2")
        data.totalStepsInMode16.append("R2")
    elif event.keysym == "l":
        makeMove(data.challengeCubeInMode16.cube,"L")
        data.totalStepsInMode16.append("L")
    elif event.keysym == "k":
        makeMove(data.challengeCubeInMode16.cube,"L'")
        data.totalStepsInMode16.append("L'")
    elif event.keysym == "j":
        makeMove(data.challengeCubeInMode16.cube,"L2")
        data.totalStepsInMode16.append("L2")
    elif event.keysym == "b":
        makeMove(data.challengeCubeInMode16.cube,"B")
        data.totalStepsInMode16.append("B")
    elif event.keysym == "v":
        makeMove(data.challengeCubeInMode16.cube,"B'")
        data.totalStepsInMode16.append("B'")
    elif event.keysym == "n":
        makeMove(data.challengeCubeInMode16.cube,"B2")
        data.totalStepsInMode16.append("B2")
    elif event.keysym == "f":
        makeMove(data.challengeCubeInMode16.cube,"F")
        data.totalStepsInMode16.append("F")
    elif event.keysym == "g":
        makeMove(data.challengeCubeInMode16.cube,"F'")
        data.totalStepsInMode16.append("F'")
    elif event.keysym == "h":
        makeMove(data.challengeCubeInMode16.cube,"F2")
        data.totalStepsInMode16.append("F2")
    elif event.keysym == "d":
        makeMove(data.challengeCubeInMode16.cube,"D")
        data.totalStepsInMode16.append("D")
    elif event.keysym == "s":
        makeMove(data.challengeCubeInMode16.cube,"D'")
        data.totalStepsInMode16.append("D'")
    elif event.keysym == "a":
        makeMove(data.challengeCubeInMode16.cube,"D2")
        data.totalStepsInMode16.append("D2")
    elif event.keysym == "u":
        makeMove(data.challengeCubeInMode16.cube,"U")
        data.totalStepsInMode16.append("U")
    elif event.keysym == "y":
        makeMove(data.challengeCubeInMode16.cube,"U'")
        data.totalStepsInMode16.append("U'")
    elif event.keysym == "i":
        makeMove(data.challengeCubeInMode16.cube,"U2")
        data.totalStepsInMode16.append("U2")
    elif event.keysym == "2":
        makeMove(data.challengeCubeInMode16.cube,"X")
        data.totalStepsInMode16.append("X")
    elif event.keysym == "1":
        makeMove(data.challengeCubeInMode16.cube,"X'")
        data.totalStepsInMode16.append("X'")
    elif event.keysym == "3":
        makeMove(data.challengeCubeInMode16.cube,"X2")
        data.totalStepsInMode16.append("X2")
    elif event.keysym == "5":
        makeMove(data.challengeCubeInMode16.cube,"Y")
        data.totalStepsInMode16.append("Y")
    elif event.keysym == "4":
        makeMove(data.challengeCubeInMode16.cube,"Y'")
        data.totalStepsInMode16.append("Y'")
    elif event.keysym == "6":
        makeMove(data.challengeCubeInMode16.cube,"Y2")
        data.totalStepsInMode16.append("Y2")
    elif event.keysym == "8":
        makeMove(data.challengeCubeInMode16.cube,"Z")
        data.totalStepsInMode16.append("Z")
    elif event.keysym == "7":
        makeMove(data.challengeCubeInMode16.cube,"Z'")
        data.totalStepsInMode16.append("Z'")
    elif event.keysym == "9":
        makeMove(data.challengeCubeInMode16.cube,"Z2")
        data.totalStepsInMode16.append("Z2")
    elif event.keysym == "o":
        makeMove(data.challengeCubeInMode16.cube,"M")
        data.totalStepsInMode16.append("M")
    elif event.keysym == "p":
        makeMove(data.challengeCubeInMode16.cube,"M'")
        data.totalStepsInMode16.append("M'")
    elif event.keysym == "q":
        makeMove(data.challengeCubeInMode16.cube,"M2")
        data.totalStepsInMode16.append("M2")

def mousePressed16(event,data):
    def findRegion(x,y):
        if 100 <= x <= 250 and 600 <= y <= 650:
            return "solution"
        elif 500 <= x <= 675 and 600 <= y <= 650:
            return "back"
        elif 300 <= x <= 450 and 600 <= y <= 650:
            return "undo"
    def getReversedMove(move):
        if move.endswith("'"):
            return move[0]
        elif move.endswith("2"):
            return move
        elif len(move) == 1:
            return move + "'"

    if findRegion(event.x,event.y) == "solution":
        data.solutionInMode17 = solveCross(copy.deepcopy(data.startingCubeInMode17))
        data.solutionCubeInMode17.cube = copy.deepcopy(data.startingCubeInMode17)
        data.curPointerInMode17 = 0
        data.mode = 17
    elif findRegion(event.x,event.y) == "back":
        init(data)
    elif findRegion(event.x,event.y) == "undo":
        if len(data.totalStepsInMode16) > 0 :
            makeMove(data.challengeCubeInMode16.cube,getReversedMove(data.totalStepsInMode16[-1]))
            data.totalStepsInMode16.pop()

def redrawAll16(canvas,data):
    def drawBasics(canvas,data):
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        canvas.create_text((1000,100),text = "Press r to do R or t to do R' or e to do R2",font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,150),text = "Press l to do L or k to do L' or j to do L2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,200),text = "Press b to do B or v to do B' or n to do B2",font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,250),text = "Press f to do F or g to do F' or h to do F2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,300),text = "Press d to do D or s to do D' or a to do D2",font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,350),text = "Press u to do U or y to do U' or i to do U2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,400),text = "Press 2 to do X or 1 to do X' or 3 to do X2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,450),text = "Press 5 to do Y or 4 to do Y' or 6 to do Y2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,500),text = "Press 8 to do Z or 7 to do Z' or 9 to do Z2", font = "Century 20",fill = "lawn green")
        canvas.create_text((1000,550),text = "Press o to do M or p to do M' or q to do M2", font = "Century 20",fill = "lawn green")
        canvas.create_rectangle((100,600),(250,650),fill = "grey")
        canvas.create_text((175,625),text = "See My Solution",font = "Eurostile 20")
        canvas.create_rectangle((500,600),(675,650),fill = "grey")
        canvas.create_text((587.5,625),text = "Back To Main Menu",font = "Eurostile 20")
        canvas.create_text((20,40),anchor = W, text = "Total Steps: %d" %(len(data.totalStepsInMode16)), font = "Harrington 30",fill = "violet")
        canvas.create_rectangle((300,600),(450,650),fill = "grey")
        canvas.create_text((375,625),text = "Undo",font = "Eurostile 20")

    drawBasics(canvas,data)   
    data.challengeCubeInMode16.draw(canvas)


######################################
# Mode 17: Challenge Solution Demo   #
######################################

def mousePressed17(event,data):
    def findRegion(x,y):
        if 1050<=x<=1250 and 450<=y<=600:
            return "next"
        elif 50 <=x<=250 and 450<=y<=600:
            return "prev"
        elif 50 <= x<=150 and 50 <=y<=100:
            return "back"
    if findRegion(event.x,event.y) == "next":
        if data.curPointerInMode17 < len(data.solutionInMode17) - 1:
            data.curPointerInMode17 += 1
    elif findRegion(event.x,event.y) == "prev":
        if data.curPointerInMode17  > 0:
            data.curPointerInMode17 -= 1
    elif findRegion(event.x,event.y) == "back":
            data.mode = 16

def redrawAll17(canvas,data):
    def drawBasics(canvas,data):
        solution = data.solutionInMode17
        canvas.create_rectangle((0,0),(1300,700),fill = "black")
        if data.curPointerInMode17 < len(solution) - 1:
            canvas.create_polygon((1050,500),(1150,500),(1150,450),(1250,525),(1150,600),(1150,550),(1050,550),fill = "salmon")
        if data.curPointerInMode17 > 0:
            canvas.create_polygon((50,525),(150,450),(150,500),(250,500),(250,550),(150,550),(150,600),fill = "salmon")
        canvas.create_text((675,575),text = solution[data.curPointerInMode17],font = "Kaiti 150 bold",fill = "slate blue")
        canvas.create_rectangle((50,50),(150,100),fill = "grey")
        canvas.create_text((100,75),text = "Back",font = "Eurostile 30")
    drawBasics(canvas,data)
    for move in data.solutionInMode17[:data.curPointerInMode17+1]:
        makeMove(data.solutionCubeInMode17.cube,move)
    data.solutionCubeInMode17.draw(canvas)
    for move in list(reversed(data.solutionInMode17[:data.curPointerInMode17+1])):
        makeMove(data.solutionCubeInMode17.cube,move)
        makeMove(data.solutionCubeInMode17.cube,move)
        makeMove(data.solutionCubeInMode17.cube,move)




####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Create root before calling init (so we can create images in init)
    root = Tk()
    root.wm_title("Virtual Rubik's Cube Tutor")
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 75 # milliseconds
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1300, 700)


#################################################################
#                                                               #
# Citation #1: The run function is cited from the course note.  #
#                                                               #
#################################################################



############################################################################################
#                                                                                          # 
# Citation #2: The line that renames the window in cited from the following web            #
#                                                                                          #
# http://stackoverflow.com/questions/2395431/using-tkinter-in-python-to-edit-the-title-bar #
############################################################################################

