# Define el menú de alimentos
menu = {
    "Pizza Margarita": 8.99,
    "Hamburguesa Clásica": 5.99,
    "Ensalada César": 7.5,
    "Agua Mineral": 1.5
}

# Función para realizar pedidos
def place_order(selected_food, money):
    try:
        # Verificar si el alimento seleccionado está en el menú
        if selected_food not in menu:
            raise ValueError("El alimento seleccionado no está en el menú")
        
        # Verificar si se dispone de suficientes fondos
        total_price = menu[selected_food]
        if total_price > money:
            raise ValueError("No se disponen de suficientes fondos para realizar el pedido")
        
        # Pedido realizado con éxito
        print(f"Pedido realizado con éxito. Alimento seleccionado: {selected_food}, Total a pagar: {total_price} €")
    
    except ValueError as e:
        print(f"Error en el pedido: {e}")

# Función para imprimir el menú
def print_menu():
    print("Menú de Alimentos:")
    # Bucle que recorre el menú
    for food, price in menu.items():
        print(f"{food}: {price} €")

# Imprime el menú
print_menu()

# Pruebo la funcion place_order con diferentes argumentos
place_order("Pizza Margarita", 10)
place_order("Pizza Margarita", 2)
place_order("Sandwich mixto", 10)
