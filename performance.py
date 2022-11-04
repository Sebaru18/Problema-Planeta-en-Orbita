#Fichero para la prueba y comparativa rendimiento
#solo python con cython

import time
import py_planetaOrbita
import cy_planetaOrbita

"""

	Ejemplo usando datos del planeta TIERRA 
	La idea principal es crear un .csv con la 
	toma del tiempo
	
"""


planeta_cy = cy_planetaOrbita.Planet()
planeta_py = py_planetaOrbita.Planet()

#inicializacion planeta para python
planeta_py.x = 100*10**3
planeta_py.y = 300*10**3
planeta_py.z = 700*10**3
planeta_py.vx = 2.000*10**3
planeta_py.vy = 29.87*10**3
planeta_py.vz = 0.034*10**3
planeta_py.m = 5.9741*10**24


#inicializacion planeta para cython
planeta_cy.x = 100*10**3
planeta_cy.y = 300*10**3
planeta_cy.z = 700*10**3
planeta_cy.vx = 2.000*10**3
planeta_cy.vy = 29.87*10**3
planeta_cy.vz = 0.034*10**3
planeta_cy.m = 5.9741*10**24
""" variables adicionales """
time_span = 400
n_steps = 2000000 





formato_datos = "{:.5f},{:.5f}\n"



for i in range(2):

	iniciopy = time.time()
	print("python: ")
	py_planetaOrbita.step_time(planeta_py, time_span, n_steps)
	finalpy = time.time() - iniciopy



	iniciocy = time.time()
	print("cython: ")
	cy_planetaOrbita.step_time(planeta_cy, time_span, n_steps)
	finalycy = time.time()  - iniciocy	
	
	with open("tierra.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy, finalcy))
    
    
