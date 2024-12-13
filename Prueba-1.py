def maximo_paneles(a, b, x, y):
    # Caso 1: Orientación original + aprovechar espacio sobrante con orientación rotada
    paneles_originales1 = (x // a) * (y // b)
    sobra_x1 = x % a  # Espacio sobrante horizontal
    sobra_y1 = y % b  # Espacio sobrante vertical
    paneles_en_sobra1 = (sobra_x1 // b) * (y // a) + (sobra_y1 // a) * (x // b)

    paneles_totales1 = paneles_originales1 + paneles_en_sobra1

    # Caso 2: Orientación rotada + aprovechar espacio sobrante con orientación original
    paneles_originales2 = (x // a) * (y // b)
    sobra_x2 = x % a  # Espacio sobrante horizontal
    sobra_y2 = y % b  # Espacio sobrante vertical
    paneles_en_sobra2 = (sobra_x2 // b) * (y // a) + (sobra_y2 // a) * (x // b)

    paneles_totales2 = paneles_originales2 + paneles_en_sobra2

    return max(paneles_totales1, paneles_totales2)

# Ejemplo 1
a1, b1 = 1, 2  # Dimensiones del panel solar
x1, y1 = 2, 4  # Dimensiones del techo

# Ejemplo 2
a2, b2 = 1, 2
x2, y2 = 3, 5

# Ejemplo 3
a3, b3 = 2, 2
x3, y3 = 1, 10

maximo_total1 = maximo_paneles(a1, b1, x1, y1)
maximo_total2 = maximo_paneles(a2, b2, x2, y2)
maximo_total3 = maximo_paneles(a3, b3, x3, y3)

print(f"La máxima cantidad de paneles solares que caben es:\n Ejemplo 1: {maximo_total1} \n Ejemplo 2: {maximo_total2} \n Ejemplo 3: {maximo_total3}")