a=1
while True:
    print("Bienvenido\n")
    print ("1.calcular area de un triangulo \n" "2.ingresar dos numeros y sumarlos\n" "3.ingresasr un numero y elevarlo por si mismo\n" "4.escribir un algoritmo que convierta de eutos a dolares\n" "5.escrubir un algoritmo que pide el lado de un cuadrado y muestre el valor del area y del perimetro\n" "6.Escribir un algoritmo que determine el area y el volumen de un cilindro\n" "7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el area\n" "8.calcular el promedio de 3 numero ingresados en el teclado\n")
    menu=int(input("seleccione el ejercicio a realizar:\n"))
    if(menu==1):
            print("Calcular el area de un triangulo\n   ")
            base1=float (input("Porfavor, base del triangulo 1\n"))
            base2=float (input("Porfavor, altra del triangulo 2\n"))
            resultado=(base1*base2)/2
            print("el area del triangulo es"+str (resultado))
    if(menu==2):
            print("perfecto, ahora el segundo ejercicio.")
            num1=float (input("Porfavor, dijite el primer numero\n"))
            num2=float (input("Porfavor, dijite el segundo numero\n"))
            resultado=(num1+num2)
            print("el regultado es"+str (resultado)) 
    if(menu==3):
            print("muy bien ahora algo un poco mas complejo, elevar un numero\n")
            num3=float(input("Porfavor, dijite el primer numero\n"))
            resultado=(num3*num3)
            print("el regultado es"+str (resultado))
    if(menu==4):  
            print("Texto, ingresa el monto por conocer\n")
            dolares = float (input ('Ingresa valor: '))
            euros=dolares*1.08
            print ('Valor es: '+str(euros))
    if(menu==5):
            print("ingrese el lado de un cuadrado y a continuacion mostrara el valor del área y el perimetro\n")
            num5=float(input("ingrese el tamaño de uno de sus lados del cuadrado (Area):\n"))
            num6=float(input("ingrese el tamaño de uno de sus lados del cuadrado (Perimetro):\n"))
            resultado=(num5*num5)
            resultado2=(num6+num6+num6+num6)
            print("El area del cuadrado es de: "+str(resultado))
            print("El perimetro del cuadrado es de: "+str(resultado2))
    if(menu==6):
            print("Ingrese el área y el volúmen de un cilindro\n")
            num7=float(input("radio del cilindro "))
            num8=float(input("altura del cilindro "))
            resultado=(2*3.1416*num7*(num7+num8))
            resultado2=(3.1426*num8*(num7+num7))
            print("area es"+str(resultado))
            print("volumen es"+str(resultado2))
    if(menu==7):
            print("Radio de una circunferenci\n")
            num9=float(input("radio\n"))
            num10=float(input("altura\n"))
            resultado2=(2*3.1416*num10*(num10*num9))    
            resultado3=(3.1416*num9*(num10*num10)) 
            print("area es"+str(resultado2))
            print("volumen es"+str(resultado3))
    if(menu==8):
            print("Calcular el promedio de tres (3) números ingresados\n")
            num11=float(input("ingrese el 1er numero "))
            num12=float(input("ingrse el 2do numero "))
            num13=float(input("ingrse el 3er numero "))
            resultado=(num11+num12+num13/3)
            print("el promedio de los numeros es de"+str(resultado))
            respuesta=input("desea continuar Y o 99 para terminar\n")
    if(respuesta=="Y"or respuesta=="99"):
        break
else:
       print()