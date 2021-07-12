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
  print("17. Comparación")
  print("18. Salir") # para dar la opción al usuario de salir de la búsqueda
  print("\n")
  print("INGRESAR EL CODIGO DE REGIÓN CON LOS PARENTECIS\nSI SE QUIERE USAR ESTE MISMO")
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
    if num <= 16: #Si el número está dentro de la cantidad de caracteres en la lista
      print("Elegiste: Región",lista[num-1]) #se imprime Elegiste: Región, y la región escogida por el usuario. 
    return num #para volver a num con su valor inicial

def datosGraficosRegionanocumulativa(region):
    df = open("CasosNuevosConSintomas.csv", "r") #Asignamos fechas1 a la lectura de la primera línea, en este caso, la de todas las fechas.
    casos=[] #listas vacias para guardar los datos de ma lectura
    region1 = []
    fechas1 = []
    for i in range(18):
        datafile2 = df.readlines(i)
        for i in range(len(datafile2)):
          df2 =  datafile2[i]
          df2 = df2.split(",")
          region1.append(df2)#guardamos la lectura de df2
    for i in range(1,15):
      xe = region1[0][-i]
      xe = xe.replace("2021","21")
      fechas1.append(xe)#guardamos la lectura de xe

    for i in range(2,16):
      xa = region1[region][-i]
      xa = int(xa)
      casos.append(xa)#guardamos la lectura de xa
    y = casos #asignamos los datos almacenados en lista casos a y
    x = fechas1 #asignamos los datos almacenados en lista fechas1 a x
    plt.bar(x,y) #creamos el grafico utilizando los valores almacenados
    plt.ylabel('Casos nuevos')
    plt.xlabel('Ultimos 14 días')
    plt.show()
    return plt #para volver al valor inicial de plt 
def datosGraficosRegionacumulativa(region):
    df = open("CasosNuevosConSintomas.csv", "r") #Asignamos fechas1 a la lectura de la primera línea, en este caso, la de todas las fechas.
    casos=[]
    region1 = []
    fechas1 = []
    for i in range(18):#para "i" en rango "18"
        datafile2 = df.readlines(i)
        for i in range(len(datafile2)):
          df2 =  datafile2[i]
          df2 = df2.split(",")
          region1.append(df2)#guardamos la lectura de "df2", en lista "region1"
    for i in range(1,15):
      xe = region1[0][-i]
      xe = xe.replace("2021","21")
      fechas1.append(xe)#guardamos la le tura de "xe", en lista "fechas1"

    for i in range(2,16):#para i en rango de 2 a 16
      xa = region1[region][-i]
      xa = xa.replace(".0","")
      xa = int(xa)
      casos.append(xa) #guardamos la lectura de "xa" en lista "casos"
    j= 0#asignamos
    i = 0#valores
    suma1 = [0]#iniciales
    for i in range(0,len(casos)):#para i en rango cero y el largo de lista "casos"
        suma = casos[i] +  suma1[j]
        suma1.append(suma)#guardamos la suma de lista "casos" con valor "i" mas lista suma1 con valor "j"
        j = j +1 #se me asigna "j" al valor de j mas 1
    del suma1[0] #borramos el elemento inicial de la lista
    y = suma1 #asignamos y a los valores almacemados en lista "suma1"
    x = fechas1 #asigamos x a los valores almacenados en llsta "fechas1"
    plt.bar(x,y) #creamos el gráfico con los valores x e y
    plt.ylabel('Casos nuevos')
    plt.xlabel('Ultimos 14 días')
    plt.show()
    return plt #retornamos al valor inicial de plt
        
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
  if grafico == 2: #si el valor ingresado es igual a 2, entramos al def que contiene la información solicitada
    datosGraficosRegionacumulativa(regiona)
  if grafico == 1: #si es 1, entonces entramod al otro def con la otra informacion 
    datosGraficosRegionanocumulativa(regiona)

