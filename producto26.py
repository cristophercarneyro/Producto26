import matplotlib.pyplot as plt 
lista = ["de Arica y Parinacota(15)", "de Tarapacá(01)","de Antofagasta(02)","de Atacama(03)","de Coquimbo(04)","de Valparaíso(05)","Metropolitana de Santiago(13)","del Libertador Gral.Bernardo O’Higgins(06)","del Maule(07)","del Ñuble(16)","del BioBio(08)","de la Araucanía(09)","de Los Ríos(14)","de los Lagos(10)","Aisén del Gral.Carlos Ibáñez del Campo(11)","de Magallanes y la Antártica Chilena(12)"] #Agregamos cada región a una lista
lista2=["(15)","(01)","(02)","(03)","(04)","(05)","(13)","(06)","(07)","(16)","(08)","(09)","14","(10)","(11)","(12)"]
def mostrarregiones(): #creamos un def para dar la opción del gráfico que se desea ver.
  print("\n") #salto de línea
  print("      Elige una región: ") 
  j = 0 #valor inicial de j
  for i in range(16): #para i en el rango de 16(cantidad de regiones), entonces
    j = j + 1  # A j se le reasigna el valor, siendo este, el valor inicial, más 1.(sumamos 1, ya que python toma el primer caracter como 0)
    print(j,end='.')
    print(" Región",lista[i])#para imprimir "región" coma, cada elemento de  lista
  print("17. Salir") # para dar la opción al usuario de salir de la búsqueda
  print("INGRESAR: EL CODIGO CON LOS PARENTECIS")
  print("\n")

def pedirNumeroEntero(): #Creamos un def para verificar que el número ingresado es válido
    correcto = False #asignamos "correcto" al valor booleano False
    while (not correcto): 
        try:
            num = input("ingrese la región a elección: ")#se intenta transformar el valor ingresado por el usuario a entero
            j = 0
            for i in range(len(lista2)):
              j = j + 1
              num = num.replace(lista2[i], str(j) )

            num = int(num)
            correcto = True #correcto cambia de valor booleano a True
        except ValueError: 
            print('Error, introduce una región valida')
    if num < 17: #Si el número está dentro de la cantidad de caracteres en la lista
      print("Elegiste: Región",lista[num-1]) #se imprime Elegiste: Región, y la región escogida por el usuario. 
    return num

def datosGraficosRegionanocumulativa(region):
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
      xa = int(xa)
      casos.append(xa)
    y = casos
    x = fechas1
    plt.bar(x,y)
    plt.show()
    plt.ylabel('Casos nuevos')
    plt.xlabel('Ultimos 14 días')

    return plt    
def datosGraficosRegionacumulativa(region):
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
      casos.append(xa) 
    j= 0
    i = 0
    suma1 = [0]
    for i in range(0,len(casos)):
        suma = casos[i] +  suma1[j]
        suma1.append(suma)
        j = j +1
    del suma1[0]
    y = suma1
    x = fechas1
    plt.bar(x,y)
    plt.show()
    plt.ylabel('Casos nuevos')
    plt.xlabel('Ultimos 14 días')

    return plt
        
def grafico(regiona):#Creamos un def para mostrar los gráficos
  print("\n")
  print ("1. Mostrar un gráfico de contagiados con síntomas acumulativos")
  print("2. Mostrar un gráfico de contagiados con síntomas NO acumulativos")
  grafico = 0
  correcto = False
  while (not correcto): #Para verificar que ingresó el dato solicitado
      try:
          grafico = int(input("Ingrese el grafico a elección: "))
          correcto = True
      except ValueError:
          print('Error, introduce un grafico valido')
  if grafico == 2: 
    datosGraficosRegionacumulativa(regiona)
  if grafico == 1:
    datosGraficosRegionanocumulativa(regiona)
  
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