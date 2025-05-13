from datetime import datetime

with open("servidor.log", "a") as archivo:  
   hora_actual = datetime.now().strftime("%H:%M:%S")
   archivo.write(f"Intento de conexión a las {hora_actual}\n") 