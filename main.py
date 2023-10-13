from pilaHanoy import Pila

def tablero(n):
    torre1 = Pila()
    torre2 = Pila()
    torre3 = Pila()

    for i in range(n, 0, -1):
        torre1.push(i)  
    return torre1, torre2, torre3

def resolver(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        disco = origen.pop()
        destino.push(disco)
        movimiento = f"D{disco} from T{origen} to T{destino}"
        movimientos.append(movimiento)
    else:
        resolver(n-1, origen, auxiliar, destino, movimientos)
        disco = origen.pop()
        destino.push(disco)
        movimiento = f"D{disco} from T{origen} to T{destino}"
        movimientos.append(movimiento)
        resolver(n-1, auxiliar, destino, origen, movimientos)

def main():
    n = int(input("Numero de discos: "))
    torre1, torre2, torre3 = tablero(n)
    print(f"Torre 1: {torre1}")
    print(f"Torre 2: {torre2}")
    print(f"Torre 3: {torre3}")
    
    movimientos = []

    resolver(n, torre1, torre3, torre2, movimientos)

    print("\nLista de movimientos:")
    for movimiento in movimientos:
        print(movimiento)

    print(f"Total de movimientos: {len(movimientos)}")
    print(f"Torre 1: {torre1}")
    print(f"Torre 2: {torre2}")
    print(f"Torre 3: {torre3}")

if __name__ == "__main__":
    main()





