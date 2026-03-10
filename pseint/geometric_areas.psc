Algoritmo geometric_areas
	//declare constants for fixer values that you will use, for example
	definir cuadradro, rectangulo, triangulo, circulo Como Entero
	//declare variables for the dimensions of each figure 
cuadradro <- lado
rectangulo <- baseRec_alturaRec
triangulo <- baseTri_alturaTri
circulo <- radio
//inpust
pi_val <- 3.1416
//For each area in each figure, it prompts the user and displays the required values on the screen.
//processes
cuadradro <- lado * lado
rectangulo <- baseRec * alturaRec
triangulo <- (baseTri * alturaTri) /2
circulo <- pi_val * (radio * radio)
//outpost
escribir"the area of the square is :",area of the square
escribir"The area of the rectangle is :", area of the rectangle
escribir"the area of the triangle is:", area of the triangle
escribir"the area of the circle is:", area of the circle
FinAlgoritmo
