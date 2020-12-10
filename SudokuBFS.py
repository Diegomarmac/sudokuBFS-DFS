import queue
from copy import deepcopy
import random

# Tableros para hacer pruebas
# si lo dejamos en ceros pasa algo interesante....
test1 = [[1,5,0,0,4,0],
         [2,4,0,0,5,6],
         [4,0,0,0,0,3],
         [0,0,0,0,0,4],
         [6,3,0,0,2,0],
         [0,2,0,0,3,1]]

test2 = [[0,0,0,0,4,0],
         [5,6,0,0,0,0],
         [3,0,2,6,5,4],
         [0,4,0,2,0,3],
         [4,0,0,0,6,5],
         [1,5,6,0,0,0]]

test3 = [[0,0,0,8,4,0,6,5,0],
         [0,8,0,0,0,0,0,0,9],
         [0,0,0,0,0,5,2,0,1],
         [0,3,4,0,7,0,5,0,6],
         [0,6,0,2,5,1,0,3,0],
         [5,0,9,0,6,0,7,2,0],
         [1,0,8,5,0,0,0,0,0],
         [6,0,0,0,0,0,0,4,0],
         [0,5,2,0,8,6,0,0,0]]

class Node(object):
	def __init__(self, state, children):
		self.state = state
		self.children = []

	def appendChild(self, newState):
		self.children.append(newState)

	def getState(self):
		return self.state

# Aquí revisamos si ya acabamos
def goal_test(state):
    for i in range(0,len(state)):
        localCount = 0
        for j in range(0, len(state)):
            localCount += state[i][j]
        if(localCount != fact_sum(len(state))):
            return False
    ##Revisamos las columnas
    for i in range(0,len(state)):
        localCount = 0
        for j in range(0, len(state)):
            localCount += state[j][i]
        if(localCount != fact_sum(len(state))):
            return False
    ##C REvisamos por espacios de 3 si están llenados apropiadamente
    if(len(state) == 6):
        for i in range(0,6,2):
            if(not checkGrid(state,i,0)):
                return False
            if(not checkGrid(state,i,3)):
                return False
    elif(len(state)==9):
        for horiz in range(0,3):
            for vert in range(0,3):
                localCount = 0
                for i in range(0,3):
                    for j in range(0,3):
                        localCount += state[(horiz*3)+i][(vert*3)+j]
                if(localCount != 45):
                    return False
    return True

def fact_sum(hold):
    returnInt = 0
    while(hold != 0):
        returnInt += hold
        hold = hold - 1
    return returnInt

def checkGrid(state, x, y):
    returnGrid = []
    returnGrid.append(state[x][y])
    returnGrid.append(state[x][y+1])
    returnGrid.append(state[x][y+2])
    returnGrid.append(state[x+1][y])
    returnGrid.append(state[x+1][y+1])
    returnGrid.append(state[x+1][y+2])
    return sum(returnGrid) == 21

def getValues(state):
	possibleValues=[]
	for i in range(0, len(state)):
		for j in range(0,len(state)):
			if(state[i][j] == 0):
				for k in range(1, len(state)+1):
					if(checkRow(state, i, k) and checkVertical(state, j, k)):
						possibleValues.append(k)
				return possibleValues
	return None

def checkVertical(state, column, value):
	for i in range(0,len(state)):
		if(state[i][column] == value):
			return False
	return True

def checkRow(state, row, value):
	if value in state[row]:
		return False
	return True


def createBoards(state, valueQueue):
	boards = []
	x = 0
	y = 0
	find = False
	for i in range(0, len(state)):
		for j in range(0,len(state)):
			if(state[i][j] == 0):
				x = i
				y = j
				find = True
				break
		if find:
			break
	for i in valueQueue:
		state[x][y] = i
		boards.append(deepcopy(state))
	return boards

def printBoard(state):
    for i in range(0, len(state)):
        print("\n")
        for j in range(0, len(state)):
            a = random.randint(1,10) 
            b = random.randint(1,10)
            if a % b == 0:  # si el modulo del numero aleatorio a con b es 0, entonces, en ese indice de i,j, el valor de la mtatriz será 0
                state[i][j] = 0
            
            print(state[i][j], end="")
    print("\n---------------------------")

def breadth_first_search(state):
    # Revisamos si el tablero comple con el objetivo
    firstNode = Node(state, [])


    if goal_test(firstNode.state):
        return firstNode.state
    # Creamos una cola para almacenar todos los nodos de cada nivel
    frontier=queue.Queue()
    frontier.put(firstNode)

    # Loop por todos los nodos revisando el objetivo
    while frontier:
        # quitamos desde frontier, para probar
        localChild = frontier.get()
        localState = localChild.state

        possibleValues = getValues(localState)
        if (possibleValues == None):
        	print("No solution found")
        	return
        localChild.children = createBoards(localState, possibleValues)
        # Loop por todos los hijos del nodo BFS
        for child in localChild.children:
            # si un hijo del nodo conbcuerda con el objetivo
            if goal_test(child):
                return child
            # añadimos cada nuevo hijo a frontier
            frontier.put(Node(child,[]))
    return None

if __name__ == '__main__':
    printBoard(breadth_first_search(test1))
    printBoard(breadth_first_search(test2))
    printBoard(breadth_first_search(test3))