var tablero = [
    [0,0,0,9,0,0,0,0,6],
    [5,0,0,0,0,0,0,0,9],
    [0,4,0,0,0,0,1,0,0],
    [0,0,6,0,3,1,9,0,8],
    [2,0,0,5,0,9,0,0,7],
    [8,0,3,7,4,0,2,0,0],
    [0,0,8,0,0,0,0,5,0],
    [9,0,0,0,0,0,0,0,4],
    [6,0,0,0,0,5,0,0,0]
]; // tablero de sudoku FIN

function siguienteEspacioVacio(tablero){
    for(var i = 0; i < 9; i++ ){
        for(var j = 0; j < 9; j++){
            if(tablero[i][j] === 0)
                return [i,j];
        }
    }
    return [-1, -1]; // En caso de que no haya vacios, nos regresará [-1,-1]
};

function revisarRenglon(tablero, renglon, valor){
    for(var i = 0; i < tablero[renglon].length; i++){
        if(tablero[renglon][1] === valor){
            return false;
        }
    }
    return true;
};
// esta funcion toma como parametro el tablero, el renglon que vamos a revisar y un valor que vamos a revisar. Regresa falso si el valor se repite en ese renglon

function revisarColumna(tablero, columna, valor){
    for(var i = 0; i < tablero.length; i++){
        if(tablero[i][columna] === valor){
            return false;
        }
    }
    return true;
}; // lo mismo que revisarRenglon pero con columnas

// Ahora, para "dividir" el problema, vamos a revisar por celdas de 3x3
// Revisamos que no se repitan valores
function revisarCelda(tablero, renglon, columna, valor){
    boxColumna = Math.floor(columna/3) * 3;
    boxRenglon = Math.floor(renglon/3) * 3;

    for(var r = 0; r < 3; r++){
        for(var c = 0; c < 3; c++){
            if(tablero[boxRenglon + r][boxColumna + c] === valor)
                return false;
        }
    }
    return true;
};

// Genial, ahora vamos a poner esto en orden para probar todos los posibles casos
function revisarValores(tablero, renglon, columna, valor){
    if(revisarRenglon(tablero, renglon, valor) &&
       revisarColumna(tablero, columna, valor) &&
       revisarCelda(tablero, renglon, columna, valor) ){return true;}
    return false;
}

// Ahora vamos a generar el sudoku

function generador(tablero){
    let lugarVacio = siguienteEspacioVacio(tablero);
    let renglon = lugarVacio[0];
    let columna = lugarVacio[1];

    // si no hay espacios vacios
    if (renglon === -1){
        return tablero;
    }

    for(let num = 1; num <= 9;num++){
        if(revisarValores(tablero, renglon, columna, num) ){
            tablero[renglon][columna] = num;
            generador(tablero);
        }
    }

    if(siguienteEspacioVacio(tablero)[0] !== -1 ) //si no me regresa la bandera de que ya no hay espacios vacios 
        tablero[renglon][columna] = 0;


    return tablero;
}

generador(tablero);
console.log(tablero[0])

