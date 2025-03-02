###################################################################
# 1. Problema de Candidatos y Votos
import numpy as np

candidates = np.arange(1, 31)

votes = np.random.randint(50, 100, size=30)
diff = 5000 - np.sum(votes)

random_candidate = np.random.randint(0, 30) 
votes[random_candidate] += diff  

sorted_indices = np.argsort(votes)[::-1]  
sorted_candidates = candidates[sorted_indices]  
sorted_votes = votes[sorted_indices]  

print("Resultados de la elección:")
for i in range(len(sorted_candidates)):
    print(f"Candidato {sorted_candidates[i]}: {sorted_votes[i]} votos")


###################################################################
# 2. Problema de promedios 

num_students = 6500
students = np.array([
    np.arange(100000, 100000 + num_students), # Code
    np.random.choice(["Juan", "María", "Pedro", "Ana", "Carlos", "Laura"], num_students), # Name
    np.random.randint(1980, 2023, num_students), # Year
    np.random.uniform(1.0, 5.0, num_students), # Avg
    np.random.randint(1, 10, num_students) # Career
]).T

codigo_carrera = int(input("Ingrese el código de la carrera a listar: "))

# First filter
filtro1 = (students[:, 4].astype(int) == codigo_carrera) & (students[:, 3].astype(float) >= 4.0)
estudiantes_filtrados = students[filtro1][:, [0, 1]]
cantidad_filtrados = len(estudiantes_filtrados)

print("\n Estudiantes de la carrera", codigo_carrera, "con promedio >= 4:")
for estudiante in estudiantes_filtrados:
    print(f"Código: {int(estudiante[0])}, Nombre: {estudiante[1]}")
print(f"Total: {cantidad_filtrados} estudiantes.\n")

# Second filter
filtro2 = (students[:, 2].astype(int) < 1990) & (students[:, 3].astype(float) < 3.0)
estudiantes_condicionales = students[filtro2][:, [0, 1]]


print("\n Estudiantes que ingresaron antes de 1990 y están condicionales:")
for estudiante in estudiantes_condicionales:
    print(f"Código: {int(estudiante[0])}, Nombre: {estudiante[1]}")
print(f"Total: {len(estudiantes_condicionales)} estudiantes.")