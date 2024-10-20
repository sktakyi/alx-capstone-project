"""
WSGI config for im_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Adjust the following line to include your project directory
path = '/home/sktakyi/alx-capstone-project/im_api'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'im_api.settings'

# Activate your virtual environment
activate_this = '/home/sktakyi/alx-capstone-project/im_api/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
