# Objectiu / Objetivo

    Define una función llamada alarm_simulator que acepte un parámetro: total_time. Este parámetro
    indica la cantidad total de “segundos” (iteraciones) que el simulador debe ejecutarse.
    Dentro de la función, inicializa una variable current_second en 0. Esta variable funcionará como
    contador para simular el paso del tiempo.
    Implementa un bucle while que continúe ejecutándose hasta que current_second alcance el valor de
    total_time.

    En cada iteración del bucle, incrementa current_second en 1 para simular el paso de un segundo.
    Utiliza la sentencia continue para “pausar” la alarma cada 10 “segundos”.
    Asegúrate de imprimir un mensaje cada vez que se “pausa” la alarma, indicando que se ha omitido un
    segundo específico.

    Imprime un mensaje en cada iteración que no se pausa para indicar que la alarma está activada y para
    mostrar el segundo actual.
    Emplea la sentencia break para terminar el bucle y finalizar la simulación de la alarma cuando
    current_second alcance el valor de total_time
    Imprime un mensaje final para indicar que la alarma se ha desactivado, especificando el total de
    “segundos” que estuvo activa.

# Invoca la función alarm_simulator