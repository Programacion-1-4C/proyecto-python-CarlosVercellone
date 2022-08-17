import pickle

listacomputadoras = pickle.load(open("Computadoras.txt", "rb"))
stockcomputadoras = pickle.load(open("stockcompus.txt", "rb"))
precioscomputadoras = pickle.load(open("precioscompus.txt", "rb"))

listacomponentes = pickle.load(open("Componentes.txt", "rb"))
stockcomponentes = pickle.load(open("stockcomponentes.txt", "rb"))
precioscomponentes = pickle.load(open("precioscomponentes.txt", "rb"))

listanotebooks = pickle.load(open("Notebooks.txt", "rb"))
stocknotebooks = pickle.load(open("stocknotebooks.txt", "rb"))
preciosnotebooks = pickle.load(open("preciosnotebooks.txt", "rb"))


def Agregarcomputadora():
    compu = input('Nombre: ')
    stockcompu = int(input('Stock: '))
    preciocompu = float(input('Precio: $'))
    listacomputadoras.append(compu)
    stockcomputadoras.append(stockcompu)
    precioscomputadoras.append(preciocompu)
    pickle.dump(listacomputadoras, open("Computadoras.txt", "wb"))
    pickle.dump(stockcomputadoras, open("stockcompus.txt", "wb"))
    pickle.dump(precioscomputadoras, open("precioscompus.txt", "wb"))


def AgregarComponente():
    componente = input('Nombre: ')
    stockcomponente = int(input('Stock: '))
    preciocomponenente = float(input('Precio: $'))
    listacomponentes.append(componente)
    precioscomponentes.append(preciocomponenente)
    stockcomponentes.append(stockcomponente)
    pickle.dump(listacomponentes, open("Componentes.txt", "wb"))
    pickle.dump(stockcomponentes, open("stockcomponentes.txt", "wb"))
    pickle.dump(precioscomponentes, open("precioscomponentes.txt", "wb"))


def Agregarnotebook():
    notebook = input('Nombre: ')
    stocknotebook = int(input('Stock: '))
    precionotebook = float(input('Precio: $'))
    listanotebooks.append(notebook)
    stocknotebooks.append(stocknotebook)
    preciosnotebooks.append(precionotebook)
    pickle.dump(listanotebooks, open("Notebooks.txt", "wb"))
    pickle.dump(stocknotebooks, open("stocknotebooks.txt", "wb"))
    pickle.dump(preciosnotebooks, open("preciosnotebooks.txt", "wb"))


def Cambiar_stock():
    producto = input('A que producto le quiere cambiar el stock?\n> ')
    if producto in listanotebooks:
        posicion = listanotebooks.index(producto)
        nuevostock = int(input(f'Nuevo stock de la notebook: {listanotebooks[posicion]}\n> '))
        stocknotebooks[posicion] = nuevostock
        pickle.dump(stocknotebooks, open("stocknotebooks.txt", "wb"))

    elif producto in listacomponentes:
        posicion = listacomponentes.index(producto)
        nuevostock = int(input(f'Nuevo stock del componente: {listacomponentes[posicion]}\n> '))
        stockcomponentes[posicion] = nuevostock
        pickle.dump(stockcomponentes, open("stockcomponentes.txt", "wb"))

    elif producto in listacomputadoras:
        posicion = listacomputadoras.index(producto)
        nuevostock = int(input(f'Nuevo stock de la computadora: {listacomputadoras[posicion]}\n> '))
        stockcomputadoras[posicion] = nuevostock
        pickle.dump(stockcomputadoras, open("stockcompus.txt", "wb"))


def Cambiar_Precio():
    producto1 = input('A que producto le quiere cambiar el precio?\n> ')
    if producto1 in listanotebooks:
        posicion = listanotebooks.index(producto1)
        nuevoprecio = int(input(f'Nuevo precio de la notebook: {listanotebooks[posicion]}\n> '))
        preciosnotebooks[posicion] = nuevoprecio
        pickle.dump(preciosnotebooks, open("preciosnotebooks.txt", "wb"))

    elif producto1 in listacomponentes:
        posicion = listacomponentes.index(producto1)
        nuevoprecio = int(input(f'Nuevo precio del componente: {listacomponentes[posicion]}\n> '))
        precioscomponentes[posicion] = nuevoprecio
        pickle.dump(precioscomponentes, open("precioscomponentes.txt", "wb"))

    elif producto1 in listacomputadoras:
        posicion = listacomputadoras.index(producto1)
        nuevoprecio = int(input(f'Nuevo precio de la computadora: {listacomputadoras[posicion]}\n> '))
        precioscomputadoras[posicion] = nuevoprecio
        pickle.dump(precioscomputadoras, open("precioscomppus.txt", "wb"))


def Comprar(producto):
    pickle.load(open("Computadoras.txt", "rb"))
    pickle.load(open("Componentes.txt", "rb"))
    pickle.load(open("Notebooks.txt", "rb"))
    pickle.load(open("precioscompus.txt", "rb"))
    pickle.load(open("precioscomponentes.txt", "rb"))
    pickle.load(open("preciosnotebooks.txt", "rb"))
    pickle.load(open("stockcompus.txt", "rb"))
    pickle.load(open("stockcomponentes.txt", "rb"))
    pickle.load(open("stocknotebooks.txt", "rb"))

    print(listanotebooks)

    if producto == 1:
        producto1 = pickle.load(open("Componentes.txt", "rb"))
        stockproducto1 = pickle.load(open("stockcomponentes.txt", "rb"))
        precioproducto1 = pickle.load(open("precioscomponentes.txt", "rb"))



    elif producto == 2:
        producto1 = pickle.load(open("Notebooks.txt", "rb"))
        stockproducto1 = pickle.load(open("stocknotebooks.txt", "rb"))
        precioproducto1 = pickle.load(open("preciosnotebooks.txt", "rb"))



    elif producto == 3:
        producto1 = pickle.load(open("Computadoras.txt", "rb"))
        stockproducto1 = pickle.load(open("stockcompus.txt", "rb"))
        precioproducto1 = pickle.load(open("precioscompus.txt", "rb"))


    contador = 0

    def separadornumeros(num):
        return ("{:,}".format(num))

    for contador in range(len(producto1)):
        preciodolares = precioproducto1[contador] / 293

        print('______________________________________________________________________________________')
        print(
            f'|{producto1[contador]}  | Stock: {stockproducto1[contador]}  | precio: ${separadornumeros(precioproducto1[contador])}  | Dolares: {separadornumeros(round(preciodolares, 2))}  |')
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
        listacomputadoras = pickle.load(open("Computadoras.txt", "rb"))

        if producto1 in listanotebooks:
            pickle.dump(producto1, open("Notebooks.txt", "wb"))
            pickle.dump(precioproducto1, open("preciosnotebooks.txt", "wb"))
            pickle.dump(stockproducto1, open("stocknotebooks.txt", "wb"))
        elif producto1 in listacomputadoras:
            pickle.dump(producto1, open("Computadoras.txt", "wb"))
            pickle.dump(precioproducto1, open("precioscompus.txt", "wb"))
            pickle.dump(stockproducto1, open("stockcompus.txt", "wb"))
        elif producto1 in listacomponentes:
            pickle.dump(producto1, open("Componentes.txt", "wb"))
            pickle.dump(precioproducto1, open("precioscomponentes.txt", "wb"))
            pickle.dump(stockproducto1, open("stockcomponentes.tx", "wb"))

