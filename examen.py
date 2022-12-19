print("Ingrese la cantidad de datos:")
numero1 = int(input())
for i in range(1,numero1+1):
    print("Ingrese el dato ",i,"")
    dato = float(input())
    acum = dato
prom=acum/numero1
print("El peormedio es:",prom)