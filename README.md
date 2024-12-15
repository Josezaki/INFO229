# Introducción 👋

...

## Backend

...

### API

Para la API se utilizó [fastAPI](https://fastapi.tiangolo.com).

#### Requisitos:

1. Instalar [Python](https://www.python.org/downloads/) para poder ejecutar los comandos de pip.
2. Entorno virtual y dependencias:

   - Crear un entorno virtual:
      ```bash
      python -m venv venv
      ```
   - Activar el entorno virtual:

      En Windows:

      ```bash
      .\venv\Scripts\activate
      ```
      
      En Linux/Mac:
      ```bash
      . venv/bin/activate
      ```
   - Instalar las dependencias:
      ```bash
      pip install -r requirements.txt
      ```
3. Iniciar la API desde la carpeta src:

      ```bash
      uvicorn API.main:app --reload
      ```


## App Web

La pagina se creó con [next, react y react-dom](https://reactnative.dev/docs/environment-setup) con el siguiente comando:
```
npm install next react react-dom
```

### Pre-requisitos:
1. Instalar [react-dom] necesario para su funcionamiento.
2. Instalar [Next] para renderizar el servidor y generacion de sitios.
3. Instalar [react] para construir las interfaces de usuario.

### Comenzando

1. Instalar dependencias

   ```bash
   npm run dev
   ```

2. Iniciar la aplicación

   ```bash
    npm start
   ```

Y una vez lista, se entrega una IP o un LocalHost con la pagina implementada, junto con su puerto correspondiente. 