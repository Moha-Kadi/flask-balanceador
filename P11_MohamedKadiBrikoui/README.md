# Práctica 11: Balanceo de Carga Escalable con Flask, Gunicorn y NGINX

Este proyecto implementa una arquitectura web escalable y tolerante a fallos basada en contenedores Docker. El sistema simula un entorno de producción real utilizando **Flask** como backend, **Gunicorn** como servidor de aplicaciones y **NGINX** como balanceador de carga.

## 1. Explicación del Sistema
La arquitectura consta de los siguientes componentes orquestados:
* **3 Instancias Backend:** Contenedores que ejecutan una aplicación Python/Flask servida por Gunicorn en el puerto 8000.
* **Balanceador de Carga:** Un contenedor NGINX que recibe todas las peticiones en el puerto 8080 (host) y las distribuye equitativamente entre las 3 instancias backend utilizando el algoritmo *Round-Robin*.
* **Healthchecks:** El sistema verifica automáticamente la salud de los contenedores; si una instancia falla, NGINX deja de enviarle tráfico.

## 2. Cómo se despliega
Requisitos: Tener instalado Docker y Docker Compose.

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu_usuario/flask-balanceador.git](https://github.com/Moha-Kadi/flask-balanceador)
    cd flask-balanceador
    ```

2.  **Levantar la infraestructura:**
    Ejecuta el siguiente comando para construir las imágenes y arrancar los contenedores:
    ```bash
    docker compose up --build
    ```

3.  **Acceso:**
    Una vez iniciado, el sistema estará accesible en: `http://localhost:8080`

## 3. Qué hace cada archivo
* **`app/application.py`**: Código fuente de Flask. Devuelve el *hostname* (ID del contenedor) para identificar visualmente qué servidor responde a cada petición.
* **`app/wsgi.py`**: Punto de entrada (Entry Point) utilizado por Gunicorn para servir la aplicación en producción.
* **`docker/nginx_balanceador.conf`**: Configuración de NGINX. Define el bloque `upstream` con los 3 servidores y configura el proxy inverso.
* **`docker-compose.yml`**: Archivo de orquestación. Define los servicios (`web1`, `web2`, `web3`, `nginx`), sus redes, volúmenes y comprobaciones de salud (*healthchecks*).
* **`scripts/test_balanceo.sh`**: Script en Bash que realiza 10 peticiones consecutivas mediante `curl` para demostrar el funcionamiento del balanceo de carga.
* **`Dockerfile`**: Instrucciones para construir la imagen de los servidores web, incluyendo la instalación de Python, dependencias y `curl` para los healthchecks.

## 4. Cómo probarlo
Existen dos formas de verificar el funcionamiento:

Ejecuta el script incluido en el proyecto:
```bash
bash scripts/test_balanceo.sh