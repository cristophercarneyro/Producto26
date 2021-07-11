import matplotlib.pyplot as plt 
lista = ["de Arica y Parinacota(15)", "de Tarapacá","de Antofagasta","de Atacama","de Coquimbo","de Valparaíso","Metropolitana de Santiago","del Libertador Gral.Bernardo O’Higgins","del Maule","del Ñuble","del BioBio","de la Araucanía","de Los Ríos","de los Lagos","Aisén del Gral.Carlos Ibáñez del Campo","de Magallanes y la Antártica Chilena"] #Agregamos cada región a una lista
def mostrarregiones(): #creamos un def para dar la opción del gráfico que se desea ver.
  print("\n") #salto de línea
  print("      Elige una región: ") 
  j = 0 #valor inicial de j
  for i in range(16): #para i en el rango de 16(cantidad de regiones), entonces
    j = j + 1  # A j se le reasigna el valor, siendo este, el valor inicial, más 1.(sumamos 1, ya que python toma el primer caracter como 0)
    print(j,end='.')
    print(" Región",lista[i])#para imprimir "región" coma, cada elemento de  lista
  print("17. Salir") # para dar la opción al usuario de salir de la búsqueda
  print("\n")
def pedirNumeroEntero(): #Creamos un def para verificar que el número ingresado es válido
    correcto = False #asignamos "correcto" al valor booleano False
    num = 0 
    while (not correcto): 
        try:
            num = int(input("ingrese la región a elección: "))#se intenta transformar el valor ingresado por el usuario a entero
            correcto = True #correcto cambia de valor booleano a True
        except ValueError: 
            print('Error, introduce una región valida')
    if num < 17: #Si el número está dentro de la cantidad de caracteres en la lista
      print("Elegiste: Región",lista[num-1]) #se imprime Elegiste: Región, y la región escogida por el usuario. 
    return num

def datosGraficosRegion(region):
    df = open("CasosNuevosConSintomas.csv", "r") #Asignamos fechas1 a la lectura de la primera línea, en este caso, la de todas las fechas.
    fechas = []
    casos=[]
    region1 = []
    fechas1 = []
    for i in range(18):
        datafile2 = df.readlines(i)
        for i in range(len(datafile2)):
          df2 =  datafile2[i]
          df2 = df2.split(",")
          region1.append(df2)
    for i in range(1,15):
      xe = region1[0][-i]
      xe = xe.replace("2021","21")
      fechas1.append(xe)

    for i in range(2,16):
      xa = region1[region][-i]
      xa = int(xa)
      casos.append(xa)
    y = casos
    x = fechas1
    plt.bar(x,y)
    plt.show()
    return casos,fechas,region,xe,xa

def datosGraficosRegion2(region):
    df = open("CasosNuevosConSintomas.csv", "r") #Asignamos fechas1 a la lectura de la primera línea, en este caso, la de todas las fechas.
    casos=[]
    region1 = []
    fechas1 = []
    for i in range(18):
        datafile2 = df.readlines(i)
        for i in range(len(datafile2)):
          df2 =  datafile2[i]
          df2 = df2.split(",")
          region1.append(df2)
    for i in range(1,15):
      xe = region1[0][-i]
      xe = xe.replace("2021","21")
      fechas1.append(xe)

    for i in range(2,16):
      xa = region1[region][-i]
      xa = xa.replace(".0","")
      xa = int(xa)
      print(xa)
      casos.append(xa) 
    suma =sum(casos)
    print("suma: ", suma)
    j= 0
    i = 0
    suma1 = [0]
    for i in range(0,len(casos)):
        suma = casos[i] +  suma1[j]
        suma1.append(suma)
        print("1:", suma1)
        j = j +1
    del suma1[0]
    y = suma1
    x = fechas1
    plt.bar(x,y)
    plt.show()

def grafico(regiona):#Creamos un def para mostrar los gráficos
  print("\n")
  print ("1. Mostrar un gráfico de contagiados con síntomas NO acumulativos")
  print("2. Mostrar un gráfico de contagiados con síntomas acumulativos")
  grafico = 0
  correcto = False
  while (not correcto): #Para verificar que ingresó el dato solicitado
      try:
          grafico = int(input("Ingrese el grafico a elección: "))
          correcto = True
      except ValueError:
          print('Error, introduce un grafico valido')
  if grafico == 1: 
    datosGraficosRegion(regiona)
    print("hola soy un grafico  con sintomas no acumulativos ")
    print("hola soy un grafico de la región ",lista[regiona-1])
  if grafico == 2:
    datosGraficosRegion2(regiona)
    print("hola soy un grafico  con síntomas acumulativos",regiona)     
    print("hola soy un grafico de la región ",lista[regiona-1])
  
  return grafico,regiona
  
opcion = 0  
while True:
    
    mostrarregiones()
    opcion=pedirNumeroEntero()
    if opcion < 17:
      grafico(opcion)
    if opcion == 17:
        break
    if opcion > 17:
        print("\nPon un numero entre el 1 y el 17")
        break
print("Fin")