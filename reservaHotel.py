### 1. Clase `Hotel`
"""
- *Atributos*:
    - `nombre` : nombre del hotel.
    - `ubicación` : dirección del hotel.
    - `habitaciones` : lista de habitaciones disponibles en el hotel.
    
- *Métodos* : 
    - `__init__ : constructor de la clase.
    - `añadir_habitación` : añade una habitación al hotel.
    - `eliminar_habitación` : elimina una habitación del hotel.
    - `buscar_habitación` : busca habitaciones por tipo o precio.
    - `mostrar_info` : devuelve información básica del hotel.
"""

### 2. Clase `Habitación`
"""
- *Atributos*:
    - `numero`: número de la habitación.
    - `tipo` : tipo de la habitación (ej. simple, doble, suite).
    - `precio` : precio por noche.
    - `disponible` : estado de disponibilidad de la habitación.

- *Métodos*:
    - `__init__` : constructor de la clase.
    - `actualizar_disponibilidad: cambia el estado de disponibilidad de la habitación.
    - `mostrar_info` : muestra la información de la habitación.
"""

### 3. Clase `Reserva`
"""
- *Atributos*:
    - `id_reserva`: identificador único de la reserva.
    - `habitacion` : la habitación reservada.
    - `cliente` : el cliente que realiza la reserva. 
    - `fecha_entrada` : fecha de entrada.
    - `fecha_salida` : fecha de salida.
    - `estado` : estado de la reserva (confirmada, pendiente, cancelada).
    
- *Métodos*: 
    - `__init__` : constructor de la clase.
    - `modificador_reserva` : permite cambiar las fechas de la reserva.
    - `cancelar_reserva` : cancela la reserva.
"""

### 4. Clase `Cliente`
"""
- *Atributos*:
    - `id_cliente` : identificador único para cada cliente.
    - `nombre` : nombre del cliente.
    - `email` : correo electrónico del cliente.
    - `reservas` : lista de reservas realizadas por el cliente.
    
- *Métodos*: 
    - `__init__` : constructor de la clase.
    - `realizar_reserva` : método para que el cliente realice una nueva reserva.
    - `cancelar_reserva` : método para que el cliente cancele una reserva existente.
"""

### 5. Clase `SistemaReservas`
"""
- *Atributos* :
    - `hoteles` : lista de hoteles en el sistema.
    - `clientes` : lista de clientes registrados.
    
- *Métodos*:
    - `__init__` : constructor de la clase.
    - `registrar_hotel` : añade un nuevo hotel del sistema.
    - `eliminar_hotel` : elimina un hotel del sistema.
    - `registrar_cliente` : añade un nuevo cliente del sistema.
    - `eliminar_cliente` : elimina un cliente del sistema.
    - `buscar_hoteles` : busca hoteles por ubicación o nombre.
    - `listar_reservas` : muestra todas las reservas realizadas.
"""

class Hotel: 
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = []
        
    def anadir_habitacion(self, habitacion): 
        self.habitacion.append(habitacion)
        print(f"Habitación  {habitacion.numero} añadida al hotel {self.nombre}.")
        
    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)
        print(f"Habitación {habitacion.numero} eliminada del hotel {self.nombre}")
        
    def buscar_habitacion(self, tipo = None, precio_max = None): 
        resultados = []
        for habitacion in self.habitaciones:
            if (tipo is None or habitacion.tipo == tipo) and (precio_max is None or habitacion.precio <= precio_max):
                resultados.append(habitacion)
        return resultados
    
    def mostrar_info(self):
        return f"Hotel {self.nombre}, ubicado en {self.ubicacion}"
    
class Habitacion: 
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True
        
    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible
        estado = "disponible" if disponible else "no disponible"
        print(f"Habitación {self.numero} ahora está {estado}")
        
    def mostrar_info(self):
        return f"Habitación {self.numero}, Tipo: {self.tipo}, Precio: {self.precio} por noche."
    
class Reserva:
    def __init__(self, id_reserva, habitacion, cliente, fecha_entrada, fecha_salida):
        self.id_reserva = id_reserva
        self.habitacion = habitacion
        self.cliente = cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = "pendiente"
        
    def modificar_reserva(self, nueva_fecha_entrada, nueva_fecha_salida):
        self.fecha_entrada = nueva_fecha_entrada
        self.fecha_salida = nueva_fecha_salida
        print(f"""
              Reserva {self.id_reserva} modificada para el período {self.fecha_entrada} a
              {self.fecha_salida}.
              """)
        
    def cancelar_reserva(self):
        self.estado = "cancelada"
        print(f"Reserva {self.id_reserva} cancelada.")

class SistemaReservas: 
    def __init__(self):
        self.hoteles = []
        self.clientes = []
    
    def registrar_hotel(self, hotel):
        self.hoteles.append(hotel)
        print(f"Hotel {hotel.nombre} registrado en el sistema.")
        
    def eliminar_hotel(self, hotel):
        self.hoteles.remove(hotel)
        print(f"Hotel {hotel.nombre} eliminado del sistema.")
        
    def registrar_hotel(self, cliente):
        self.clientes.remove(cliente)
        print(f"Cliente {cliente.nombre} registrado en el sistema.")
    
    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)
        print(f"Cliente {cliente.nombre} eliminado del sistema.")
        
    def buscar_hoteles(self, ubicacion = None, nombre = None): 
        resultados = []
        for hotel in self.hoteles: 
            if (ubicacion is None or hotel.ubicacion == ubicacion) and (nombre is None or hotel.nombre == nombre):
                resultados.append(hotel)
        return resultados
    
    def listar_reservas(self):
        for cliente in self.clientes:
            for reserva in cliente.reservas:
                print(f"""Reserva {reserva.id_reserva} para el cliente {cliente.nombre},
                      para las fechas desde: {reserva.fecha_entrada}, hasta: {reserva.fecha_salida}
                      Estado: {reserva.estado}.""")

# Crear una instancia del sistema de reservas
sistema = SistemaReservas()

# Crear algunos hoteles
hotel1 = Hotel("Hotel Sol", "Madrid")
hotel2 = Hotel("Hotel Luna", "Barcelona")

print(sistema.buscar_hoteles("Madrid"))

# Registrar hoteles en el sistema
sistema.registrar_hotel(hotel1)
sistema.registrar_hotel(hotel2)

print(sistema.buscar_hoteles("Madrid"))

print(sistema.buscar_hoteles("Madrid")[0])

print(sistema.buscar_hoteles("Madrid")[0].nombre)

hotel1.habitaciones

# Añadir habitaciones a los hoteles
habitacion1 = Habitacion(101, "simple", 100)
habitacion2 = Habitacion(102, "double", 150)
habitacion3 = Habitacion(201, "suite", 200)

hotel1.anadir_habitacion(habitacion1)
hotel1.anadir_habitacion(habitacion2)
hotel2.anadir_habitacion(habitacion3)