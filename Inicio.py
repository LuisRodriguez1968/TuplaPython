from datetime import datetime

# 1. Función para cargar datos desde el archivo de texto
def cargar_datos_desde_archivo(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:  # Usar UTF-8
            for linea in archivo:
                partes = linea.strip().split(',')
                ciudad = partes[0]
                temperatura = float(partes[1])
                humedad = int(partes[2])
                viento = int(partes[3])
                fecha_hora = datetime.strptime(partes[4], '%Y-%m-%d %H:%M')
                datos.append((ciudad, temperatura, humedad, viento, fecha_hora))
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    return datos

# Cargar los datos desde el archivo
datos_meteorologicos = cargar_datos_desde_archivo("datos_meteorologicos.txt")

# 2. Funciones para manipular y mostrar los datos (igual que antes)
def mostrar_informacion_ciudad(ciudad):
    for registro in datos_meteorologicos:
        if registro[0] == ciudad:
            nombre, temperatura, humedad, viento, fecha_hora = registro
            print(f"Ciudad: {nombre}")
            print(f"Temperatura: {temperatura}°C")
            print(f"Humedad: {humedad}%")
            print(f"Viento: {viento} km/h")
            print(f"Fecha y Hora: {fecha_hora}")
            return
    print(f"No se encontraron datos para la ciudad: {ciudad}")

def ciudad_mas_calor():
    ciudad_caliente = max(datos_meteorologicos, key=lambda registro: registro[1])
    nombre, temperatura, *_ = ciudad_caliente
    print(f"La ciudad más caliente es {nombre} con una temperatura de {temperatura}°C")

def filtrar_por_humedad(min_humedad):
    ciudades_humedas = [registro for registro in datos_meteorologicos if registro[2] > min_humedad]
    print(f"Ciudades con humedad mayor a {min_humedad}%:")
    for nombre, temperatura, humedad, viento, fecha_hora in ciudades_humedas:
        print(f" - {nombre} con {humedad}% de humedad")

def informacion_mas_reciente():
    registro_reciente = max(datos_meteorologicos, key=lambda registro: registro[4])
    nombre, temperatura, humedad, viento, fecha_hora = registro_reciente
    print("Información más reciente registrada:")
    print(f"Ciudad: {nombre}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Humedad: {humedad}%")
    print(f"Viento: {viento} km/h")
    print(f"Fecha y Hora: {fecha_hora}")

# Ejecución de ejemplos
print("Información para Los Ángeles:")
mostrar_informacion_ciudad("Los Ángeles")

print("\nCiudad con mayor temperatura:")
ciudad_mas_calor()

print("\nCiudades con alta humedad (>50%):")
filtrar_por_humedad(50)

print("\nInformación más reciente registrada:")
informacion_mas_reciente()