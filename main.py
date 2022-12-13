from http.client import NETWORK_AUTHENTICATION_REQUIRED
from clases import *
import networkx as nx

opcion = ""

pila = Stack()
cola = Queue()
arbol = Arbol("50")
grafo = nx.Graph()
if __name__ == "__main__":
    while opcion != '5':
        print("Escoja una de las siguientes opciones")
        print("1-Pilas")
        print("2-Colas")
        print("3-Arboles Binarios")
        print("4-Grafos")
        print("5-Salir")
        opcion = input("Escoja una de las opciones: ")
        borrarPantalla()
        match opcion:
            case '1':
                optPila = ""
                while optPila != '4':
        
                    print("PILAS")
                    print("Escoja una de las siguientes opciones")
                    print("1-Insertar")
                    print("2-Extraer")
                    print("3-Visualizar")
                    print("4-Salir")
                    
                    optPila = input("Opcion : ")
                    borrarPantalla()
                    match optPila:
                        case '1':
                            agregar = input("Agrege un elemento a la Pila ")
                            pila.push(agregar)
                            pausa()
                            borrarPantalla()
                        case '2':
                            print("Se ha eliminado ",pila.pop())
                        case '3':
                            pila.print_stack()
                            pausa()
                            borrarPantalla()
                        case '4':
                            continue
                        case _:
                            print("La opcion en no es correcta")
                            pausa()
                            borrarPantalla()

            case '2':
                optCola = ""
                while optCola != '4':
                   
                    print("Colas")
                    print("Escoja una de las siguientes opciones")
                    print("1-Insertar")
                    print("2-Extraer")
                    print("3-Visualizar")
                    print("4-Salir")
                    
                    optCola = input("Opcion: ")
                    borrarPantalla()
                    match optCola:
                        case '1':
                            agregar = input("Agrege un elemento a la Cola ")
                            cola.enqueue(agregar)
                            pausa()
                            borrarPantalla()
                        case '2':
                            print("Se ha eliminado", cola.dequeue())
                        case '3':
                            cola.print_queue()
                            pausa()
                            borrarPantalla()
                        case '4':
                            continue
                        case _:
                            print("La opcion en no es correcta")
                            pausa()
                            borrarPantalla()
            case '3':
                optArbol = ""
                while optArbol != '5':
                    
                    print("Arboles Binarios")
                    print("Escoja una de las siguientes opciones")
                    print("1-Crear Arbol")
                    print("2-Recorrido PreOrden")
                    print("3-Recorrido EnOrden")
                    print("4-Recorrido PostOrden")
                    print("5-Salir")
                    
                    optArbol = input("Opcion: ")
                    borrarPantalla()
                    match optArbol:
                        case '1':
                            opcElemento = "si"
                            while opcElemento == "si":
                                elementoArbol = input("Agrage un elemento al arbol Binario: ")
                                arbol.agregar(elementoArbol)
                                opcElemento = input("Desea Agregar otro elemento: ")
                                borrarPantalla()
                        case '2':
                            arbol.preorden()
                            pausa()
                            borrarPantalla()
                        case '3':
                            arbol.inorden()
                            pausa()
                            borrarPantalla()
                        case '4':
                            arbol.postorden()
                            pausa()
                            borrarPantalla()
                        case '5':
                            continue
                        case _:
                            print("La opcion en no es correcta")
                            pausa()
                            borrarPantalla()
            case '4':
                optGrafo = ""
                while optGrafo != '5':
                    
                    print("Grafos")
                    print("Escoja una de las siguientes opciones")
                    print("1-Crear el Grafo")
                    print("2-Introducir elemento")
                    print("3-Eliminar elemento")
                    print("4-Recorrer el grafo")
                    print("5-Salir")
                    
                    optGrafo = input("Opcion: ")
                    borrarPantalla()
                    match optGrafo:
                        case '1':
                            grafo = nx.Graph()
                            print("Se ha creado el grafo satisfactoriamente")
                            pausa()
                            borrarPantalla()
                        case '2':
                            opcnodo = ""
                            while opcnodo != '3':
                                print("Grafos")
                                print("Escoja una de las siguientes opciones")
                                print("1-Crear un nodo")
                                print("2-crear un vertice")
                                print("3-Salir")
                                opcnodo = input("Desea Agregar otro elemento: ")
                                borrarPantalla()
                                match opcnodo:
                                    case '1':
                                        nodo = input("Agrege un nodo al grafo: ")
                                        grafo.add_node(nodo)
                                        borrarPantalla()
                                    case '2':
                                        print("Agrege un vertice al grafo: ")
                                        nodo1 = input("Nodo inicial del vertice: ")
                                        nodo2 = input("Nodo final del vertice: ")
                                        peso = int(input("peso del vertice: "))
                                        if nodo1 and nodo2 in grafo.nodes:
                                            grafo.add_edge(nodo1, nodo2, weight = peso)
                                            print("el vertice fue creado exitosamente")
                                            pausa()
                                            borrarPantalla()
                                        else:
                                            print("el vertice no pudo ser creado, revise si ambos nodos existen dentro del grafo")
                                            pausa()
                                            borrarPantalla()
                                    case '3':
                                        continue
                                    case _:
                                        print("La opcion no es correcta")
                                        pausa()
                                        borrarPantalla()
                        case '3':
                            remove = input("Ingrese el nodo a retirar: ")
                            if remove in grafo.nodes():
                                grafo.remove_node(remove)
                                print("Se ha retirado satisfactoriamente el nodo ", remove)
                                pausa()
                                borrarPantalla()
                            else:
                                print("El nodo que intenta retirar del grafo no existe")
                                pausa()
                                borrarPantalla()
                        case '4':
                            print("Recorrido de grafos, ingrese el nodo inicial y el nodo final")
                            nodoinicio = input("Nodo inicial del vertice: ")
                            nodofin = input("Nodo final del vertice: ")
                            ''' if nodoinicio and nodofin in grafo.nodes:
                                print(nx.shortest_path(grafo, nodoinicio, nodofin, weight="weight"))
                                pausa()
                                borrarPantalla()
                            else:
                                print("El recorrido no pudo ser completado, Verifique que ambos nodos existan dentro del grafo")
                                print("Nodos dentro del grafo ")
                                print(grafo.nodes())
                                pausa()
                                borrarPantalla() '''
                            try:
                                print(nx.shortest_path(grafo, nodoinicio, nodofin, weight="weight"))
                                pausa()
                                borrarPantalla()
                            except nx.exception.NetworkXNoPath:
                                print("no existe una ruta entre esos puntos")
                                pausa()
                                borrarPantalla()
                        case '5':
                            continue
                        case _:
                            print("La opcion en no es correcta")
                            pausa()
                            borrarPantalla()
            case '5':
                print("El Programa ha terminado. muchas gracias")
            case _:
                print("La opcion no es correcta")
                pausa()
                borrarPantalla()           
