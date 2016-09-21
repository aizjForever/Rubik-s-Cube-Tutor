import copy,time,random

def solve(cubic):
    hasSolution = False
    times = 0
    while not hasSolution:

        # I would use a dictionary to represent the cube
        # The keys of the dict are different surfaces of the cube.
        # Correspodent to each key is a list, containing 9 values, from upper-left to 
        # bottom- right, which are colors of the blocks on that surface. 



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



        def updateLoc(cube):
            nonlocal corners,edges
            corners = updateCorner(cube)
            edges = updateEdge(cube)

        def updateCenterColor(cube):
            nonlocal TOP,LEFT,RIGHT,FRONT,BACK,DOWN
            TOP = cube["up"][4]
            LEFT = cube["left"][4]
            RIGHT = cube["right"][4]
            FRONT = cube["front"][4]
            BACK = cube["back"][4]
            DOWN = cube["down"][4]

        def makeMove(cube,move):
            nonlocal solution
            solution.append(move)
            if move.startswith("R"):
                R(cube,move)
                updateLoc(cube)
            elif move.startswith("L"):
                L(cube,move)
                updateLoc(cube)
            elif move.startswith("U"):
                U(cube,move)
                updateLoc(cube)
            elif move.startswith("B"):
                B(cube,move)
                updateLoc(cube)
            elif move.startswith("D"):
                D(cube,move)
                updateLoc(cube)
            elif move.startswith("F"):
                F(cube,move)
                updateLoc(cube)
            elif move.startswith("X"):
                X(cube,move)
                updateLoc(cube)
                updateCenterColor(cube)
            elif move.startswith("Y"):
                Y(cube,move)
                updateLoc(cube)
                updateCenterColor(cube)
            elif move.startswith("Z"):
                Z(cube,move)
                updateLoc(cube)
                updateCenterColor(cube)
            elif move.startswith("r"):
                r(cube,move)
                updateLoc(cube)
                updateCenterColor(cube)
            elif move.startswith("M"):
                M(cube,move)
                updateLoc(cube)
                updateCenterColor(cube)
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

        def length(sol):
            result = 0
            for a in sol:
                if not (a.startswith("X") or a.startswith("Y") or a.startswith("Z")):
                    result += 1
            return result



        cube = copy.deepcopy(cubic)
        times+=1
        corners = updateCorner(cube)
        edges = updateEdge(cube)
        TOP = cube["up"][4]
        LEFT = cube["left"][4]
        RIGHT = cube["right"][4]
        FRONT = cube["front"][4]
        BACK = cube["back"][4]
        DOWN = cube["down"][4]
        solutionByStep = []
        solution = []
        deadLoop = False
        startTime = time.time()

        ############################################
        # The first step : make a cross on the top #
        ############################################


        # so my thought is that first I loop through all the middle and down edges,
        # when I hit an edge that belongs to the top, I find its target pos, calc the move
        # until all the middle and down edges do not contain top edges anymore
        # Then I put the top edges in the correct order

        def calcTheOtherEdge(otherColor):
            if otherColor == LEFT:
                return "L"
            elif otherColor == RIGHT:
                return "R"
            elif otherColor == FRONT:
                return "F"
            elif otherColor == BACK:
                return "B"

        def hasTopEdge(edges,topcolor):# return a tuple (True or False, if True: the edge)
            pool = ["FR","FL","BR","BL","DR","DL","DF","DB"]
            random.shuffle(pool)
            for edge in pool:
                if topcolor in edges[edge]:
                    return (True,edge)
            return (False,None)


        def figureOutEdge(edges,srcEdge,topcolor):
            if edges[srcEdge][0] == topcolor:
                otherColor = edges[srcEdge][1]
            else:
                otherColor = edges[srcEdge][0]
            return "U"+calcTheOtherEdge(otherColor)


        def figureOutMove(srcEdge,tgtEdge):

            def toUR(srcEdge):
                if srcEdge == "DR":
                    return random.choice([["R2"],["D'","F'","R"]])

                elif srcEdge == "DF":
                    return random.choice([["F'","R"],["D","R2"]])

                elif srcEdge == "DL":
                    return random.choice([["D2'","R2"],["D","F'","R"]])

                elif srcEdge == "DB":
                    return random.choice([["B","R'"],["D'","R2"]])

                elif srcEdge == "FR":
                    return random.choice([["R"],["F","D","R2"]])

                elif srcEdge == "FL":
                    return random.choice([["F2","R"],["F'","D","R2"]])

                elif srcEdge == "BR":
                    return random.choice([["R'"],["B'","D'","R2"]])

                elif srcEdge == "BL":
                    return random.choice([["B2","R'"],["B","D'","R2"]])

            def toUF(srcEdge):
                if srcEdge == "DR":
                    return random.choice([["R","F'"],["D'","F2"]])

                elif srcEdge == "DF":
                    return random.choice([["F2"],["D","R","F'"]])

                elif srcEdge == "DL":
                    return random.choice([["L'","F"],["D","F2"]])

                elif srcEdge == "DB":
                    return random.choice([["D2","F2"],["D","L'","F"]])

                elif srcEdge == "FR":
                    return random.choice([["F'"],["R'","D'","F2"]])

                elif srcEdge == "FL":
                    return random.choice([["F"],["L","D","F2"]])

                elif srcEdge == "BR":
                    return random.choice([["B'","D2","F2"],["R","D'","F2"]])

                elif srcEdge == "BL":
                    return random.choice([["B","D2","F2"],["L'","D","F2"]])
                    
            def toUL(srcEdge):
                if srcEdge == "DR":
                    return random.choice([["D2","L2"],["D'","F","L'"]])

                elif srcEdge == "DF":
                    return random.choice([["D'","L2"],["F","L'"]])

                elif srcEdge == "DL":
                    return random.choice([["L2"],["D","F","L'"]])

                elif srcEdge == "DB":
                    return random.choice([["D","L2"],["B'","L"]])

                elif srcEdge == "FR":
                    return random.choice([["F2","L'"],["F","D'","L2"]])

                elif srcEdge == "FL":
                    return random.choice([["L'"],["F'","D'","L2"]])

                elif srcEdge == "BR":
                    return random.choice([["B2","L"],["B'","D","L2"]])

                elif srcEdge == "BL":
                    return random.choice([["L"],["B","D","L2"]])
                    
            def toUB(srcEdge):
                if srcEdge == "DR":
                    return random.choice([["R'","B"],["D","B2"]])

                elif srcEdge == "DF":
                    return random.choice([["D2","B2"],["D","R'","B"]])

                elif srcEdge == "DL":
                    return random.choice([["L","B'"],["D'","B2"]])

                elif srcEdge == "DB":
                    return random.choice([["B2"],["D'","R'","B"]])

                elif srcEdge == "FR":
                    return random.choice([["R2","B"],["R'","D","B2"]])

                elif srcEdge == "FL":
                    return random.choice([["L2","B'"],["L","D'","B2"]])

                elif srcEdge == "BR":
                    return random.choice([["B"],["R","D","B2"]])

                elif srcEdge == "BL":
                    return random.choice([["B'"],["L'","D'","B2"]])
                    
            if tgtEdge == "UR":
                return toUR(srcEdge)
            elif tgtEdge == "UF":
                return toUF(srcEdge)
            elif tgtEdge == "UL":
                return toUL(srcEdge)
            elif tgtEdge == "UB":
                return toUB(srcEdge)


        while hasTopEdge(edges,TOP)[0]:
            if time.time() - startTime >= 0.01:
                deadLoop = True
                break
            srcEdge = hasTopEdge(edges,TOP)[1]
            tgtEdge = figureOutEdge(edges,srcEdge,TOP)
            #print(srcEdge,tgtEdge)
            moves = figureOutMove(srcEdge,tgtEdge)
            for move in moves:
                makeMove(cube,move)
        if deadLoop:
            continue

        # So at this point we probably have moved all the below-Top Edge to the top
        # Now we have to check if the right block is on the top
        # We have to put the to-be-identified blok to UR

        for i in range(4):
            if edges["UR"][0] != TOP:
                # which means we have to do something
                for move in ["R'","U","F'","U'"]:
                    makeMove(cube,move)
            # Turn the cube:
            makeMove(cube,"Y'")
            
        while edges["UF"][1] != FRONT:
            makeMove(cube,"Y'")

        def recoverUB(edges):
            nonlocal BACK
            if edges["UL"][1] == BACK:
                return ["L2","D'","B2","D","L2"]
            else:
                return ["R2","D","B2","D'","R2"]

        if edges["UB"][1] != BACK:
            for move in recoverUB(edges):
                makeMove(cube,move)

        if edges["UL"][1] != LEFT:
            for move in ["L2","D2","R2","D2","L2"]:
                makeMove(cube,move)
        def isCompletedFirst(edges):
            nonlocal TOP,FRONT,RIGHT,LEFT,BACK
            if edges["UF"] == [TOP,FRONT] and edges["UR"] == [TOP,RIGHT] and edges["UL"] == [TOP,LEFT] and edges["UB"] == [TOP,BACK]:
                return True
            return False

        solutionByStep.append(solution)
        solution = []
        # By now we have made a cross on the top, and the edges should at its right place.

        ############################################
        # The second step : Finish the first layer #
        ############################################


        # SO basically I am gonna first see the bottom corners if I find a corner block that contains the top color,
        # I should try to find its right place and place it there
        # Then I would see any top corner blocks not in the right direc if yes, try to rotate it to the right place



        # we first let all the top blocks that are at their wrong place be at the bottom

        i = 0
        while i < 4:
            if time.time() - startTime >= 0.01:
                deadLoop = True
                break
            if corners["UFL"] != [TOP,FRONT,LEFT] and (TOP in corners["UFL"]):
                moves = ["L","D","L'"]
                for move in moves:
                    makeMove(cube,move)
            else:
                makeMove(cube,"Y")
                i+=1

        if deadLoop:
            continue

        # Now we are recovering the right corner blocks one by one
        for i in range(4):
            if (corners["UFL"] != [TOP,FRONT,LEFT]): # which means the top block is not here

                # we repeatedly rotate the bottom until the right block appears:
                while not ((TOP in corners["DLF"]) and (FRONT in corners["DLF"]) and (LEFT in corners["DLF"])):
                    if time.time() - startTime >= 0.01:
                        deadLoop = True
                        break
                    makeMove(cube,"D'")
                # we repeated do one thing:
                if corners["DLF"] == [LEFT,TOP,FRONT]:
                    for move in ["L","D","L'"]:
                        makeMove(cube,move)
                elif corners["DLF"] == [FRONT,LEFT,TOP]:
                    for move in ["F'","D'","F"]:
                        makeMove(cube,move)
                else:
                    for move in ["L","D","L'"]*2+["D'"]+["L","D","L'"]:
                        makeMove(cube,move)

            makeMove(cube,"Y")

        if deadLoop:
            continue

        def isCompletedSecond(cube):
            if cube["up"] == [cube["up"][4]]*9 and cube["left"][:3] == [cube["left"][4]] * 3 and cube["right"][:3] == [cube["right"][4]] * 3 and cube["front"][:3] == [cube["front"][4]] * 3 and cube["back"][:3] == [cube["back"][4]] * 3:
                return True
            return False


        # Turn the cube upside down
        makeMove(cube,"X2")

        solutionByStep.append(solution)
        solution = []
        ############################################
        # The third step : Finish the second layer #
        ############################################

        def finishedSecondStep(cube):
            for surface in ["front","left","right","back"]:
                if [cube[surface][4]]*3 != [cube[surface][3],cube[surface][4],cube[surface][5]]:
                    return False
            return True

        def readyToGo(edges): # returns a tuple (True or False; moves or None)
            nonlocal FRONT,TOP,LEFT,RIGHT
            if edges["UF"][1] == FRONT and edges["UF"][0] != TOP:
                color = edges["UF"][0]
                if color == RIGHT:
                    return (True,["U","R","U","R'","U'","F'","U'","F","U"])
                elif color == LEFT:
                    return (True,["U'","L'","U'","L","U","F","U","F'","U'"])
            else:
                return(False,None)

        def isCrossedEdge(edges):
            nonlocal TOP,FRONT,LEFT,RIGHT
            if edges["FR"] == [RIGHT,FRONT]:
                return (True,"right")
            elif edges["FL"] == [LEFT,FRONT]:
                return (True,"left")
            return (False,None)

        while not finishedSecondStep(cube):
            if time.time() - startTime >= 0.01:
                deadLoop = True
                break
            
            if isCrossedEdge(edges)[0]:
                if isCrossedEdge(edges)[1] == "right":
                    for move in ["U","R","U","R'","U'","F'","U'","F","U"]:
                        makeMove(cube,move)
                elif isCrossedEdge(edges)[1] == "left":
                    for move in ["U'","L'","U'","L","U","F","U","F'","U'"]:
                        makeMove(cube,move)
            else:
                i = 0
                while i < 4:
                    if time.time() - startTime >= 0.01:
                        deadLoop = True
                        break
                    if readyToGo(edges)[0]:
                        moves = readyToGo(edges)[1]
                        for move in moves:
                            makeMove(cube,move)
                    else:
                        makeMove(cube,"U'")
                        i+=1
                makeMove(cube,"Y'")
        if deadLoop :
            continue

        def isCompletedThird(cube):
            if cube["down"] == [cube["down"][4]]*9 and cube["left"][3:] == [cube["left"][4]] * 6 and cube["right"][3:] == [cube["right"][4]] * 6 and cube["front"][3:] == [cube["front"][4]] * 6 and cube["back"][3:] == [cube["back"][4]] * 6:
                return True
            return False

        solutionByStep.append(solution)
        solution = []
        #############################################
        # The fourth step : Make a cross on the top #
        #############################################


        # This step maybe optional. In some situation, the cross may already be made
        # The critical step is to identify the pattern on the top

        def isDotPattern(pattern):
            nonlocal TOP
            if pattern[1] != TOP and pattern[3] != TOP and pattern[5] != TOP and pattern[7] != TOP:
                return True
            return False
        def isVerticalLine(pattern):
            nonlocal TOP
            if pattern[1] == TOP and pattern[7] == TOP:
                return True
            else:
                return False
        def isHorizontalLine(pattern):
            nonlocal TOP
            if pattern[3] == TOP and pattern[5] == TOP:
                return True
            else:
                return False
        def isArrow(pattern):
            if pattern[5] == TOP and pattern[7] == TOP:
                return (True,0)
            elif pattern[3] == TOP and pattern[7] == TOP:
                return (True,1)
            elif pattern[3] == TOP and pattern[1] == TOP:
                return (True,2)
            elif pattern[1] == TOP and pattern[5] == TOP:
                return (True,3)
            else:
                return (False,None)

        pattern = cube["up"]
        if [pattern[1],pattern[3],pattern[4],pattern[5],pattern[7]] == [pattern[4]] * 5:
            pass # we do not need to do anything
        elif isVerticalLine(pattern):
            makeMove(cube,"Y")
            for move in ["F","R","U","R'","U'","F'"]:
                makeMove(cube,move)
        elif isHorizontalLine(pattern):
            for move in ["F","R","U","R'","U'","F'"]:
                makeMove(cube,move)
        elif isArrow(pattern)[0]:
            times = isArrow(pattern)[1]
            for i in range(times):
                makeMove(cube,"Y'")
            for move in ["F","R","U","R'","U'","F'"]:
                makeMove(cube,move)
            makeMove(cube,"Y")
            for move in ["F","R","U","R'","U'","F'"]:
                makeMove(cube,move)
        elif isDotPattern(pattern):
            for move in ["F","R","U","R'","U'","F'"]*2:
                makeMove(cube,move)
            makeMove(cube,"Y")
            for move in ["F","R","U","R'","U'","F'"]:
                makeMove(cube,move)
        def isCompletedFourth(cube,edges):
            if isCompletedThird(cube) and [cube["up"][1],cube["up"][3],cube["up"][4],cube["up"][5],cube["up"][7]] == [cube["up"][4]]*5:
                return True
            return False

        solutionByStep.append(solution)
        solution = []
        ###########################################################
        # The fifth step : Finish the top surface after rotation  #
        ###########################################################

        # This step is kinda straightforward
        #Follow all the algorithms listed

        pattern = cube["up"]

        def isLittleFish1(corners,pattern):
            nonlocal TOP
            if pattern[1] == TOP and pattern[3] == TOP and pattern[4] == TOP and pattern[5] == TOP and pattern[7] == TOP and pattern[8] == TOP and corners["ULB"][2] == TOP and corners["UBR"][2] == TOP and corners["UFL"][2] == TOP:
                return True
            return False

        def isLittleFish2(corners,pattern):
            nonlocal TOP
            if pattern[1] == TOP and pattern[2] == TOP and pattern[3] == TOP and pattern[4] == TOP and pattern[5] == TOP and pattern[7] == TOP and corners["ULB"][1] == TOP and corners["URF"][1] == TOP and corners["UFL"][1] == TOP:
                return True
            return False

        def isTank1(corners,pattern):
            nonlocal TOP
            if pattern[1] == TOP and pattern[2] == TOP and pattern[3] == TOP and pattern[4] == TOP and pattern[5] == TOP and pattern[7] == TOP and pattern[8] == TOP and corners["ULB"][2] == TOP and corners["UFL"][1] == TOP: 
                return True
            return False

        def isTank2(corners,pattern):
            nonlocal TOP
            if pattern[1] == TOP and pattern[3] == TOP and pattern[4] == TOP and pattern[5] == TOP and pattern[6] == TOP and pattern[7] == TOP and pattern[8] == TOP and corners["ULB"][2] == TOP and corners["UBR"][1] == TOP: 
                return True
            return False

        def isWeirdShape(corners,pattern):
            nonlocal TOP
            if pattern[1] == TOP and pattern[2] == TOP and pattern[3] == TOP and pattern[4] == TOP and pattern[5] == TOP and pattern[6] == TOP and pattern[7] == TOP and corners["ULB"][1] == TOP and corners["URF"][2] == TOP: 
                return True
            return False

        if pattern.count(TOP) == 5: #which basically means this is a cross
            while not ( (corners["ULB"][2] == TOP and corners["UBR"][1] == TOP and corners["UFL"][1] == TOP and corners["URF"][2] == TOP) or (corners["ULB"][1] == TOP and corners["UBR"][1] == TOP and corners["UFL"][2] == TOP and corners["URF"][2] == TOP) ):
                makeMove(cube,"Y'")
            if corners["ULB"][2] == TOP and corners["UBR"][1] == TOP and corners["UFL"][1] == TOP and corners["URF"][2] == TOP:
                for move in ["R","U","U","R'","U'","R","U","R'","U'","R","U'","R'"]:
                    makeMove(cube,move)
            elif corners["ULB"][1] == TOP and corners["UBR"][1] == TOP and corners["UFL"][2] == TOP and corners["URF"][2] == TOP:
                for move in ["R","U'","U'","R2","U'","R2","U'","R2","U2","R"]:
                    makeMove(cube,move)
        elif pattern.count(TOP) == 6:
            while not (isLittleFish1(corners,pattern) or isLittleFish2(corners,pattern)):
                makeMove(cube,"Y")
            if isLittleFish1(corners,pattern):
                for move in ["R'","U2","R","U","R'","U","R"]:
                    makeMove(cube,move)
            elif isLittleFish2(corners,pattern):
                for move in ["R","U'","U'","R'","U'","R","U'","R'"]:
                    makeMove(cube,move)
        elif pattern.count(TOP) == 7:
            while not (isTank1(corners,pattern) or isTank2(corners,pattern) or isWeirdShape(corners,pattern)):
                makeMove(cube,"Y'")
            if isTank1(corners,pattern):
                for move in ["r","U","R'","U'","r'","F","R","F'"]:
                    makeMove(cube,move)
            elif isTank2(corners,pattern):
                for move in ["R2","D'","R","U'","U'","R'","D","R","U'","U'","R"]:
                    makeMove(cube,move)
            elif isWeirdShape(corners,pattern):
                for move in ["F'","r","U","R'","U'","r'","F","R"]:
                    makeMove(cube,move)
                
        def isCompletedFifth(cube,edges):
            if isCompletedThird(cube) and isCompletedFourth(cube,edges) and cube["up"] == [cube["up"][4]]*9:
                return True
            return False

        solutionByStep.append(solution)
        solution = []
        #########################################################
        # The sixth step : Put the right corners in their place #
        #########################################################



        # Use My Own Algorithm (Formula): "R2","D2","R'","U'","R","D2","R'","U","R'"
        # first do the X'
        # Then examine for the same corners on one edge: if yes -->  do the above formula then X
        # if no -- > do the formula anyway; examine the same; do the above formula then X

        makeMove(cube,"X'")

        isExistTwoCorners = False
        for i in range(4):
            if corners["URF"][1] == corners["DFR"][2]:
                isExistTwoCorners = True
                break
            makeMove(cube,"Z")
        if isExistTwoCorners:
            for move in ["R2","D2","R'","U'","R","D2","R'","U","R'"]:
                makeMove(cube,move)
            makeMove(cube,"X")
        else:
            for move in ["R2","D2","R'","U'","R","D2","R'","U","R'"]:
                makeMove(cube,move)
            for i in range(4):
                if corners["URF"][1] == corners["DFR"][2]:
                    for move in ["R2","D2","R'","U'","R","D2","R'","U","R'"]:
                        makeMove(cube,move)
                    makeMove(cube,"X")
                    break
                makeMove(cube,"Z")

        for i in range(4):
            if corners["UBR"][2] == RIGHT:
                break
            makeMove(cube,"U")
        def isCompletedSixth(cube,edges,corners):
            if isCompletedFifth(cube,edges) and corners["ULB"][1:] == [LEFT,BACK] and corners["UBR"][1:] == [BACK,RIGHT] and corners["UFL"][1:] == [FRONT,LEFT] and corners["URF"][1:] == [RIGHT,FRONT]:
                return True
            return False

        solutionByStep.append(solution)
        solution = []
        #############################################
        # The seventh step : Recover the whole cube #
        #############################################


        # Go with the formula
        # This step maybe optional

        def isFinishedAlltheOperations(cube):
            for surface in cube:
                if cube[surface] != [cube[surface][4]]*9:
                    return False
            return True

        def isClockwise(edges):
            if edges["UB"][1] == BACK and edges["UL"][1] == RIGHT and edges["UR"][1] == FRONT and edges["UF"][1] == LEFT :
                return True
            return False

        def isCounterClockwise(edges):
            if edges["UB"][1] == BACK and edges["UL"][1] == FRONT and edges["UR"][1] == LEFT and edges["UF"][1] == RIGHT :
                return True
            return False

        def isACross(edges):
            if edges["UB"][1] == FRONT and edges["UL"][1] == RIGHT and edges["UR"][1] == LEFT and edges["UF"][1] == BACK :
                return True
            return False

        def isDiagonal(edges):
            if edges["UB"][1] == LEFT and edges["UL"][1] == BACK and edges["UR"][1] == FRONT and edges["UF"][1] == RIGHT :
                return True
            return False

        if isFinishedAlltheOperations(cube):
            pass

        else:
            while not ( isClockwise(edges) or isCounterClockwise(edges) or isACross(edges) or isDiagonal(edges) ):
                makeMove(cube,"Y'")

            if isClockwise(edges):
                for move in ["R2","U","R","U","R'","U'","R'","U'","R'","U","R'"]:
                    makeMove(cube,move)

            elif isCounterClockwise(edges):
                for move in ["R","U'","R","U","R","U","R","U'","R'","U'","R2"]:
                    makeMove(cube,move)

            elif isACross(edges):
                for move in ["M2","U","M2","U2","M2","U",'M2']:
                    makeMove(cube,move)

            elif isDiagonal(edges):
                for move in ["M2","U","M2","U","M'","U2","M2","U2","M'","U2"]:
                    makeMove(cube,move)


        def isCompletedSeventh(cube):
            for surface in cube:
                if cube[surface] != [cube[surface][4]]*9:
                    return False
            return True
        
        if isCompletedSeventh(cube):
            hasSolution = True
        
        solutionByStep.append(solution)
        solution = []
        #############################################
        # We Did it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
        #############################################
    return solutionByStep



