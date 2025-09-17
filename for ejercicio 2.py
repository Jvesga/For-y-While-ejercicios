notas_acumuladas1= 0
notas_acumuladas2= 0

for estudiante in range(0,3,1):
    estudiante1=int(input(f"Dijite la nota {estudiante+1} estudiante 1: "))
    estudiante2=int(input(f"Dijite la nota {estudiante+1} estudiante 2: "))
    notas_acumuladas1= estudiante1 + notas_acumuladas1
    notas_acumuladas2= estudiante2 + notas_acumuladas2


notas_promedio1= notas_acumuladas1/3
notas_promedio2= notas_acumuladas2/3


print(f"Nota promedio estudiante 1: {notas_promedio1}")
print(f"Nota promedio estuadiante 2: {notas_promedio2}")