#Fichero para la prueba y comparativa rendimiento
#solo python con cython

import time
import py_planetaOrbita
import cy_planetaOrbita

planeta_cy = cy_planetaOrbita.Planet()
planeta_py = py_planetaOrbita.Planet()


init_time = time.time()
print("python: ")
py_planetaOrbita.step_time(planeta_py, 33.5,5)
fin_time = time.time()
total_time_python = fin_time - init_time
print("tiempo total python: ", total_time_python)


init_time = time.time()
print("cython: ")
cy_planetaOrbita.c_step_time(planeta_cy, 33.5,5)
fin_time = time.time()
total_time_cython = fin_time - init_time
print("tiempo total cython: ", total_time_cython)

print(f"cython es {total_time_python/total_time_cython} mas rapido que python")