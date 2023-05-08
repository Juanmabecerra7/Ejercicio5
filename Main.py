from ManejadorPlan import ManejadorPlan
from PlanAhorro import Plan

if __name__ == '__main__':
    mv = ManejadorPlan()
    mv.testplanes()
    print(str(mv))
    opcion = 1
    while opcion != 0:
        print("1: Actualizar el valor del Vehiculo de un plan")
        print("2: Mostar Informacion")
        print("3: Mostar el monto a pagar para poder licitar el vehiculo")
        print("4: Modificar la cantidad de cuotas a pagar para poder licitar el vehiculo")
        print("5: Salir")
        opcion = int(input())
        if opcion == 1:
            print(mv.actualizar())
        elif opcion == 2:
            valor = int(input("Ingrese un valor de cuota"))
            mv.buscar(valor)
        elif opcion == 3:
            modelo = input("Ingrese el modelo del vehiculo")
            version = input("Ingrese la version del vehiculo")
            print(mv.mostar(modelo, version))
        elif opcion == 4:
            codigo = int(input("Ingrese un codigo de plan"))
            mv.modificar(codigo)
        elif opcion == 5:
            exit()
        else:
            print("----Opcion Invalida----")
        opcion = 1
