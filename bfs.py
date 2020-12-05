from collections import deque
# Creamos el grafo ESTO PUEDE IR EN UN FILE.PY DISTINTO
graph                  = {}
graph["raiz"]          = ["nivelAunoF", "nivelAdos", "nivelAtres"] # le puse una F a algunos nodos para que no acabe ahí el algoritmo
graph["nivelAdos"]     = ["nivelBunoF", "nivelBdos"]
graph["nivelAunoF"]    = ["nivelBtres", "nivelBcuatro"] # quiero que acabe en nivelBcuatro solo para asegurarme que está leyendo todo
graph["nivelAtres"]    = []
graph["nivelBunoF"]    = []
graph["nivelBdos"]     = []
graph["nivelBtres"]    = []
graph["nivelBcuatro"]  = []

# definimos node_is_terminal supongo que esto puede ir en un file.py distinto
# Aquí van las reglas de busqueda... en teoría aquí van las reglas del sudoku... toDo: revisar y hacer pruebas
def node_is_terminal(nodeLetters):
    return nodeLetters[-1] == 'o' # funcion tonta, solo revisa si el nodo termina en o

# BFS ! sería útil ponerlo en un file.py distinto ?
def search(node):
    search_queue = deque()
    search_queue += graph[node]
    searched = [] # lsita de ya revisados
    while search_queue: # Mientras que el queue esté vacío
        youAreHere = search_queue.popleft() # Tomamos el primer nodo en el queue
        if not youAreHere in searched: # solo hacemos la busqueda si ese nodo NO ha sido visitado antes
            if node_is_terminal(youAreHere): # Revisamos que sea el nodo que buscamos... en el sudoku que reglas serán ?
                print(f"{youAreHere} es el nodo terminal") # Acabamos ! el nodo objetivo ha sido encontrado
                return True
            else:
                search_queue += graph[youAreHere] # No hemos llegado al final.. añadimos los nodos consecuentes
                searched.append(youAreHere) # para evitar bucles infinitos añadimos el nodo a ya revisado
    return False # ERROR !  JAMAS SE LLEGÓ AL NODO OBJETIVO... en el sudoku... no se llegó a la sumatoria ???? 

# Ahora que arranque el bfs !!!
search("raiz")
