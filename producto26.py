import matplotlib.pyplot as plt


def mostrarregiones():
  print("\n")
  print("      Elige una región: ")
  j = 0
  for i in range(15):
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
    
salir = False
opcion = 0

while not salir:
    
    mostrarregiones()
    opcion = pedirNumeroEntero()

    if opcion == 1:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 2:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 3:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 4:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 5:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 6:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 7:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 8:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 9:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 10:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 11:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 12:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 13:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 14:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 15:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 16:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 17:
        salir = True

    else:
        print("Introduce un numero entre 1 y 17")

print("Fin")
