import copy
def updateCorner(cube):
            result = dict()
            # First Update Corner Block:
            result["ULB"] = [cube["up"][0],cube["left"][0],cube["back"][2]]
            result["UBR"] = [cube["up"][2],cube["back"][0],cube["right"][2]]
            result["UFL"] = [cube["up"][6],cube["front"][0],cube["left"][2]]
            result["URF"] = [cube["up"][8],cube["right"][0],cube["front"][2]]
            result["DFR"] = [cube["down"][2],cube["front"][8],cube["right"][6]]
            result["DLF"] = [cube["down"][0],cube["left"][8],cube["front"][6]]
            result["DBL"] = [cube["down"][6],cube["back"][8],cube["left"][6]]
            result["DRB"] = [cube["down"][8],cube["right"][8],cube["back"][6]]
            return result

def updateEdge(cube):
    result = dict()
    result["UR"] = [cube["up"][5],cube["right"][1]]
    result["UF"] = [cube["up"][7],cube["front"][1]]
    result["UL"] = [cube["up"][3],cube["left"][1]]
    result["UB"] = [cube["up"][1],cube["back"][1]]
    result["DR"] = [cube["down"][5],cube["right"][7]]
    result["DF"] = [cube["down"][1],cube["front"][7]]
    result["DL"] = [cube["down"][3],cube["left"][7]]
    result["DB"] = [cube["down"][7],cube["back"][7]]
    result["FR"] = [cube["front"][5],cube["right"][3]]
    result["FL"] = [cube["front"][3],cube["left"][5]]
    result["BR"] = [cube["back"][3],cube["right"][5]]
    result["BL"] = [cube["back"][5],cube["left"][3]]
    return result
    
def makeMove(cube,move):
    if move.startswith("R"):
        R(cube,move)
    elif move.startswith("L"):
        L(cube,move)
    elif move.startswith("U"):
        U(cube,move)
    elif move.startswith("B"):
        B(cube,move)
    elif move.startswith("D"):
        D(cube,move)
    elif move.startswith("F"):
        F(cube,move)
    elif move.startswith("X"):
        X(cube,move)
    elif move.startswith("Y"):
        Y(cube,move)
    elif move.startswith("Z"):
        Z(cube,move)
    elif move.startswith("r"):
        r(cube,move)
    elif move.startswith("M"):
        M(cube,move)
    return
def M(cube,move):
    def rotate(cube):
        front = copy.deepcopy(cube["front"])
        up = copy.deepcopy(cube["up"])
        back= copy.deepcopy(cube["back"])
        down = copy.deepcopy(cube["down"])
        cube["front"][1],cube["front"][4],cube["front"][7] = up[1],up[4],up[7]
        cube["down"][1],cube["down"][4],cube["down"][7] = front[1],front[4],front[7]
        cube["back"][1],cube["back"][4],cube["back"][7] = down[7],down[4],down[1]
        cube["up"][1],cube["up"][4],cube["up"][7] = back[7],back[4],back[1]

    if move == "M":
        rotate(cube)
    elif move == "M2":
        rotate(cube)
        rotate(cube)
    elif move == "M'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return  
def r(cube,move):
    def rotate(cube):
       M(cube,"M'")
       R(cube,"R")

    if move == "r":
        rotate(cube)
    elif move == "r2":
        rotate(cube)
        rotate(cube)
    elif move == "r'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return  
