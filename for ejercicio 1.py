notas_acumuladas = 0

for estudiante in range(0,5,1):
    estudiante=int(input("Dijite la nota del estudiante"))
    notas_acumuladas= estudiante + notas_acumuladas

notas_promedio= notas_acumuladas/5
notas_acumuladas = 0

print(notas_promedio)
