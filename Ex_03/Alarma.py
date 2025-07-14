def alarm_simulator(total_time):
    current_second = 0
    """
    Bucle While: continua ejecutándose hasta que current_second alcance el valor de total_time.
    Variable current_second: incrementa en 1 para simular el paso de un segundo.
    Sentencia continue: para pausar la alarma cada 10 segundos.
    """
    while current_second < total_time:
        current_second += 1
        if current_second % 10 == 0:
            print(f"Alarma pausada en el segundo {current_second}")
            continue
        if current_second > total_time:
            break
        print(f"Alarma activada en el segundo {current_second}")
    print(f"Alarma desactivada después de {total_time} segundos")

# Invoca la función
alarm_simulator(30)