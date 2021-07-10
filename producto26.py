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
    if num < 17:
      print("Elegiste: Región",lista[num-1])
    return num
def mostrargrafico(region):
    print("hola soy un grafico de la región ",lista[region-1])

opcion = 0

def llamadografico(a):
  if a <17:
    pedirRespGraf()  
    grafico()
    mostrargrafico(a)
        

while True:
    mostrarregiones()
    opcion=pedirNumeroEntero()
    if opcion==17:
        break
    if opcion>17:
        print("\nPon un numero entre el 1 y el 17")
        break
    llamadografico(opcion)


print("Fin")

df = open("CasosNuevosConSintomas.csv", "r")

fechas = []
region1 = []
region2 = []
region3 = []
region4 = []
region5 = []
region6 = []
region7 = []
region8 = []
region9 = []
region10 = []
region11 = []
region12 = []
region13 = []
region14 = []
region15 = []
total16 = []

fechas1 = df.readlines(1)
for i in range(len(fechas1)):
  df2 =  fechas1[i]
  df2 = df2.split(",")
  fechas.append(df2)
  print("\n",fechas[0][100])
  x1 = fechas[0][100]
  x2 = x1 + fechas[0][101]
  x14 =fechas[0][114]
datafile2 = df.readlines(2)
for i in range(len(datafile2)):
  df2 =  datafile2[i]
  df2 = df2.split(",")
  region1.append(df2)
  print("\n",region1[0][0],":", region1[0][100])

datafile3 = df.readlines(3)
for i in range(len(datafile3)):
  df2 =  datafile3[i]
  df2 = df2.split(",")
  region2.append(df2)
  print("\n",region2[0][100])
  
datafile4 = df.readlines(4)
for i in range(len(datafile4)):
  df2 =  datafile4[i]
  df2 = df2.split(",")
  region3.append(df2)
  print("\n",region3[0][100])
  
datafile5 = df.readlines(5)
for i in range(len(datafile5)):
  df2 =  datafile5[i]
  df2 = df2.split(",")
  region4.append(df2)
  print("\n",region4[0][100])  

datafile6 = df.readlines(6)
for i in range(len(datafile6)):
  df2 =  datafile6[i]
  df2 = df2.split(",")
  region5.append(df2)
print("\n",region5[0][100]) 
  
datafile7 = df.readlines(7)
for i in range(len(datafile7)):
  df2 =  datafile7[i]
  df2 = df2.split(",")
  region6.append(df2)
  print("\n",region6[0][100])

datafile8 = df.readlines(8)
for i in range(len(datafile8)):
  df2 =  datafile8[i]
  df2 = df2.split(",")
  region7.append(df2)
  print("\n",region7[0][100])

datafile9 = df.readlines(9)
for i in range(len(datafile9)):
  df2 =  datafile9[i]
  df2 = df2.split(",")
  region8.append(df2)
  print("\n",region8[0][100])
  
datafile10 = df.readlines(10)
for i in range(len(datafile10)):
  df2 =  datafile10[i]
  df2 = df2.split(",")
  region9.append(df2)
  print("\n",region9[0][100])
  
datafile11 = df.readlines(11)
for i in range(len(datafile11)):
  df2 =  datafile11[i]
  df2 = df2.split(",")
  region10.append(df2)
  print("\n",region10[0][100])

datafile12 = df.readlines(12)
for i in range(len(datafile12)):
  df2 =  datafile12[i]
  df2 = df2.split(",")
  region11.append(df2)
  print("\n",region11[0][100])

datafile13 = df.readlines(13)
for i in range(len(datafile13)):
  df2 =  datafile13[i]
  df2 = df2.split(",")
  region12.append(df2)
  print("\n",region12[0][100])

datafile14 = df.readlines(14)
for i in range(len(datafile14)):
  df2 =  datafile14[i]
  df2 = df2.split(",")
  region13.append(df2)
  print("\n",region13[0][100])
  
datafile15 = df.readlines(15)
for i in range(len(datafile15)):
  df2 =  datafile15[i]
  df2 = df2.split(",")
  region14.append(df2)
  print("\n",region14[0][100])

datafile16 = df.readlines(16)
for i in range(len(datafile16)):
  df2 =  datafile16[i]
  df2 = df2.split(",")
  region15.append(df2)
  print("\n",region15[0][100])
  
datafile16 = df.readlines(16)
for i in range(len(datafile16)):
  df2 =  datafile16[i]
  df2 = df2.split(",")
  total16.append(df2)
  print("\n",total16[0][100])

  