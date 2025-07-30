prods = {}
cat = ('Hombre', 'Mujer', 'Niño')
tall = ('S','M''L','XL')
error_mesagge = '-'*50+'\n'+"✖"*5+"   Lo siento, intentelo nuevamente   "+"✖"*5

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print(error_mesagge)
    return value

n = input_integer("▶  Ingresa la cantidad que deseas agreagar: ")
for i in range(n):
    print("-"*20+f"PRODUCTO {i+1}"+"-"*20)
    while True:
        code = input("▶  Ingresa un codigo (Ej: P001): ")
        if code in prods: print("\nCodigo existente intente de nuevo")
        else: break
    prod = input("▶  Ingresa el nombre de tu producto: ")
    print("   1) Hombre\n   2) Mujer\n   3) Niño")
    cat_sel =  input_integer("▶  Ingresa la categoria: ")
    print("   1) S\n   2) M\n   3) L\n   4) XL")
    tal = input_integer("▶  Ingresa la talla: ")
    while True:
        while True:
            try:
                price = float(input("▶  Ingrese el precio: "))
                break
            except ValueError: print(error_mesagge)
        if price > 0: break
        else: print(error_mesagge)
    while True:
        stock = input_integer("▶  Ingrese la cantidad del stock: ")
        if stock > 0: break
        else: print(error_mesagge)

    prods[code] = {
        'name': prod,
        'categoria' : cat[cat_sel-1],
        'talla': tall[tal-1],
        'c/u': price,
        'stock' : stock
    }
print("-"*15+"PRODUCTOS"+"-"*15)
print(f"{'codigo':<10}{'nombre':<50}{'categoria':<20}{'talla':<20}{'Precio C/U':<20}{'Stock':<20}{'Valor Total':<25}")
for i,j in prods.items():
    print(f"{i:<10}{j['name']:<50}{j['categoria']:<20}{j['talla']:<20}{j['c/u']:<20}{j['stock']:<20}{j['c/u']*j['stock']:<25}")

code = input("▶  Ingresa un codigo (Ej: P001): ")
if code in prods:
    print(f"{'nombre':<50}{'categoria':<20}{'talla':<20}{'Precio C/U':<20}{'Stock':<20}{'Valor Total':<25}")

    print(f"{prods[code]['name']:<50}{prods[code]['categoria']:<20}{prods[code]['talla']:<20}{prods[code]['c/u']:<20}{prods[code]['stock']:<20}{prods[code]['c/u']*prods[code]['stock']:<25}")
else: print("Lo sentimos, el codigo no existe")

print("-"*15+"PRODUCTOS POR CATEGORIA"+"-"*15)
print(f"{'categoria':<20} {'cantidad':<10}")
for i in cat:
    count = 0
    for j in prods.values():
        if j['categoria'] == i: count+=1

    print(f"{i:<20}{count:<10}")