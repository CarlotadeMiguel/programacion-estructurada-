from cryptography.fernet import Fernet
import hashlib
import hmac

# === Cifrado y Descifrado de Datos ===
def generar_clave():
    return Fernet.generate_key()

def cifrar_datos(clave, datos):
    fernet = Fernet(clave)
    return fernet.encrypt(datos.encode())

def descifrar_datos(clave, datos_cifrados):
    fernet = Fernet(clave)
    return fernet.decrypt(datos_cifrados).decode()

# === Hashing de Contraseñas ===
def hash_contraseña(contraseña):
    # Usamos SHA-256 para hashear la contraseña
    return hashlib.sha256(contraseña.encode()).hexdigest()

def verificar_contraseña(contraseña_ingresada, hash_almacenado):
    hash_ingresado = hashlib.sha256(contraseña_ingresada.encode()).hexdigest()
    return hash_ingresado == hash_almacenado

# === Prevención de Ataques: Verificación con HMAC ===
def verificar_integridad(mensaje, clave_secreta, firma):
    nueva_firma = hmac.new(clave_secreta.encode(), mensaje.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(nueva_firma, firma)

# === Programa Principal ===
if __name__ == "__main__":
    print("=== Cifrado y Descifrado de Datos ===")
    clave = generar_clave()
    print(f"Clave generada: {clave.decode()}")
    datos = "Este es un mensaje secreto"
    datos_cifrados = cifrar_datos(clave, datos)
    print(f"Datos cifrados: {datos_cifrados}")
    datos_descifrados = descifrar_datos(clave, datos_cifrados)
    print(f"Datos descifrados: {datos_descifrados}\n")

    print("=== Hashing de Contraseñas ===")
    contraseña = "mi_contraseña_segura"
    hash_generado = hash_contraseña(contraseña)
    print(f"Contraseña original: {contraseña}")
    print(f"Hash de la contraseña: {hash_generado}")

    # Verificar contraseña ingresada
    contraseña_ingresada = input("Introduce la contraseña para verificar: ")
    es_valida = verificar_contraseña(contraseña_ingresada, hash_generado)
    print(f"¿La contraseña es válida? {'Sí' if es_valida else 'No'}\n")


    print("=== Prevención de Ataques: Verificación con HMAC ===")
    mensaje_original = "Este es un mensaje importante"
    clave_secreta = "clave_secreta"
    
    # Generar la firma del mensaje original
    firma_original = hmac.new(clave_secreta.encode(), mensaje_original.encode(), hashlib.sha256).hexdigest()
    print(f"Mensaje original: {mensaje_original}")
    print(f"Firma generada: {firma_original}")
    
    # Verificar el mensaje original
    es_valido = verificar_integridad(mensaje_original, clave_secreta, firma_original)
    print(f"¿El mensaje es válido? {'Sí' if es_valido else 'No'}")
    
    # Modificar el mensaje
    mensaje_modificado = "Este es un mensaje modificado"
    print(f"\nMensaje modificado: {mensaje_modificado}")
    
    # Verificar el mensaje modificado con la firma original
    es_valido_modificado = verificar_integridad(mensaje_modificado, clave_secreta, firma_original)
    print(f"¿El mensaje es válido? {'Sí' if es_valido_modificado else 'No'}")