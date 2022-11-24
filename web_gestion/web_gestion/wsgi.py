#Este fichero es la interfaz de puerta de enlace del servidor
#es el que ejecuta el python, pone en marcha el servicio y lo deja corriendo

"""
WSGI config for web_gestion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_gestion.settings')

application = get_wsgi_application()
