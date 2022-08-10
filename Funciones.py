import pickle

listacomputadoras = []
stockcomputadoras = []
precioscomputadoras = []


listacomponentes = []
stockcomponentes = []
precioscomponentes = []

listanotebooks = []
stocknotebooks = []
preciosnotebooks = []


def Agregarcomputadora():
    compu = input('Nombre: ')
    stockcompu = int(input('Stock: '))
    preciocompu = float(input('Precio: $'))
    listacomputadoras.append(compu)
    stockcomputadoras.append(stockcompu)
    precioscomputadoras.append(preciocompu)
    pickle.dump(listacomputadoras, open("productos.txt", "wb"))
    pickle.dump(stockcomputadoras, open("stock.txt", "wb"))
    pickle.dump(precioscomputadoras, open("precios.txt", "wb"))


def AgregarComponente():
    componente = input('Nombre: ')
    stockcomponente = int(input('Stock: '))
    preciocomponenente = float(input('Precio: $'))
    listacomponentes.append(componente)
    precioscomponentes.append(preciocomponenente)
    stockcomponentes.append(stockcomponente)
    pickle.dump(listacomponentes, open("productos.txt", "wb"))
    pickle.dump(stockcomponentes, open("stock.txt", "wb"))
    pickle.dump(precioscomponentes, open("precios.txt", "wb"))


def Agregarnotebook():
    notebook = input('Nombre: ')
    stocknotebook = int(input('Stock: '))
    precionotebook = float(input('Precio: $'))
    listanotebooks.append(notebook)
    stocknotebooks.append(stocknotebook)
    preciosnotebooks.append(precionotebook)
    pickle.dump(listanotebooks, open("productos.txt", "wb"))
    pickle.dump(stocknotebooks, open("stock.txt", "wb"))
    pickle.dump(preciosnotebooks, open("precios.txt", "wb"))

def Cambiar_stock():
    producto = input('A que producto le quiere cambiar el stock?\n> ')
    if producto in listanotebooks:
        posicion = listanotebooks.index(producto)
        nuevostock = int(input(f'Nuevo stock de la notebook: {listanotebooks[posicion]}\n> '))
        stocknotebooks[posicion] = nuevostock
        pickle.dump(stocknotebooks, open("precios.txt", "wb"))

    elif producto in listacomponentes:
        posicion = listacomponentes.index(producto)
        nuevostock = int(input(f'Nuevo stock del componente: {listacomponentes[posicion]}\n> '))
        stockcomponentes[posicion] = nuevostock
        pickle.dump(stockcomponentes, open("precios.txt", "wb"))

    elif producto in listacomputadoras:
        posicion = listacomputadoras.index(producto)
        nuevostock = int(input(f'Nuevo stock de la computadora: {listacomputadoras[posicion]}\n> '))
        stockcomputadoras[posicion] = nuevostock
        pickle.dump(stockcomputadoras, open("precios.txt", "wb"))

def Cambiar_Precio():
    producto1 = input('A que producto le quiere cambiar el precio?\n> ')
    if producto1 in listanotebooks:
        posicion = listanotebooks.index(producto1)
        nuevoprecio = int(input(f'Nuevo precio de la notebook: {listanotebooks[posicion]}\n> '))
        preciosnotebooks[posicion] = nuevoprecio
        pickle.dump(preciosnotebooks, open("precios.txt", "wb"))

    elif producto1 in listacomponentes:
        posicion = listacomponentes.index(producto1)
        nuevoprecio = int(input(f'Nuevo precio del componente: {listacomponentes[posicion]}\n> '))
        precioscomponentes[posicion] = nuevoprecio
        pickle.dump(precioscomponentes, open("precios.txt", "wb"))

    elif producto1 in listacomputadoras:
        posicion = listacomputadoras.index(producto1)
        nuevoprecio = int(input(f'Nuevo precio de la computadora: {listacomputadoras[posicion]}\n> '))
        precioscomputadoras[posicion] = nuevoprecio
        pickle.dump(precioscomputadoras, open("precios.txt", "wb"))



def Comprar(producto):

    pickle.load(open("productos.txt", "rb"))
    pickle.load(open("precios.txt", "rb"))
    pickle.load(open("stock.txt", "rb"))

    print(listanotebooks)

    if producto == 1:
        producto1 = listacomponentes
        precioproducto1 = precioscomponentes
        stockproducto1 = stockcomponentes

    elif producto == 2:
        producto1 = listanotebooks
        precioproducto1 = preciosnotebooks
        stockproducto1 = stocknotebooks

    elif producto == 3:
        producto1 = listacomputadoras
        precioproducto1 = precioscomputadoras
        stockproducto1 = stockcomputadoras

    contador = 0

    def separadornumeros(num):
        return ("{:,}".format(num))


    for contador in  range(len(producto1)):
        preciodolares = precioproducto1[contador] / 293

        print('______________________________________________________________________________________')
        print(f'|{producto1[contador]}  | Stock: {stockproducto1[contador]}  | precio: ${separadornumeros(precioproducto1[contador])}  | Dolares: {separadornumeros(round(preciodolares , 2))}  |')
        print('______________________________________________________________________________________')
        contador += 1

    producto_a_comprar = input('Que producto desea comprar?\n> ')
    if producto_a_comprar not in producto1:
        print("\nPRODUCTO NO DISPONIBLE ACTUALMENTE\n")

    else:
        posicion = producto1.index(producto_a_comprar)
        producto1.remove(producto1[posicion])
        stockproducto1.remove(stockproducto1[posicion])
        precioproducto1.remove(precioproducto1[posicion])
        pickle.dump(producto1, open("productos.txt", "wb"))
        pickle.dump(precioproducto1, open("precios.txt", "wb"))
        pickle.dump(stockproducto1, open("stock.txt", "wb"))

