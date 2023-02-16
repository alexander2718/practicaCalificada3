class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listaTareasPendientes:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None
    
    def agregar_tarea_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size +=1

    def eliminar_tarea_final(self):
        if self.vacia():
            print("Lista de tareas pendientes vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size =0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -=1

    def mostrar_orden_inverso(self):
        aux = self.ultimo
        while aux!= None:
            print(aux.dato)
            aux = aux.anterior

    def tareas_pendientes(self):
        print("Número de tareas pendientes:", self.size)


try:
    if  __name__ == "__main__":
        opcion = 0
        lista_tareas = listaTareasPendientes()
        while opcion != 5:
            opcion = int(input("\nLista de tareas pendientes:\n1. Agregar al inicio\n2. Eliminar del final\n3. Mostrar en orden inverso\n4. Cantidad de tareas pendientes\n5. Salir\nSelecciona una opción: "))
            if opcion == 1:
                valor = input("Ingrese la tarea pendiente: ")
                lista_tareas.agregar_tarea_inicio(valor)
                print("Tarea pendiente agregada.")
            elif opcion == 2:
                lista_tareas.eliminar_tarea_final()
            elif opcion == 3:
                lista_tareas.mostrar_orden_inverso()
            elif opcion ==4:
                lista_tareas.tareas_pendientes()
            elif opcion == 5:
                print("Adiós.")
                break
            else:
                print("Opción inválida, selecciona una opción válida.")
except Exception as e:
    print(e)