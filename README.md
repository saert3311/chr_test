
# Test CHR

Un proyecto de prueba en django para CHR


## Instalacion

Lo ideal es usar un entorno virtual de python (se recomienda 3.10) e instalar las dependencias que estan en requirements.txt

```bash
  python venv venv
```
Activar el entorno virtual en windows 
```bash
  /venv/scripts/activate
```
Una vez activo el entorno virtual se instalan las dependencias
```bash
  (venv) pip install -r requirements.txt
```

## db

django esta configurado para usar una db en postgres por lo que debes realizar los ajustes en el archivo settings.py




## Enlaces

Existen solo 2 enlaces que son 

/bikesantiago/ Para el punto 1, este toma los datos de la api y la muestra en una tabla ademas de haberlo guardado anteriormente

/scrapper/ Para el punto 2, tomar en cuenta que el proceso es largo dado que son varias paginas a buscar, igualmente se uso concurrencia para acelerar el proceso.

Para objeto de prueba cada vez que se entre en cada enlace la tabla se vaciara y se volvera a repetir el proceso para efectos de evaluacion