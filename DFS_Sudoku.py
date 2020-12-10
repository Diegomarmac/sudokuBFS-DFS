import copy
import time
import random

class Problem(object):

    def __init__(self, initial):
        self.initial = initial
        self.type = len(initial) # Este programa puede aceptar matrices de 6x6 y de 9x9, aqui definimos cual se va usar 
        self.height = int(self.type/3) # DDefinimos los cuadrantes (2 para 6x6, 3 para 9x9)

    def goal_test(self, state):
        # Definimos el goal test como una sumatoria
        total = sum(range(1, self.type+1))

        # Regresa false si la sumatoria es incoherente para nuestro objetivo
        for row in range(self.type):
            if (len(state[row]) != self.type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(self.type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        # Regresa false si la sumatoria es incoherente para nuestro objetivo
        for column in range(0,self.type,3):
            for row in range(0,self.type,self.height):

                block_total = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
                    return False

        return True

    # Regresamos valores que no se repiten
    def filter_values(self, values, used):
        return [number for number in values if number not in used]

    # Regresamos el primer bloque o coordenada vacia
    def get_spot(self, board, state):
        for row in range(board):
            for column in range(board):
                if state[row][column] == 0:
                    return row, column

    # Filtramos respuestas correctas por renglon
    def filter_row(self, state, row):
        number_set = range(1, self.type+1) # Nos indica que numeros púeden ser validos
        in_row = [number for number in state[row] if (number != 0)]
        options = self.filter_values(number_set, in_row)
        return options

    # Filtramos respuestas correctas por columna
    def filter_col(self, options, state, column):
        in_column = [] # Lista de valores aceptables
        for column_index in range(self.type):
            if state[column_index][column] != 0:
                in_column.append(state[column_index][column])
        options = self.filter_values(options, in_column)
        return options

    # Filtramos respuestas correctas por cuadrante
    def filter_quad(self, options, state, row, column):
        in_block = [] # Lista de valores aceptables
        row_start = int(row/self.height)*self.height
        column_start = int(column/3)*3
        
        for block_row in range(0, self.height):
            for block_column in range(0,3):
                in_block.append(state[row_start + block_row][column_start + block_column])
        options = self.filter_values(options, in_block)
        return options    

    def actions(self, state):
        row,column = self.get_spot(self.type, state) # Obtenemos primer coordenada vacia

        # Desechamos opciones invalidas
        options = self.filter_row(state, row)
        options = self.filter_col(options, state, column)
        options = self.filter_quad(options, state, row, column)

        # loop para opciones validas
        for number in options:
            new_state = copy.deepcopy(state)
            new_state[row][column] = number
            yield new_state

class Node:

    def __init__(self, state):
        self.state = state

    def expand(self, problem):
        # Regresamos una lsita de estados aceptados
        return [Node(state) for state in problem.actions(self.state)]

def DFS(problem):
    start = Node(problem.initial)
    if problem.goal_test(start.state):
        return start.state

    stack = []
    stack.append(start) # nodo inicial a la pila

    while stack:
        node = stack.pop()
        if problem.goal_test(node.state):
            return node.state
        stack.extend(node.expand(problem)) # agregamos estados aceptables a la pila
    return None

def solve_dfs(board):
    print ("\nUsando DFS para generar un sudoku...")
    start_time = time.time()
    problem = Problem(board)
    solution = DFS(problem)
    elapsed_time = time.time() - start_time

    if solution:
        for row in solution:
            for num in range(1,6):
                a = random.randint(1,10) 
                b = random.randint(1,10)
                if a % b == 0:  # si el modulo del numero aleatorio a con b es 0, entonces, en ese indice de i,j, el valor de la mtatriz será 0
                    row[num] = 0
            print (row)
    else:
        print ("ERROR 500")

    
