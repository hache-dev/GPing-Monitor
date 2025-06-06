
# GPing Monitor

📡 **GPing Monitor** es una aplicación web y de escritorio para monitorear la latencia y el estado de hosts en tiempo real mediante pings. Permite agregar y eliminar hosts fácilmente y visualizar la latencia en gráficos dinámicos.

![image](https://github.com/user-attachments/assets/5703e801-bead-4262-aca3-505ee9a70939)


---

## Características

- Interfaz moderna y responsive basada en Bootstrap 5 con tema oscuro.
- Monitoreo en tiempo real de múltiples hosts.
- Visualización gráfica de latencia histórica (últimos 30 puntos).
- Soporte para hosts con IP, dominios y `localhost`.
- Guardado persistente de hosts en archivo local `hosts.txt`.
- Agregar y eliminar hosts desde la interfaz.
- Notificaciones con toasts para avisos y errores.

---

## Requisitos

- Python 3.8 o superior
- Paquetes Python:
  - `Flask`
  - `ping3`
  - `pywebview`

Puedes instalarlos con:

```bash
pip install Flask ping3 pywebview
```

---

## Archivos principales

- `app.py`: Script principal con la aplicación Flask y la integración de pywebview.
- `templates/index.html`: Interfaz web con Bootstrap y lógica de frontend en JavaScript.
- `hosts.txt`: Archivo donde se almacenan los hosts agregados (creado automáticamente).

---

## Uso

1. Clona o descarga este repositorio.
2. Asegúrate de tener instalados los paquetes necesarios (`Flask`, `ping3`, `pywebview`).
3. Ejecuta el script principal:

```bash
python app.py
```

4. Se abrirá una ventana con la interfaz de monitoreo.
5. Agrega hosts (IP o dominios) en el campo de texto separados por coma y presiona "Add Host".
6. La aplicación realizará pings periódicos (cada 1.5 segundos) y mostrará la latencia en gráficos.
7. Puedes eliminar hosts con el botón "x" en cada tarjeta.

---

## Personalización

- El intervalo de ping está configurado en `INTERVAL = 1500` ms (1.5 segundos).
- Se guardan hasta 30 puntos de latencia por host (`MAX_POINTS`).
- El número máximo de hosts por diapositiva del carrusel es 6 (`PER_SLIDE`).

---

## Notas

- La aplicación usa `ping3` que requiere permisos adecuados para enviar paquetes ICMP (puede necesitar ejecución con permisos de administrador o root en algunos sistemas).
- La interfaz está en español y usa tema oscuro por defecto.
- La aplicación corre en el puerto `5009` por defecto.

---

## Licencia

Este proyecto es de código abierto y puede usarse y modificarse libremente.

---

¡Disfruta monitoreando tus hosts con GPing Monitor! 🚀
