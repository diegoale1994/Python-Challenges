#codigo para saber cuando un numero es primo
'''
def resultado(final):
	if estado==True:
		print("el numero ingresado no es primo")
	else:
		print("el numero ingresado es primo")

varia = int(input("ingresa un numero: \n"))
estado = False
for i in range(2,varia,1):
	if varia%i == 0:
		estado= True
		break
resultado(estado)
'''
'''
lista = ["perro","gato",15]
print(lista[:])#muestra toda la lista
print(lista[2])#mustra gato
print(lista[2:])#imprime partes de la lista
lista.append(input("ingrese algo"))#append "agregar a la lista al final" insert "agrega al final de la lista"
lista.insert(0,input("ingrese algo"))#append "agregar a la lista al final" insert "agrega al final de la lista"
lista.extend(["megadeth","ursus"])#extend ingresa varios elementos al tiempo
print(lista[:])
print(lista.index("ursus"))
#buscar un elemnto en una lista
print(15 in lista)
lista.remove("gato")

print(lista[:])
lista.pop() #elimina el ultimo valor de la lista
'''
'''
lista2 = []
tamaño = int(input("ingrese el tamaño del array "))
for i in range(0,tamaño,1):
	lista2.append(int(input("ingresa un valor a la lista: ")))
print(lista2[:])
'''
'''
tupla = ("juan",15,"slayer","embriont")
lista = list(tupla)#combierte una tupla en una lista [listas] (tuplas)
tupla2 = tuple(lista)#combierte una lista en una tupla [listas] (tuplas)

print(lista[:])
print(tupla)
print(tupla2)
'''
'''
tupla = ("juan",15,"slayer","embriont")
tupla_sin_parentesis = "juani",150,"slayers","embrionte" #empaquetado de tupla
nombre,numero,banda,banda2 = tupla_sin_parentesis #asignando variables independientes a los vaores de na tupla,"desempaquetado de tupla"
print(15 in tupla)
print(tupla.count("juan")) #contar cuantas veces esta un elemento en un objeto
print(len(tupla))
tupla_Unitaria=(1,)
print(len(tupla_Unitaria))
print(banda)
'''
#DICCIONARIOS
'''
diccionario = {"colombia":"bogota","venezuela":"caracas","peru":"lima"}
print(diccionario["colombia"])
diccionario["argentina"]="brasilia"
print(diccionario)
diccionario["argentina"]="buenos aires"
print(diccionario)
del(diccionario["venezuela"])
print(diccionario)
'''
'''
dic = {"nombre":"diego", "edad":22, "estudios":["primarios","secundarios","pregrado"]}
print(dic["estudios"])
print(dic.keys())
print(dic.values())
print(len(dic))
'''
'''
numero1 = int(input("ingrese el primer numero"))
numero2 = int(input("ingrese el segundo numero"))
if numero1 > numero2:
	print(str(numero1)+" es mayor que: "+ str(numero2))
elif numero2 > numero1:
	print(str(numero2)+" es mayor que: "+ str(numero1))
else:
	print("los numeros son iguales")
'''
'''
lista = []
lista.append(input("ingrese el nombre "))
lista.append(input("ingrese el Direccion "))
lista.append(input("ingrese el telefono "))
print("los datos personales son:")
for i in lista:
	print(i)
'''
'''
nums = 1
i= 1
while i <=100:
	band=False
	for x in range(2,i,1):
		if i%x==0:
			band=True
			break
	if band==False:
		print(str(nums)+"-"+str(i))
		nums+=1
	i+=1
'''
'''
i=1
a=0
b=1
while c<13:
	c=a+b
	print(str(i)+"-"+str(c))
	a=b
	b=c
	i+=1
'''
'''
for x in range(1,100,1):
	if x % 5 == 0 and x %3==0 :
		print(str(x)+" FizzBuzz")
	elif x %3==0 or '3' in str(x):
		print(str(x)+" frizz")
	elif x % 5 ==0 or '5' in str(x):
		print(str(x)+" Buzz")
	else:
		print(x)
'''
'''
cantidad_numeros=1
numero_inicial=0
numero_final=1
aux=0 
while aux<=100:
	aux=numero_inicial+numero_final
	print(str(cantidad_numeros)+"-"+str(aux))
	numero_inicial=numero_final
	numero_final=aux
	cantidad_numeros+=1
'''
'''
def burbuja(array):

	band=0
	while band == 0:
		band=1
		for i in range(0,len(array)-1,1):
			if array[i]>array[i+1]:
				aux = array[i]
				array[i]=array[i+1]
				array[i+1]=aux
				band = 0
	return array
def burbuja1(array):

	band=0
	while band == 0:
		band=1
		for i in range(0,len(array)-1,1):
			if array[i]<array[i+1]:
				aux = array[i]
				array[i]=array[i+1]
				array[i+1]=aux
				band = 0
	return array
 
print("Constante de Kaprekar")
numero = 1121
constante=0
iteraciones=0

while constante !=  6174:
	mayor =""
	menor =""
	array1=[]
	iteraciones+=1
	for x in str(numero).zfill(4):
		array1+=[int(x)]
	array_menor_mayor=burbuja(array1)
	for x in array_menor_mayor:
		menor+=str(x)
	array_mayor_menor=burbuja1(array1)
	for x in array_mayor_menor:
		mayor+=str(x)
	if int(mayor)-int(menor) ==  6174:
		constante = 6174
		print(int(mayor)-int(menor))
	else:
		numero = int(mayor)-int(menor)
		
print("iteraciones "+str(iteraciones))
'''
''' encriptacion cesar
palabra = "megadeth"
palabracript=""
palabradecript=""
letra = "b"
st = ['a','b','c','d','e','f','g','h','i','j','k','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
for x in palabra:
	if st.index(x)+st.index(letra)>=len(st):
		palabracript+=st[(st.index(x)+st.index(letra))-(len(st))]
	else:
		palabracript+=st[st.index(x)+st.index(letra)]
print(palabracript)
for x in palabracript:
	if st.index(x)-st.index(letra)<0:
		palabradecript+=st[(len(st))-(st.index(x)+st.index(letra))]
	else:
		palabradecript+=st[st.index(x)-st.index(letra)]
print(palabradecript)

'''
'''decimal a binario
num = 1465899
est = False
bina=""
while est == False:
	if num % 2 == 0:
		bina +="0"
	else:
		bina +="1"
	if(num == 1):
		est = True
	num = int(num / 2)
binar = bina[::-1]
print(binar)
'''
'''
num = 823
est = False
while(est==False):
	
	if int(num/8)==0:
		est = True
	print (num%8)
	num = int(num/8)
print("hasta aca")
num = 823
est = False
while(est==False):
	
	if int(num/5)==0:
		est = True
	print (num%5)
	num = int(num/5)
'''
class Carro():
	largo = 4.5
	ancho = 1.2
	ruedas = 4
	enmarcha = False
	