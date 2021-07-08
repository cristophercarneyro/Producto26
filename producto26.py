import matplotlib.pyplot as plt

def pedirRespGraf():
  print("\n")
  print ("1. Mostrar un gráfico de contagiados con síntomas NO acumulativos")
  print("2. Mostrar un gráfico de contagiados con síntomas acumulativos")

def grafico():      
  grafico = 0
  correcto = False
  while (not correcto):
      try:
          grafico = int(input("ingrese el grafico a elección: "))
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

    return num

salir = False
opcion = 0

while not salir:
    print("\n")
    print("1.  Arica y parinacota ")
    print("2.  Tarapacá ")
    print("3.  Antofagasta ")
    print("4.  Atacama ")
    print("5.  Coquimbo ")
    print("6.  Valparaíso  ")
    print("7.  Metropolitana de Santiago")
    print("8.  Región del Libertador Gral.Bernardo O’Higgins")
    print("9.  Región del Maule")
    print("10. Región del Ñuble.")
    print("11. Región del BioBio")
    print("12. Región de la Araucanía")
    print("13. Región de Los Ríos")
    print("14. Rgión de los Lagos ")
    print("15. Región Aisén del Gral.Carlos Ibáñez del Campo")
    print("16. Región de Magallanes y la Antártica Chilena	")
    print("17. Salir")
    print("\n")
    print("       Elige una opcion")

    opcion = pedirNumeroEntero()
    print("Elegiste:",end=' ')
    if opcion == 1:
        print("Arica y parinacota ")
        pedirRespGraf()  
        grafico()
        
        
    elif opcion == 2:
        print("Tarapacá")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 3:
        print("Antofagasta")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 4:
        print("Atacama")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 5:
        print("Coquimbo")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 6:
        print("Valparaíso")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 7:
        print("Metropolitana de Santiago")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 8:
        print("Región del Libertador Gral.Bernardo O’Higgins")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 9:
        print("hola")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 10:
        print("hola")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 11:
        print("hola")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 12:
        print("Región de la Araucanía")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 13:
        print("Región de Los Ríos")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 14:
        print("Región de los Lagos")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 15:
        pedirRespGraf()  
        grafico()
        
    elif opcion == 16:
        print("Región de Magallanes y la Antártica Chilena")
        pedirRespGraf()  
        grafico()
        
    elif opcion == 17:
        salir = True

    else:
        print("Introduce un numero entre 1 y 16")

print("Fin")
