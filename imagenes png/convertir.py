import os
from PIL import Image

def optimizar_a_webp(directorio=".", calidad=80):
    # Recorrer todos los archivos en el directorio dado
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(".png"):
            ruta_png = os.path.join(directorio, archivo)
            
            # Crear el nuevo nombre de archivo con extensión .webp
            nombre_sin_ext = os.path.splitext(archivo)[0]
            ruta_webp = os.path.join(directorio, f"{nombre_sin_ext}.webp")
            
            try:
                # Abrir la imagen original y guardarla como WebP
                with Image.open(ruta_png) as img:
                    # Convertir a RGB si la imagen tiene paleta de colores con transparencia (opcional pero recomendado)
                    if img.mode != "RGBA" and img.mode != "RGB":
                        img = img.convert("RGBA")
                        
                    img.save(ruta_webp, "webp", quality=calidad)
                print(f"✅ Convertido: {archivo} -> {nombre_sin_ext}.webp")
            except Exception as e:
                print(f"❌ Error al convertir {archivo}: {e}")

# Ejecutar la función en la carpeta actual con una calidad del 80%
if __name__ == "__main__":
    print("Iniciando conversión...")
    optimizar_a_webp(".", calidad=80)
    print("¡Proceso terminado!")