
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

django esta configurado para usar una db en postgres tiene el usuario y la contraseña por defecto, igualmente puedes crear
la bd que se llamara chr donde se haran las migraciones respectivas




## Enlaces

Existen solo 2 enlaces que son 

http://127.0.0.1:8000/citibik/bikerio/ Para el punto 1, este toma los datos de la api y la muestra en una tabla ademas de haberlo guardado anteriormente

bikerio se pasa como argumento por lo que podrian consultarse otros endpoins de http://api.citybik.es/v2/networks

Claro se necesitaria mas pruebas y ajustes si hay discrepancias entre la informacion proporcionada pero la funcionalidad base ya esta.

/scrapper/ Para el punto 2, tomar en cuenta que el proceso es largo dado que son varias paginas a buscar, igualmente se uso concurrencia para acelerar el proceso.

Para objeto de prueba cada vez que se entre en cada enlace la tabla se vaciara y se volvera a repetir el proceso para efectos de evaluacion