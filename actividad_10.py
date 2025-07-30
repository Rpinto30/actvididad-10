prods = {}
cat = ('Hombre', 'Mujer', 'Niño')
tall = ('S','M','L','XL')
error_mesagge = '-'*50+'\n'+"✖"*5+"   Lo siento, intentelo nuevamente   "+"✖"*5

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print(error_mesagge)
    return value

while True:
    n = input_integer("▶  Ingresa la cantidad que deseas agreagar: ")
    if n > 0: break
    else: print(error_mesagge)
for i in range(n):
    print("-"*20+f"PRODUCTO {i+1}"+"-"*20)
    while True:
        code = input("▶  Ingresa un codigo (Ej: P001): ")
        if code in prods: print("\nCodigo existente intente de nuevo")
        else: break
    prod = input("▶  Ingresa el nombre de tu producto: ")
    while True:
        print("   1) Hombre\n   2) Mujer\n   3) Niño")
        cat_sel =  input_integer("▶  Ingresa la categoria: ")
        if 0 < cat_sel <=3: break
        else: print(error_mesagge)
    while True:
        print("   1) S\n   2) M\n   3) L\n   4) XL")
        tal = input_integer("▶  Ingresa la talla: ")
        if 0 < tal <= 4: break
        else: print(error_mesagge)
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
print("-"*25+"PRODUCTOS"+"-"*25)
print(f"{'Codigo':<10}{'Nombre':<25}{'Categoria':<20}{'Talla':<20}{'Precio C/U':<20}{'Stock':<20}{'Valor Total':<25}")
for i,j in prods.items():
    print(f"{i:<10}{j['name']:<25}{j['categoria']:<20}{j['talla']:<20}{'Q'+str(j['c/u']):<20}{j['stock']:<20}{'Q'+str(j['c/u']*j['stock']):<25}")

print("-"*25+"PRODUCTOS POR CATEGORIA"+"-"*25)
print(f"{'Categoria':<20} {'Cantidad':<10}")
for i in cat:
    count = 0
    for j in prods.values():
        if j['categoria'] == i: count+=1

    print(f"{i:<20}{count:<10}")

code = input("\n\n▶  Ingresa un codigo para visualizar su información por separado: ")
if code in prods:
    print(f"{'Nombre':<25}{'Categoria':<20}{'Talla':<20}{'Precio C/U':<20}{'Stock':<20}{'Valor Total':<25}")
    print(f"{prods[code]['name']:<25}{prods[code]['categoria']:<20}{prods[code]['talla']:<20}{'Q'+str(prods[code]['c/u']):<20}{prods[code]['stock']:<20}{'Q'+str(prods[code]['c/u']*prods[code]['stock']):<25}")
else: print("Lo sentimos, el codigo no existe")

