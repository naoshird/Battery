import psutil
import time

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if percent == 100 and plugged:
        # La batería está al 100% y está conectada a la corriente
        # No transmitir corriente eléctrica
        print("La batería está completamente cargada. No se transmite corriente.")
    elif percent <= 10 and not plugged:
        # La batería está al 10% o menos y no está conectada a la corriente
        # Transmitir corriente eléctrica
        print("La batería está al 10% o menos. Se transmite corriente.")
    else:
        # En cualquier otro caso, no se hace nada
        pass

    # Esperar un tiempo antes de volver a revisar el estado de la batería
    time.sleep(60)
