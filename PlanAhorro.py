class Plan:
    __codigo = 0
    __modelo = ""
    __version = ""
    __valor = 0
    __cant_cuotas = 0
    __pagar_cuotas = 0

    def __init__(self, codigo, modelo, version, valor, cant_cuotas, pagar_cuotas):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        self.__cant_cuotas = cant_cuotas
        self.__pagar_cuotas = pagar_cuotas

    def mostar(self):
        print(f"Codigo {self.__codigo}, Modelo {self.__modelo}, Version {self.__version}")

    def modificar(self):
        nuevo = int(input("Ingrese la nueva cantidad de cuotas para licitar el vehiculo"))
        self.__pagar_cuotas = nuevo

    def getVersion(self):
        return str(self.__version)

    def getModelo(self):
        return str(self.__modelo)

    def licitar(self):
        print(self.__pagar_cuotas)
        print(self.getValorCuotas())
        valor = (self.__pagar_cuotas * self.getValorCuotas())
        return int(valor)

    def getCodigo(self):
        return int(self.__codigo)

    def getValor(self):
        return int(self.__valor)

    def getValorCuotas(self):
        return int((self.__valor / self.__cant_cuotas) + int(self.__valor * 0.10))

    def actualizarprecio(self, precio):
        self.__valor = precio
        return

    def __str__(self):
        return str(str(self.__codigo)+" "+self.__modelo+" "+self.__version+" "+str(self.__valor)+" "+str(self.__cant_cuotas)+" "+str(self.__pagar_cuotas)+" ")
