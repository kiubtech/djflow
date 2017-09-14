# djflow.

Maneje de forma efectiva el flujo de de ingresos y egresos que tiene su negocio

# Instalación

Al descargar el proyecto encontraremos un archivo llamado "requirements.txt" el cual contiene todas las dependencias Python para ejecutar el proyecto. 

Ejecutamos lo siguiente: 

    [kiubtech]$ pip install -r requirements.txt


# Configuración.

Cree una copia del archivo "settings.example.json" con el nombre "settings.json".

Una vez realizado esto, deberá configurar la información de las credenciales de su base de datos

    "DB": {
        "default": {
          "ENGINE": "django.db.backends.postgresql_psycopg2",
          "HOST": "localhost",
          "NAME": "djflow",
          "USER": "admin",
          "PASSWORD": "admin",
          "PORT": 5432
        }
      }


Y también sus credenciales de envío de correos electrónicos. 

    "EMAIL": {
        "EMAIL_USE_TLS": true,
        "EMAIL_HOST": "smtp.gmail.com",
        "EMAIL_PORT": 587,
        "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "EMAIL_HOST_USER": "my-mail@gmail.com",
        "EMAIL_HOST_PASSWORD": "**************",
        "DEFAULT_FROM_EMAIL": "my-mail@gmail.com",
        "CONTACT_EMAIL": "my-mail@gmail.com"
      }

# Iniciando base de datos y proyecto.

Ejecutamos las migraciones para crear la base de datos: 

    [kiubtech]$ python manage.py migrate


y posteriormente generamos nuestro super usuario. 

    [kiubtech]$ python manage.py createsuperuser


Listo! Esto debe ser todo lo necesario para que tengan corriendo el proyecto en sus equipos locales: 

    [kiubtech]$ python manage.py runserver

# Powered by Open Source Projects. 

Agradecemos enormemente el esfuerzo de las comunidades que mantienen el desarrollo de los siguientes proyectos.

- [Django Project](https://www.djangoproject.com)
- [Django Solo](https://github.com/lazybird/django-solo)
- [Pillow](https://github.com/python-pillow/Pillow)
- [PostGreSQL](https://www.postgresql.org/)
- [Psycopg2](https://github.com/psycopg/psycopg2)
- [Django Tenant Schemas](https://github.com/bernardopires/django-tenant-schemas)
- [Bootstrap v4](http://getbootstrap.com/)


# Licenciamiento.

MIT License

    Copyright (c) 2017 Kiub Technologies
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.



Make with love by [@kiubtech](https://twitter.com/kiubtech) and [@pythonizame](https://twitter.com/pythonizame).