def datosGraficosRegion2():
    df = open("CasosNuevosConSintomas.csv", "r") #Asignamos fechas1 a la lectura de la primera línea, en este caso, la de todas las fechas.
    casos=[]
    casos2 = []
    casos3 = []
    casos4 = []
    casos5 = []
    casos6 = []
    casos7 = []
    casos8 = []
    casos9 = []
    casos10 = []
    casos11 = []
    casos12 = []
    casos13 = []
    casos14 = []
    casos15= []
    casos16= []
    region1 = []
    fechas1 = []
    norte = []
    centro =[]
    sur = []
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
      xa = region1[1][-i]
      xa = xa.replace(".0","")
      xa = int(xa)
      casos.append(xa) 
    for i in range(2,16):   
     xa = region1[2][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos2.append(xa) 
    for i in range(2,16):    
     xa = region1[3][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos3.append(xa) 
    for i in range(2,16):
     xa = region1[4][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos4.append(xa) 
    for i in range(2,16):  
     xa = region1[5][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos5.append(xa) 
    suma  =sum(casos)
    suma2 =sum(casos2)
    suma3 = sum(casos3)
    suma4 = sum(casos4)
    suma5 = sum(casos5)
    norte.append(suma)
    norte.append(suma2)
    norte.append(suma3)
    norte.append(suma4)
    norte.append(suma5)
    for i in range(2,16):  
     xa = region1[6][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos6.append(xa) 
    for i in range(2,16):  
     xa = region1[7][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos7.append(xa) 
    for i in range(2,16):  
     xa = region1[8][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos8.append(xa) 
    for i in range(2,16):  
     xa = region1[9][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos9.append(xa)
    for i in range(2,16):  
     xa = region1[10][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos10.append(xa) 
    suma6  =sum(casos6)
    suma7 =sum(casos7)
    suma8 = sum(casos8)
    suma9 = sum(casos9)
    suma10 = sum(casos10)
    centro.append(suma6)
    centro.append(suma7)
    centro.append(suma8)
    centro.append(suma9)
    centro.append(suma10)
    for i in range(2,16):  
     xa = region1[11][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos11.append(xa) 
    for i in range(2,16):  
     xa = region1[12][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos12.append(xa)
    for i in range(2,16):  
     xa = region1[13][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos13.append(xa)    
    for i in range(2,16):  
     xa = region1[14][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos14.append(xa) 
    for i in range(2,16):  
     xa = region1[15][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos15.append(xa)
    for i in range(2,16):  
     xa = region1[16][-i]
     xa = xa.replace(".0","")
     xa = int(xa)
     casos16.append(xa)   
    suma11  =sum(casos11)
    suma12 =sum(casos12)
    suma13 = sum(casos13)
    suma14 = sum(casos14)
    suma15 = sum(casos15)
    suma16 = sum(casos16)
    sur.append(suma11)
    sur.append(suma12)
    sur.append(suma13)
    sur.append(suma14)
    sur.append(suma15)
    sur.append(suma16)
    print("\n")
    print("Elija la zona para comparar entre zonas de chile que region tiene mas o menos contagiados ")
    print ("1. norte")
    print("2. centro")
    print("3. sur")
    comparativa = 0
    real = False
    while (not real): #Para verificar que ingresó el dato solicitado
        try:
            comparativa = int(input("Ingrese el opción a elección: "))
            real = True
        except ValueError:
            print('Error, introduce una opción valida')
    if comparativa == 1: 
      y = norte
      x = ["arica y parinacota", "Tarapacá","Antofagasta", "Atacama", "Coquimbo"]
      plt.bar(x,y)
      plt.show()
    if comparativa == 2:
      y = centro
      x = ["Valparaíso","Santiago","O’Higgins","Maule","Ñuble"]
      plt.bar(x,y)
      plt.show()    
    if comparativa == 3:
      y = sur
      x = ["Bio-Bio","La Araucanía","Los Ríos","los Lagos","Aisén","Magallanes y la Antártica Chilena"]
      plt.bar(x,y)
      plt.show()  
  
opcion = 0  
while True:
      #solo llamamls la información almacenada en los def
    mostrarregiones()
    opcion=pedirNumeroEntero()
    if opcion == 17:
      datosGraficosRegion2()
    if opcion <= 16:
      grafico(opcion)
      print("2")
    if opcion == 18: #18 en el menú es salir, asique, rompe, y finaliza.
        break
    if opcion > 18: #si es mayor que 18, no está dentro de las opciones, por ende, se me pide al usuario más especifico que valor debe ingresar.
        print("\nPon un numero entre el 1 y el 18")
        break
print("Fin")