#Compra de boletos para un concierto 


print('Vamos a hacer la compra de boletos para un concierto')
print('Recuerda responder unicamete "si" o "no"')
print('Antes que nada tienes qu elegir si lo vas hacer online o presencial ')

print('____________________________________________________________________')



Compra_online = input('¿Vamos a comprarlos presencial?').sprit().lower 
if Compra_online == 'si':
  print('Ingresar a la página web de su confiaza')
else:
  Compra_online == 'no'
  print('Ir al centro comercial donde vendan los boletos y sea de su entera confianza')

print('____________________________________________________________________')


Caro = input('¿Vamos a comprar los boletos más caros?').sprint().lower
if Caro == 'si':
  print('Elije la cantidad de boletos que necesites')
else:
  Caro == 'no'
  print('Mirar nuestra economía y ver para qué boletos alcanza')
  print('Ahora elije la cantidad de boletos que necesites')

print('____________________________________________________________________')

print('Elige el medio de pago')
medio_pago = input('Los medios de pago son: efectivo, crédito o debito').sprint().lower
if medio_pago == 'efectivo':
  print('Poner los datos que le pide, luego de recibir el código en celular dirígite al efecty más cercano a consignar el dinero')
elif medio_pago == 'crédito':
  print('verifica el cupo e la tarjeta, pon los datos y elije el número de cuotas')
else:
   medio_pago == 'debito'
   print('Verifica el saldo de la tarjeta y pon los datos que te pidan')

print('____________________________________________________________________')

print('Verifica si la verificación de compra de los boletos llegó al correo')
llego = input('¿Llegó o no llegó?').sprint().lower 
if llego == 'si':
  print('Perfecto, la compra fue exitosa')
else: 
  llego == 'no'
  print('Llamar a la entidad donde se hizo la compra y verificar por qué los boletos no llegaron al correo y encontrar la solución.')
  print('Ahora que se aclaró el inconveniente ya tienes tus boletos')

print('____________________________________________________________________')
print('Disfruta el concierto')

