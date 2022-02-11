from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#Primero crearemos un inicio de sesión usando el bucle while, agregaremos algunos mensajes para descibrir las distintas situaciones y crear una interfaz más amigable e interactiva.
#Para el inicio de sesión usaremos los siguientes datos:
# usuario:
#     Invitado
# contraseña:
#     DataDarks

usuarioAccedio = False
intentos = 0

mensaje_bienvenida = "Le damos la bienvenida al sistema.  \nInicia sesión para acceder"
print(mensaje_bienvenida)

while not usuarioAccedio:

    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    intentos += 1

    if usuario == 'Invitado' and contrasena == 'DataDarks':
        usuarioAccedio = True
        print('\n ¡Saludos! \n')
    else:

        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'Invitado':
            print('La contraseña es incorrecta.')
        else:
            print(f'El usuario: "{usuario}" no esta registrado.')

    if intentos == 3:
        print("Por favor intente de nuevo más tarde")
        exit()

#Una vez que el usuario haya iniciado sesión usaremos otro bucle while para darle a elegir si quiere o no ver los datos obtenidos, esto decide si el resto del código se ejecuta o no.

Correr_codigo = False
while not Correr_codigo:
    si_no = input('¿Desea ver las listas obtenida ("si" | "no") ')
    if si_no == "si":
        Correr_codigo = True
    elif si_no == "no":
        exit()
    else:
        print("Por favor escriba únicamente 'si' o 'no'")

#Para obtener los datos de los productos con más ventas seguiremos los siguientes pasos:
#Primero crearemos un diccionario con los datos de la list lifestore_sales en la que asociaremos el id_product con el id_sale, llamaremos a este diccionario ventas_clasificadas.

id_categoria_ventas = [[producto[0], producto[1]]
                       for producto in lifestore_sales]
#print(id_categoria)
ventas_clasificadas = {}
for par in id_categoria_ventas:
    idv = par[0]
    categoria = par[1]
    if categoria not in ventas_clasificadas.keys():
        ventas_clasificadas[categoria] = []
    ventas_clasificadas[categoria].append(idv)
#print(ventas_clasificadas )

#Ahora crearemos una lista llamada lista_mas_ventas, donde guardaremos los siguientes datos: [no. de veces que se vendio un producto, id_product]. Para esto usaremos un ciclo for sobre los elementos de ventas_clsificadas y la función isinstance() para contar el número de elementos de cada entrada del diccionario.

lista_mas_ventas = []

for v in ventas_clasificadas:
    count = 0
    if isinstance(ventas_clasificadas[v], list):
        count += len(ventas_clasificadas[v])
    lista_mas_ventas.append([count, v])

    #print( count)
#print(lista_mas_ventas)
print("\n")
print("Más vendidos:")

#Seguido usaremos dos ciclos for (uno para los lementos de lista_mas_ventas y otro para los elementos de lifestore_products) y la función insert para agregar el nombre del producto a la lista de lista_mas_ventas, esto con la finalidad de crear un output más limpio.

for k in lista_mas_ventas:
    for l in lifestore_products:
        if k[1] == l[0]:
            k.insert(2, l[1])
#print(lista_mas_ventas)

#Finalmente usaremos la función .sort() para ordenar lista_mas_ventas de mayor a menor, y viceversa según sea el caso, usando como parametro el primer dato de cada elemento (número de ventas) y crearemos un mensaje de output para mostrar estos datos de forma más ordenada.

lista_mas_ventas.sort(reverse=True)

for w in lista_mas_ventas[:5]:
    print("El producto " + w[2], " fue vendido " + str(w[0]), " veces.  ")
print("\n")
print("Menos venidos:")
lista_mas_ventas.sort()
for ww in lista_mas_ventas[:5]:
    print("El producto " + ww[2], " fue vendido " + str(ww[0]), " veces.  ")
print("\n")

#El proceso para obtener las mayores y menores busquedas es exactamenet igual al usado para las ventas, salvo que aquí usaremos los datos de la lista lifestore_searches

id_categoria_busquedas = [[productob[0], productob[1]]
                          for productob in lifestore_searches]
#print(id_categoria_busquedas)
busquedas_clasificadas = {}
for parb in id_categoria_busquedas:
    idb = parb[0]
    categoriab = parb[1]
    if categoriab not in busquedas_clasificadas.keys():
        busquedas_clasificadas[categoriab] = []
    busquedas_clasificadas[categoriab].append(idb)
#print(busquedas_clasificadas)

lista_mas_busquedas = []
for b in busquedas_clasificadas:
    countb = 0
    if isinstance(busquedas_clasificadas[b], list):
        countb += len(busquedas_clasificadas[b])
    lista_mas_busquedas.append([countb, b])

    #print( countb)
# print(lista_mas_busquedas)

for k1 in lista_mas_busquedas:
    for l1 in lifestore_products:
        if k1[1] == l1[0]:
            k1.insert(2, l1[1])

print("Más buscados:")
lista_mas_busquedas.sort(reverse=True)

for w1 in lista_mas_busquedas[:10]:
    print("El producto " + w1[2], " fue buscado " + str(w1[0]), " veces.  ")
print("\n")

print("Menos buscados:")
lista_mas_busquedas.sort()
for ww1 in lista_mas_busquedas[:10]:
    print("El producto " + ww1[2], " fue buscado " + str(ww1[0]), " veces.  ")
print("\n")