def Z(cube,move):
    def rotate(cube):
        L = cube["front"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["front"] = L
        L = cube["back"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[2],L[5],L[8],L[1],L[4],L[7],L[0],L[3],L[6]
        cube["back"] = L
        up = cube["up"]
        right = cube["right"]
        down = cube["down"]
        left = cube["left"]
        up[0],up[1],up[2],up[3],up[4],up[5],up[6],up[7],up[8] = up[6],up[3],up[0],up[7],up[4],up[1],up[8],up[5],up[2]
        cube["right"] = up
        right[0],right[1],right[2],right[3],right[4],right[5],right[6],right[7],right[8] = right[6],right[3],right[0],right[7],right[4],right[1],right[8],right[5],right[2]
        cube["down"] = right
        down[0],down[1],down[2],down[3],down[4],down[5],down[6],down[7],down[8] = down[6],down[3],down[0],down[7],down[4],down[1],down[8],down[5],down[2]
        cube["left"] = down
        left[0],left[1],left[2],left[3],left[4],left[5],left[6],left[7],left[8] = left[6],left[3],left[0],left[7],left[4],left[1],left[8],left[5],left[2]
        cube["up"] = left
    if move == "Z":
        rotate(cube)
    elif move == "Z2":
        rotate(cube)
        rotate(cube)
    elif move == "Z'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return 

def Y(cube,move):
    def rotate(cube):
        L = cube["up"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["up"] = L
        L = cube["down"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[2],L[5],L[8],L[1],L[4],L[7],L[0],L[3],L[6]
        cube["down"] = L
        front = cube["front"]
        left = cube["left"]
        back = cube["back"]
        right = cube["right"]
        cube["front"] = right
        cube["left"] = front
        cube["back"] = left
        cube['right'] = back
    if move == "Y":
        rotate(cube)
    elif move == "Y2":
        rotate(cube)
        rotate(cube)
    elif move == "Y'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return 

def X(cube,move):
    def rotate(cube):
        L = cube["right"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["right"] = L
        L = cube["left"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[2],L[5],L[8],L[1],L[4],L[7],L[0],L[3],L[6]
        cube["left"] = L
        front = cube["front"]
        up = cube["up"]
        back = cube["back"]
        down = cube["down"]
        cube["front"] = down
        cube["up"] = front
        up[0],up[1],up[2],up[3],up[4],up[5],up[6],up[7],up[8] = up[8],up[7],up[6],up[5],up[4],up[3],up[2],up[1],up[0]
        cube["back"] = up
        back[0],back[1],back[2],back[3],back[4],back[5],back[6],back[7],back[8] = back[8],back[7],back[6],back[5],back[4],back[3],back[2],back[1],back[0]
        cube['down'] = back
    if move == "X":
        rotate(cube)
    elif move == "X2":
        rotate(cube)
        rotate(cube)
    elif move == "X'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return

def R(cube,move):
    def rotate(cube): 
        cube["front"][2],cube["up"][2],cube["back"][6],cube["down"][2] = cube["down"][2],cube["front"][2],cube["up"][2],cube["back"][6]
        cube["front"][5],cube["up"][5],cube["back"][3],cube["down"][5] = cube["down"][5],cube["front"][5],cube["up"][5],cube["back"][3]
        cube["front"][8],cube["up"][8],cube["back"][0],cube["down"][8] = cube["down"][8],cube["front"][8],cube["up"][8],cube["back"][0]
        L = cube["right"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["right"] = L
    if move == "R":
        rotate(cube)
    elif move == "R2":
        rotate(cube)
        rotate(cube)
    elif move == "R'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return 

def L(cube,move):
    def rotate(cube):
        cube["front"][0],cube["down"][0], cube["back"][8],cube["up"][0] = cube["up"][0],cube["front"][0],cube["down"][0],cube["back"][8]
        cube["front"][3],cube["down"][3], cube["back"][5],cube["up"][3] = cube["up"][3],cube["front"][3],cube["down"][3],cube["back"][5]
        cube["front"][6],cube["down"][6], cube["back"][2],cube["up"][6] = cube["up"][6],cube["front"][6],cube["down"][6],cube["back"][2]
        L = cube["left"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["left"] = L
    if move == "L":
        rotate(cube)
    elif move == "L2":
        rotate(cube)
        rotate(cube)
    elif move == "L'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return

def U(cube,move):
    def rotate(cube):
        cube["front"][0],cube["left"][0], cube["back"][0],cube["right"][0] = cube["right"][0],cube["front"][0],cube["left"][0],cube["back"][0]
        cube["front"][1],cube["left"][1], cube["back"][1],cube["right"][1] = cube["right"][1],cube["front"][1],cube["left"][1],cube["back"][1]
        cube["front"][2],cube["left"][2], cube["back"][2],cube["right"][2] = cube["right"][2],cube["front"][2],cube["left"][2],cube["back"][2]
        L = cube["up"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["up"] = L
    if move == "U":
        rotate(cube)
    elif move == "U2":
        rotate(cube)
        rotate(cube)
    elif move == "U'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return

def B(cube,move):
    def rotate(cube):
        cube["right"][2],cube["up"][0], cube["left"][6],cube["down"][8] = cube["down"][8],cube["right"][2],cube["up"][0],cube["left"][6]
        cube["right"][5],cube["up"][1], cube["left"][3],cube["down"][7] = cube["down"][7],cube["right"][5],cube["up"][1],cube["left"][3]
        cube["right"][8],cube["up"][2], cube["left"][0],cube["down"][6] = cube["down"][6],cube["right"][8],cube["up"][2],cube["left"][0]
        L = cube["back"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["back"] = L
    if move == "B":
        rotate(cube)
    elif move == "B2":
        rotate(cube)
        rotate(cube)
    elif move == "B'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return

def D(cube,move):
    def rotate(cube):
        cube["left"][8],cube["front"][8], cube["right"][8],cube["back"][8] = cube["back"][8],cube["left"][8],cube["front"][8],cube["right"][8]
        cube["left"][7],cube["front"][7], cube["right"][7],cube["back"][7] = cube["back"][7],cube["left"][7],cube["front"][7],cube["right"][7]
        cube["left"][6],cube["front"][6], cube["right"][6],cube["back"][6] = cube["back"][6],cube["left"][6],cube["front"][6],cube["right"][6]
        L = cube["down"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["down"] = L
    if move == "D":
        rotate(cube)
    elif move == "D2":
        rotate(cube)
        rotate(cube)
    elif move == "D'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return

def F(cube,move):
    def rotate(cube):
        cube["left"][2],cube["up"][8],cube["right"][6],cube["down"][0] = cube["down"][0],cube["left"][2],cube["up"][8],cube["right"][6]
        cube["left"][5],cube["up"][7],cube["right"][3],cube["down"][1] = cube["down"][1],cube["left"][5],cube["up"][7],cube["right"][3]
        cube["left"][8],cube["up"][6],cube["right"][0],cube["down"][2] = cube["down"][2],cube["left"][8],cube["up"][6],cube["right"][0]
        L = cube["front"]
        L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8] = L[6],L[3],L[0],L[7],L[4],L[1],L[8],L[5],L[2]
        cube["front"] = L
    if move == "F":
        rotate(cube)
    elif move == "F2":
        rotate(cube)
        rotate(cube)
    elif move == "F'":
        rotate(cube)
        rotate(cube)
        rotate(cube)
    return