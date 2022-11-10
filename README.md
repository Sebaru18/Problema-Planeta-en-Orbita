# Problema-Planeta-en-Orbita 
### Sebastian Andres Ruiz Garcia


Se realiza la comparación de rendimiento de la aplicación de las orbitas,
teniendo en cuenta que este sera ejecutado con el codigo original en 
python, frente al codigo en Cython, en el que se modifican ciertos elementos
para tener un mejor rendimiento.

el archivo en python se llama py_planetaOrbita.py siendo el codigo original, ahora el de cython se llamaria cy_planetaOrbita.pyx el cual fue modificado para tener elementos de C.



se encuentra el setup.py el cual se encarga de convertir a cython la aplicacion cy_planetaOrbita.pyx.


tambien se debe tener en cuenta el performance.py, este, que es la bateria de experimentos es el que va a ejecutar una cantidad de veces (30 veces) los programas, tanto en cython y python, y va guardando los tiempos de ejecución en un archivo csv que crea. 


Los resultados se podran observar el repositorio, un archivo que se llama Resultados.ipynb.
