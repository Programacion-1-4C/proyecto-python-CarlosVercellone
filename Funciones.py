import pickle

listacomputadoras = pickle.load(open("Computadoras_nombre.gdc", "rb"))
stockcomputadoras = pickle.load(open("Computadoras_stock.gdc", "rb"))
precioscomputadoras = pickle.load(open("Computadoras_precio.gdc", "rb"))

listacomponentes = pickle.load(open("Componentes_nombre.gdc", "rb"))
stockcomponentes = pickle.load(open("Componentes_stock.gdc", "rb"))
precioscomponentes = pickle.load(open("Componentes_precio.gdc", "rb"))

listanotebooks = pickle.load(open("Notebooks_nombre.gdc", "rb"))
stocknotebooks = pickle.load(open("Notebooks_stock.gdc", "rb"))
preciosnotebooks = pickle.load(open("Notebooks_precio.gdc", "rb"))



def agregar_elemento(lista_nombres, lista_stocks, lista_precios, elemento_a_modificar):
    nombre = input('Nombre: ')
    stock = int(input('Stock: '))
    precio = float(input('Precio: $'))
    lista_nombres.append(nombre)
    lista_stocks.append(stock)
    lista_precios.append(precio)
    pickle.dump(lista_nombres, open(f"{elemento_a_modificar}_nombre.gdc", "wb"))
    pickle.dump(lista_stocks, open(f"{elemento_a_modificar}_stock.gdc", "wb"))
    pickle.dump(lista_precios, open(f"{elemento_a_modificar}_precio.gdc", "wb"))

def cambiar_dato_en_lista(producto1, lista, lista_modificar, nombre_archivo, modificado):
    if producto1 in lista:
        posicion = lista.index(producto1)
        nuevodato = int(input(f'Nuevo {modificado} {nombre_archivo}: {lista[posicion]}\n> '))
        lista_modificar[posicion] = nuevodato
        pickle.dump(lista_modificar, open(f"{nombre_archivo}_{modificado}.gdc", "wb"))

def Cambiar_stock():
    producto = input('A que producto le quiere cambiar el stock?\n> ')

    cambiar_dato_en_lista(producto, listanotebooks, stocknotebooks, "Notebooks", "stock")
    cambiar_dato_en_lista(producto, listacomponentes, stockcomponentes, "Componentes", "stock")
    cambiar_dato_en_lista(producto, listacomputadoras, stockcomputadoras, "Computadoras", "stock")

def Cambiar_Precio():
    producto1 = input('A que producto le quiere cambiar el precio?\n> ')

    cambiar_dato_en_lista(producto1, listanotebooks, preciosnotebooks, "Notebooks", "precio")
    cambiar_dato_en_lista(producto1, listacomponentes, precioscomponentes, "Componentes", "precio")
    cambiar_dato_en_lista(producto1, listacomputadoras, precioscomputadoras, "Computadoras", "precio")


def eliminar_producto(lista_nombres, lista_precios, lista_stocks, nombre_archivo, posicion):
    lista_nombres.remove(lista_nombres[posicion])
    lista_precios.remove(lista_precios[posicion])
    lista_stocks.remove(lista_stocks[posicion])
    pickle.dump(lista_nombres, open(f"{nombre_archivo}_nombre.gdc", "wb"))
    pickle.dump(lista_precios, open(f"{nombre_archivo}_precio.gdc", "wb"))
    pickle.dump(lista_stocks, open(f"{nombre_archivo}_stock.gdc", "wb"))

def Comprar(producto):

    if producto == 1:
        producto1 = pickle.load(open("Componentes_nombre.gdc", "rb"))
        stockproducto1 = pickle.load(open("Componentes_stock.gdc", "rb"))
        precioproducto1 = pickle.load(open("Componentes_precio.gdc", "rb"))

    elif producto == 2:
        producto1 = pickle.load(open("Notebooks_nombre.gdc", "rb"))
        stockproducto1 = pickle.load(open("Notebooks_stock.gdc", "rb"))
        precioproducto1 = pickle.load(open("Notebooks_precio.gdc", "rb"))

    elif producto == 3:
        producto1 = pickle.load(open("Computadoras_nombre.gdc", "rb"))
        stockproducto1 = pickle.load(open("Computadoras_stock.gdc", "rb"))
        precioproducto1 = pickle.load(open("Computadoras_precio.gdc", "rb"))

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

        if producto == 2:
            eliminar_producto(listanotebooks, preciosnotebooks, stocknotebooks, "Notebooks", posicion)

        elif producto == 3:
            eliminar_producto(listacomputadoras, precioscomputadoras, stockcomputadoras, "Computadoras", posicion)

        elif producto == 1:
            eliminar_producto(listacomponentes, precioscomponentes, stockcomponentes, "Componentes", posicion)
