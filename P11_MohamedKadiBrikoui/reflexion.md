# Reflexión sobre la Práctica

### ¿Qué has aprendido sobre balanceo?
He aprendido que el balanceo de carga es fundamental para distribuir el tráfico entre varios servidores, evitando que una sola instancia se sature. Utilizando NGINX con un bloque `upstream`, es sencillo repartir las peticiones usando el algoritmo Round-Robin, lo que aumenta la capacidad de respuesta del sistema.

### ¿Cómo has identificado qué instancia respondía?
En la aplicación Flask (`application.py`), utilizamos la librería `socket` y la función `socket.gethostname()`. Como cada contenedor Docker tiene un ID único que actúa como su nombre de host, al imprimir este valor en la respuesta HTTP podemos visualizar físicamente qué contenedor específico procesó nuestra petición.

### ¿Qué pasaría si NGINX falla?
NGINX actúa como el único punto de entrada al sistema (puerta de enlace). Si el contenedor de NGINX falla o se detiene, el sitio web completo dejaría de ser accesible para el usuario final, aunque las instancias de Flask sigan funcionando correctamente en segundo plano.

### ¿Qué mejorarías en este sistema?
Para solucionar el problema anterior, añadiría un segundo balanceador NGINX configurado en alta disponibilidad para que si uno cae, el otro asuma el tráfico. También añadiría HTTPS para cifrar las comunicaciones y un sistema de monitoreo de logs centralizado.

### ¿Qué ventajas ves al usar GitHub?
GitHub permite mantener un historial de versiones del código (control de cambios), facilita la colaboración si hubiera más desarrolladores, y sirve como una copia de seguridad en la nube. Además, simplifica el despliegue en cualquier máquina nueva, ya que solo hace falta clonar el repositorio para tener toda la infraestructura lista.