#El proceso para obtener las reseñas sigue siendo el mismo que hemos estado usando, de nuevo la diferencia aquí es que usamos los datos de la lista lifestore_sales, el apartado de las reseñas.

id_categoria_resenas = [[productor[2], productor[1]]
                        for productor in lifestore_sales]
#print(id_categoria_resenas)
resenas_clasificadas = {}
for par_r in id_categoria_resenas:
    idr = par_r[0]
    categoriar = par_r[1]
    if categoriar not in resenas_clasificadas.keys():
        resenas_clasificadas[categoriar] = []
    resenas_clasificadas[categoriar].append(idr)
#print(resenas_clasificadas )

#Otra diferencia es que como aquí buscamos un promedio, usaremos la función sum() para obtener la suma de los elementos de resenas_clasificadas[] y agregaremos una variable llamada promedio que guardara, como su nombre lo dice, el promedio de reseñas de cada producto, a la lista lista_mejores_resena agregaremos los datos [promedio, id_product].

lista_mejores_resenas = []
for r in resenas_clasificadas:
    countr = 0
    if isinstance(resenas_clasificadas[r], list):
        countr += len(resenas_clasificadas[r])
    countr2 = 0
    if isinstance(resenas_clasificadas[r], list):
        countr2 += sum(resenas_clasificadas[r])
    #print(countr2)
    promedio = round(countr2 / countr, 2)
    #print(promedio)
    lista_mejores_resenas.append([promedio, r])

#print(lista_mejores_resenas)

for k2 in lista_mejores_resenas:
    for l2 in lifestore_products:
        if k2[1] == l2[0]:
            k2.insert(2, l2[1])

print("Mejores reseñas:")
lista_mejores_resenas.sort(reverse=True)
for w2 in lista_mejores_resenas[:10]:
    print("El producto " + w2[2],
          " tiene una reseña promedio de " + str(w2[0]), " estrellas.  ")
print("\n")

print("Peores reseñas:")
lista_mejores_resenas.sort()
for ww2 in lista_mejores_resenas[:10]:
    print("El producto " + ww2[2],
          " tiene una reseña promedio de  " + str(ww2[0]), " estrellas.  ")
print("\n")

#Para los ingresos y ventas primero craremos una lista llamada lifestore_sales_noref, que será una copia de lifestore_sales, pero quitando los productos que fueron devueltos y usando la función for agregaremos el precio de cada producto a esta lista.

print("Ingresos y Ventas:")

lifestore_sales_noref = []
for element in lifestore_sales:
    if element[4] == 0:
        lifestore_sales_noref.append(element)
#print(lifestore_sales_noref)

for a in lifestore_sales_noref:
    for b in lifestore_products:
        if a[1] == b[0]:
            a.insert(5, b[2])
    #print(a)

#Aquí usaremos la función datatime para ordenar lifestore_sales_noref según la fecha en que fueron vendidos los productos.

from datetime import datetime
import calendar

fecha = [element1[3] for element1 in lifestore_sales_noref]


#print(fecha)
def sortByDate(elem):
    return datetime.strptime(elem[3], "%d/%m/%Y")


lifestore_sales_noref.sort(key=sortByDate)
#print(lifestore_sales_noref)

#Crearemos cuatro listas nuevas, ingreso_anual_lista guardará los ingresos mensuales; ventas_totales_lista las ventas mensuales; ventas_promedio el resultado de dividir el ingreso mensual entre las ventas mensuales y Meses tendra el nombr de cada mes y su número (Esta última lista es meramente para correlacionar datos y tener un ouyput más ordenado).

ingreso_anual_lista = []
ventas_totales_lista = []
ventas_promedio = []
Meses = [["Enero", "01"], ["Febrero", "02"], ["Marzo", "03"], ["Abril", "04"],
         ["Mayo", "05"], ["Junio", "06"], ["Julio", "07"], ["Agosto", "08"],
         ["Septiembre", "09"], ["Octubre", "10"], ["Noviembre", "11"],
         ["Diciembre", "12"]]

# Usandoun ciclo for sobre Meses y otro sobre lifestore_sales_noref correlacionaremos y contaremos el ingreso de cada mes. Asimismo usando otro ciclo for sobre lifestore_sales obtendremos las ventas mensuales y con estos dos datos el numero de ventas promedio.

for m in Meses:
    income = 0
    for m2 in lifestore_sales_noref:

        if m[1] == m2[3][3:5]:
            income += m2[5]
    ingreso_anual_lista.append(income)
    print("El ingreso total mensual de " + m[0], "es de $" + str(income))
    ventas_a = 0
    for m2 in lifestore_sales:

        if m[1] == m2[3][3:5]:
            ventas_a += 1
    ventas_totales_lista.append(ventas_a)
    print("Las ventas totales de " + m[0], "son de " + str(ventas_a))
    if ventas_a == 0:
        print("Las ventas promedio de " + m[0], "son de 0", "\n")
    else:
        print("Las ventas promedio de " + m[0],
              "son de " + str(round(income / ventas_a, 2)), "\n")

#Por ultimo usaremos la función sum() para obtener el total de ingresos y de ventas y con estos datos las ventas promedio anuales.

#print(ventas_totales_lista)
print("El ingreso total anual es de: $" + str(sum(ingreso_anual_lista)))
print("Las ventas totales anuales fueron de: " +
      str(sum(ventas_totales_lista)))
print("Las ventas promedio mensuales totales son de: " +
      str(round(sum(ingreso_anual_lista) / sum(ventas_totales_lista), 2)))
