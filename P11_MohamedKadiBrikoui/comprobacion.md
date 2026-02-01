# Comprobación Técnica

### ¿Qué hace el bloque upstream?
El bloque `upstream` en NGINX define un grupo de servidores backend (en nuestro caso: `web1`, `web2` y `web3`) a los que NGINX puede redirigir el tráfico. NGINX trata este grupo como una única entidad para distribuir la carga entre ellos.

### ¿Cómo se configuran los healthchecks?
Los *healthchecks* se configuran en el archivo `docker-compose.yml` dentro de cada servicio. Hemos definido un test que ejecuta `curl -f http://localhost:8000/status`. Si el contenedor devuelve un código 200 OK, Docker lo marca como "healthy", si falla repetidamente, Docker sabe que esa instancia no está disponible.

### ¿Cómo se pasa tráfico de NGINX a Flask?
El tráfico se pasa mediante la directiva `proxy_pass http://flask_servers;` dentro del bloque `location /` de la configuración de NGINX. Esto toma la petición que llega al puerto 80 de NGINX y la reenvía al grupo de servidores definido en el `upstream`.

### ¿Qué puertos se usan?
* **8080**: Puerto externo en la máquina anfitriona (el que usa el usuario en el navegador).
* **80**: Puerto interno del contenedor NGINX donde escucha las peticiones.
* **8000**: Puerto interno de los contenedores Flask donde Gunicorn está escuchando.

### ¿Qué función tiene Gunicorn?
Gunicorn es un servidor HTTP WSGI de nivel de producción. Mientras que el servidor integrado de Flask es solo para desarrollo y no gestiona bien la concurrencia, Gunicorn es robusto, rápido y capaz de manejar múltiples peticiones simultáneas de manera eficiente antes de pasarlas a la aplicación Python.