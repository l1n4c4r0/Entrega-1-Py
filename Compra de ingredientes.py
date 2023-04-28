print('Hoy vamos a comprar ingredietes para una receta.')
print('La receta es una Pizza')
print('Responde sólamente "si" o "no"')
print('____________________________________________________________________')

Tienda_presencial = input('¿Vamos a hacer la compra en una tienda presencial?' ).lower 
if Tienda_presencial == ('si'):
  print('Vamos a la tienda de su preferencia y tomemos un carrito de compras')
else:
  Tienda_presencial == ('no')
  print('Vamos a internet, buscamos una tienda de preferencia y vamos a la sección de alimentos')
print('____________________________________________________________________')

print('Empecemos con la masa')
Masa_hecha = input('¿Está disponible la masa hecha?' ).lower 
if Masa_hecha == ('si'):
  print('Excelente, vamos a ponerla en el carrito de compras')
else:
  Masa_hecha == ('no')
  print('vamos a comprar los ingredientes que necesitemos para hacer la masa')
  print('Necesitamos 1 huevo, arina de trigo y agua')
print('Ya que encontramos los ingredietes vamos a ponerlos en la canasta de compras')
print('____________________________________________________________________')
print('Ahora vamos a buscar los demás ingredientes')
print('Necesitamos: Queso, salsa de tomate, pecchuga de pollo y champiñones frescos')

print('____________________________________________________________________')
disponibilidad = input('¿Todos los ingredienetes están disponibles?' )
if disponibilidad == ('si'):
  print('Excelente, vamos a agregarlos a la canasta de compras y vamos a pagar la compra')
  print('¡Listo, ya compramos los ingredientes para la receta')
else:
  disponibilidad == ('no')
  print('Entonces vamos a pagar los ingredientes que tenemos en la canasta de compras')
  print('Ahora, vamos a otra tienda por los ingredientes que hagan falta')
  print('Busquemos los ingredientes, los agregamos a la canasta de compras y vamos a pagar la compra')
  print('¡Listo, ya compramos los ingredientes para la receta')
print('Fin')