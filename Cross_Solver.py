import copy

def solve(edges,TOP,LEFT,RIGHT,FRONT,BACK):
    def formatToStartStatus(edges,TOP,LEFT,RIGHT,FRONT,BACK):
        result = ""
        for edge in edges:
            if edges[edge] == [TOP,FRONT]:
                result += edge + " "
            elif edges[edge] == [FRONT,TOP]:
                result += edge[::-1] + " "
        for edge in edges:
            if edges[edge] == [TOP,LEFT]:
                result += edge + " "
            elif edges[edge] == [LEFT,TOP]:
                result += edge[::-1] + " "
        for edge in edges:
            if edges[edge] == [TOP,BACK]:
                result += edge + " "
            elif edges[edge] == [BACK,TOP]:
                result += edge[::-1] + " "
        for edge in edges:
            if edges[edge] == [TOP,RIGHT]:
                result += edge + " "
            elif edges[edge] == [RIGHT,TOP]:
                result += edge[::-1] + " "
        return result[:-1]

    endStatus = ["UF UL UB UR"]
    startStatus = [formatToStartStatus(edges,TOP,LEFT,RIGHT,FRONT,BACK)]
    startTable = {startStatus[0] : []}
    endTable = {endStatus[0] : []}


    def clockwise(move,face):
        def R(face):
            if face == "U":
                return "B"
            elif face == "B":
                return "D"
            elif face == "D":
                return "F"
            elif face == "F":
                return "U"
        def L(face):
            if face == "U":
                return "F"
            elif face == "F":
                return "D"
            elif face == "D":
                return "B"
            elif face == "B":
                return "U"
        def B(face):
            if face == "U":
                return "L"
            elif face == "L":
                return "D"
            elif face == "D":
                return "R"
            elif face == "R":
                return "U"
        def F(face):
            if face == "U":
                return "R"
            elif face == "R":
                return "D"
            elif face == "D":
                return "L"
            elif face == "L":
                return "U"

        def U(face):
            if face == "B":
                return "R"
            elif face == "R":
                return "F"
            elif face == "F":
                return "L"
            elif face == "L":
                return "B"

        def D(face):
            if face == "B":
                return "L"
            elif face == "L":
                return "F"
            elif face == "F":
                return "R"
            elif face == "R":
                return "B" 

        if move == "R":
            return R(face)
        elif move == "L":
            return L(face)
        elif move == "B":
            return B(face)
        elif move == "F":
            return F(face)
        elif move == "U":
            return U(face)
        elif move == "D":
            return D(face)

    def turn2(move,face):
        a = clockwise(move,face)
        return clockwise(move,a)

    def counterclockwise(move,face):
        a = clockwise(move,face)
        b = clockwise(move,a)
        return clockwise(move,b)

    def makeMove(status,move):
        if move.startswith("R"):
            return turning("R",status,move)
        elif move.startswith("L"):
            return turning("L",status,move)
        elif move.startswith("B"):
            return turning("B",status,move)
        elif move.startswith("F"):
            return turning("F",status,move)
        elif move.startswith("U"):
            return turning("U",status,move)
        elif move.startswith("D"):
            return turning("D",status,move)

    def turning(group,status,move):
        result = ""
        if move == group:
            for block in status.split(" "):
                if group not in block:
                    result += block + " "
                else:
                    if block[0] == group:
                        result += group + clockwise(group,block[1]) + " "
                    else:
                        result += clockwise(group,block[0]) + group + " "
        elif move == (group + "2"):
            for block in status.split(" "):
                if group not in block:
                    result += block + " "
                else:
                    if block[0] == group:
                        result += group+ turn2(group,block[1]) + " "
                    else:
                        result += turn2(group,block[0]) + group + " "
        elif move == (group + "'"):
            for block in status.split(" "):
                if group not in block:
                    result += block + " "
                else:
                    if block[0] == group:
                        result += group+ counterclockwise(group,block[1]) + " "
                    else:
                        result += counterclockwise(group,block[0]) + group + " "        
        return result[:-1]


    def getReversedMove(move):
        if move.endswith("'"):
            return move[0]
        elif move.endswith("2"):
            return move
        elif len(move) == 1:
            return move + "'"

    def Reverse(moves):
        newMoves = list(reversed(moves))
        for i in range(len(newMoves)):
            newMoves[i] = getReversedMove(newMoves[i])
        return newMoves

    def makeSolution1(move,newStatus,status,endTable,startTable):
        return startTable[newStatus] + Reverse(endTable[status] + [move])

    def makeSolution2(move,newStatus,status,newEndTable,startTable):
        return startTable[status] + [move] + Reverse(newEndTable[newStatus])

    def search(endStatus,startStatus,endTable,startTable,depth = 1):
        newEndTable = dict()
        newEndStatus = []
        for status in endStatus:
            temp = status
            for move in ["F","F2","F'","R","R2","R'","L","L'","L2","B","B2","B'","U","U2","U'","D","D2","D'"]:
                temp3 = copy.deepcopy(temp)
                newStatus = makeMove(temp3,move)
                if newStatus not in startTable:
                    newEndStatus.append(newStatus)
                    newEndTable[newStatus] = copy.deepcopy(endTable[status]+[move])
                else:
                    return makeSolution1(move,newStatus,status,endTable,startTable)

        newStartTable = dict()
        newStartStatus = []
        for status in startStatus:
            temp = status
            
            for move in ["F","F2","F'","R","R2","R'","L","L'","L2","B","B2","B'","U","U2","U'","D","D2","D'"]:
                temp3 = copy.deepcopy(temp)
                newStatus = makeMove(temp3,move)
                if newStatus not in newEndTable:
                    newStartStatus.append(newStatus)
                    newStartTable[newStatus] = copy.deepcopy(startTable[status]+[move])
                else:
                    return makeSolution2(move,newStatus,status,newEndTable,startTable)
        return search(newEndStatus,newStartStatus,newEndTable,newStartTable,depth + 1)

    if startTable == endTable : return[]
    else:
        return search(endStatus,startStatus,endTable,startTable)