# 	Practica M01_TE01_P01_S04

Se ha generado un fichero "Requeriments.txt" con los paquetes necesarios. El 
fichero con el código se encuentra en la ruta 
**"src\main\scripts\main.py"** y se han usado las siguientes librerías: 

- pytest para la realización de las pruebas. 
```bash
pytest src\test
```

- La librería coverage junto con pytest para medir la cobertura de las pruebas 
```bash
 coverage run -m pytest
 Coverage report --omit */site-packages/*
```

- Por último, la librería flake8 para revisar la calidad del código con el 
estándar PEP8 asi como la complejidad inferior a 8
```bash
flake8 --max-complexity 8 --statistics src/main
```