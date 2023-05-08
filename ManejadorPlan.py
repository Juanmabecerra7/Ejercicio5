from PlanAhorro import Plan
import csv


class ManejadorPlan:
    def __init__(self):
        self.__lista = []

    def actualizar(self):
        indice = 0
        while indice < len(self.__lista):
            Plan.mostar(self.__lista[indice])
            precio = int(input("Ingrese el precio actual del vehiculo: "))
            if precio == int(self.__lista[indice].getValor()):
                nuevo_precio = int(input("Ingrese el nuevo precio del vehiculo: "))
                Plan.actualizarprecio(self.__lista[indice], nuevo_precio)
            indice = indice + 1


    def agregarunplan(self, unplan):
        self.__lista.append(unplan)

    def testplanes(self):
        archivo = open("planes.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            codigo = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = int(fila[3])
            cant_cuotas = int(fila[4])
            pagar_cuotas = int(fila[5])
            unplan = Plan(codigo, modelo, version, valor, cant_cuotas, pagar_cuotas)
            self.agregarunplan(unplan)
        archivo.close()

    def mostar(self, modelo, version):
        indice = 0
        s = 0
        while indice < len(self.__lista):
            if Plan.getModelo(self.__lista[indice]) == modelo and Plan.getVersion(self.__lista[indice]) == version:
                print(indice)
                s = Plan.licitar(self.__lista[indice])
            indice = indice + 1
        return s

    def modificar(self, codigo):
        indice = 0
        while indice < len(self.__lista):
            if Plan.getCodigo(self.__lista[indice]) == codigo:
                Plan.modificar(self.__lista[indice])
            indice = indice + 1

    def buscar(self, valor):
        indice = 0
        while indice < len(self.__lista):
            if self.__lista[indice].getValorCuotas() < valor:
                print(Plan.mostar(self.__lista[indice]))
            indice = indice + 1

    def __str__(self):
        s = ""
        for Plan in self.__lista:
            s = s + str(Plan) + "\n"
        return str(s)
