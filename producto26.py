import matplotlib.pyplot as plt
lista = ["de Arica y Parinacota", "de Tarapacá","de Antofagasta","de Atacama","de Coquimbo","de Valparaíso","Metropolitana de Santiago","del Libertador Gral.Bernardo O’Higgins","del Maule","del Ñuble","del BioBio","de la Araucanía","de Los Ríos","de los Lagos","Aisén del Gral.Carlos Ibáñez del Campo","de Magallanes y la Antártica Chilena"]

def mostrarregiones():
  print("\n")
  print("      Elige una región: ")
  j = 0
  for i in range(16):
    j = j + 1 
    print(j,end='.')
    print(" Región",lista[i])
  print("17. Salir")
  print("\n")

def pedirRespGraf():
  print("\n")
  print ("1. Mostrar un gráfico de contagiados con síntomas NO acumulativos")
  print("2. Mostrar un gráfico de contagiados con síntomas acumulativos")

def grafico():      
  grafico = 0
  correcto = False
  while (not correcto):
      try:
          grafico = int(input("Ingrese el grafico a elección: "))
          correcto = True
      except ValueError:
          print('Error, introduce un grafico valido')
  if grafico == 1:
    print("hola soy un grafico  con sintomas no acumulativos ")
  if grafico == 2:
    print("hola soy un grafico  con síntomas acumulativos")     
  return grafico
def pedirNumeroEntero():

    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("ingrese la región a elección: "))
            correcto = True
        except ValueError:
            print('Error, introduce una región valida')
    if not num == 17:
      print("Elegiste: Región",lista[num-1])
    return num
def mostrargrafico():
    print("hola")


salir = False
opcion = 0

while not salir:
    
    mostrarregiones()
    opcion = pedirNumeroEntero()

    for i in range(16) :
      if opcion == i:
        pedirRespGraf()  
        grafico()
        mostrargrafico()
      elif opcion == 17:
          salir = True

    else:
        print("Introduce un numero entre 1 y 17")

print("Fin")
