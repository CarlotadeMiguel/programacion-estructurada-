import threading
import multiprocessing
import time

# Función para tareas concurrentes y paralelas
def tarea(nombre, duracion):
    print(f"Iniciando tarea {nombre}")
    time.sleep(duracion)
    print(f"Tarea {nombre} completada en {duracion} segundos")


# Ejemplo de programación concurrente con threading

# Los hilos comparten el mismo espacio de memoria, lo que los hace ligeros.
# Útil para tareas que dependen de I/O (como leer archivos o realizar solicitudes de red).
# En este ejemplo, tres hilos ejecutan la función tarea_concurrente simultáneamente.

def ejemplo_threading():
    print("=== Programación Concurrente con threading ===")
    hilos = []
    for i in range(3):
        hilo = threading.Thread(target=tarea, args=(f"Hilo-{i+1}", i+2))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Todas las tareas concurrentes han finalizado.\n")



# Ejemplo de programación paralela con multiprocessing

# Los procesos tienen su propio espacio de memoria, lo que los hace más pesados pero ideales para tareas que consumen mucha CPU.
# Útil para aprovechar múltiples núcleos del procesador.
# En este ejemplo, tres procesos ejecutan la función tarea_paralela en paralelo.


def ejemplo_multiprocessing():
    print("=== Programación Paralela con multiprocessing ===")
    procesos = []
    for i in range(3):
        proceso = multiprocessing.Process(target=tarea, args=(f"Proceso-{i+1}", i+2))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    print("Todas las tareas paralelas han finalizado.\n")

if __name__ == "__main__":
    # Ejecutar ejemplos
    ejemplo_threading()
    ejemplo_multiprocessing()