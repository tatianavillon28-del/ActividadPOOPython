# Clase Motor
class Motor:
    def __init__(self, tipo, potencia):
        self.__tipo = tipo
        self.__potencia = potencia

    # Encapsulamiento
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, nueva_potencia):
        self.__potencia = nueva_potencia

    # Métodos de comportamiento
    def encender_motor(self):
        print("El motor está encendido.")

    def detener_motor(self):
        print("El motor está apagado.")

    # Método str
    def __str__(self):
        return f"Motor: {self.__tipo} - Potencia: {self.__potencia}"


# Superclase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio, motor):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__motor = motor

    # Encapsulamiento
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, nueva_marca):
        self.__marca = nueva_marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, nuevo_anio):
        self.__anio = nuevo_anio

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, nuevo_motor):
        self.__motor = nuevo_motor

    # Métodos de comportamiento
    def encender(self):
        print(f"{self.__marca} {self.__modelo} encendido.")

    def apagar(self):
        print(f"{self.__marca} {self.__modelo} apagado.")

    # Método str
    def __str__(self):
        return f"Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__anio} | {self.__motor}"


# Clase hija Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, puertas):
        super().__init__(marca, modelo, anio, motor)
        self.__puertas = puertas

    @property
    def puertas(self):
        return self.__puertas

    @puertas.setter
    def puertas(self, nuevas_puertas):
        self.__puertas = nuevas_puertas

    # Métodos de comportamiento
    def abrir_maletero(self):
        print("El maletero está abierto.")

    def tocar_claxon(self):
        print("¡Pii pii!")

    # Método str sobrescrito
    def __str__(self):
        return super().__str__() + f" | Puertas: {self.__puertas}"


# Clase hija Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        super().__init__(marca, modelo, anio, motor)
        self.__cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        self.__cilindraje = nuevo_cilindraje

    # Métodos de comportamiento
    def hacer_caballito(self):
        print("La motocicleta está haciendo un caballito.")

    def usar_patada_arranque(self):
        print("La motocicleta arrancó con patada.")

    # Método str sobrescrito
    def __str__(self):
        return super().__str__() + f" | Cilindraje: {self.__cilindraje}cc"


# Objetos Motor
motor1 = Motor("Gasolina", "150 HP")
motor2 = Motor("Diésel", "200 HP")
motor3 = Motor("Gasolina", "80 HP")
motor4 = Motor("Eléctrico", "100 HP")

# Objetos Automovil
auto1 = Automovil("Toyota", "Corolla", 2022, motor1, 4)
auto2 = Automovil("Chevrolet", "Spark", 2021, motor2, 4)

# Objetos Motocicleta
moto1 = Motocicleta("Yamaha", "R15", 2023, motor3, 150)
moto2 = Motocicleta("Honda", "CBR", 2022, motor4, 250)

# Ejecución de métodos
auto1.encender()
auto1.abrir_maletero()
auto1.tocar_claxon()

moto1.encender()
moto1.hacer_caballito()
moto1.usar_patada_arranque()

# Mostrar información
print("\n--- AUTOMÓVILES ---")
print(auto1)
print(auto2)

print("\n--- MOTOCICLETAS ---")
print(moto1)
print(moto2)