#el dominio seria una pareja de numeros R y C los cuales son enteros
#el codominio es un rango de posibles fracciones que genere nuestro codigo


def crearfracciones(c, r):
    fracciones = set()
    fracciones_vistas = set()  # Almacenamos las fracciones que ya hemos visto
    for den in range(1000, 1000000,):
        num = c * den
        if num < 10**5:
            if num / den == c and (num, den) not in fracciones_vistas:
                fracciones.add((num, den))
                fracciones_vistas.add((num, den))
    return fracciones

def apariciones_de_N(num, den):
    apariciones = {}
    while num > 0 or den > 0:
        digito_num = num % 10
        digito_den = den % 10
        apariciones[digito_num] = apariciones.get(digito_num, 0) + 1
        apariciones[digito_den] = apariciones.get(digito_den, 0) + 1
        num //= 10
        den //= 10
    return apariciones

T = int(input())
casos_de_prueba = []
for _ in range(T):
    c, r = map(int, input().split())
    casos_de_prueba.append((c, r))

for i, (c, r) in enumerate(casos_de_prueba):
    fracciones = crearfracciones(c, r)
    if fracciones:  # Solo imprimimos si hay fracciones
        for num, den in sorted(fracciones):
            apariciones = apariciones_de_N(num, den)
            if all(v <= r for v in apariciones.values()):
                print(f"{num}/{den}={num/den}")
        if i < len(casos_de_prueba) - 1:  
            print()
