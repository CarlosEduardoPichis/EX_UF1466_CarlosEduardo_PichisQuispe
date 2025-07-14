# Objectiu / Objetivo

Crea un diccionario menu que represente un menú de alimentos con precios. El menú se compone de:

## » Pizza Margarita : 8.99
## » Hamburguesa Clásica: 5.99
## » Ensalada César: 7.5
## » Agua Mineral: 1.5

    Define una función place_order que tome como argumento: selected_food (un string con el
    alimento) y money (la cantidad de fondos de los que dispone el usuario).
    Imprime el menú de alimentos. Para poder imprimir cada alimento puedes utilizar un bucle for que
    recorra el diccionario.

# Define un sistema de excepciones personalizadas:

## » Si el selected_food no está en el menú, asignar a ValueError la frase: “El alimento
    seleccionado no está en el menú”
## » Si el precio del alimento_seleccionado es superior a la cantidad de dinero, asignar a ValueError
    la frase: “No se disponen de suficientes fondos para realizar el pedido”
## » Si todo es correcto, guarda en la variable total_price el precio del selected_food según el
    menú e imprime la siguiente frase: “Pedido realizado con éxito. Alimento seleccionado:
    {alimento_seleccionado}, Total a pagar: {coste_total} €”
# Define la sentencia except de la excepción imprimiendo la frase: “Error en el pedido: ValueError

    (asignado en las sentencias anteriores)”
    Ejecución del programa: Llama a la función place_order con diferentes argumentos para probar las
    excepciones:
## » alimento_seleccionado = Pizza Margarita, dinero = 10
## » alimento_seleccionado = Pizza Margarita, dinero = 2
## » alimento_seleccionado = Sandwich mixto, dinero = 10