class Nodo:
    def __init__(self, valor, next=None):
        self.valor = valor
        self.next = next

class ListaCompras:
    def __init__(self):
        self.cabeza = None

    def agregar_producto_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.next = self.cabeza
        else:
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next != self.cabeza:
                ultimo_nodo = ultimo_nodo.next
            ultimo_nodo.next = nuevo_nodo
            nuevo_nodo.next = self.cabeza

    def eliminar_producto_inicio(self):
        if self.cabeza is None:
            return None
        elif self.cabeza.next == self.cabeza:
            valor = self.cabeza.valor
            self.cabeza = None
            return valor
        else:
            valor = self.cabeza.valor
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next != self.cabeza:
                ultimo_nodo = ultimo_nodo.next
            self.cabeza = self.cabeza.next
            ultimo_nodo.next = self.cabeza
    def mostrar_productos(self):
        if self.cabeza is None:
            print("La lista de compras está vacía.")
        else:
            actual = self.cabeza
            while True:
                print(actual.valor)
                actual = actual.next
                if actual == self.cabeza:
                    break
try:
    if  __name__ == "__main__":
        opcion = 0
        lista_compras = ListaCompras()
        while opcion != 4:
            opcion = int(input("\nLista de compras:\n1. Agregar al final\n2. Eliminar al inicio\n3. Mostrar lista de compras\n4. Salir\nSelecciona una opción: "))
            if opcion == 1:
                valor = input("Ingrese el producto a agregar: ")
                lista_compras.agregar_producto_final(valor)
                print("Producto agregado exitosamente.")
            elif opcion == 2:
                lista_compras.eliminar_producto_inicio()
                print("Producto eliminado")
            elif opcion == 3:
                lista_compras.mostrar_productos()
            elif opcion == 4:
                print("Adiós.")
                break
            else:
                print("Opción inválida, selecciona una opción válida.")
except Exception as e:
    print(e)