"""
WSGI config for repo_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

{% if cookiecutter.use_white_red_noise == 'white' -%}
from whitenoise.django import DjangoWhiteNoise
{% elif cookiecutter.use_white_red_noise == 'red' -%}
from rednoise import DjangoRedNoise
{%- endif %}

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

{% if cookiecutter.use_white_red_noise == 'white' %}
# Use Whitenoise to serve static files
# See: https://whitenoise.readthedocs.org/
application = DjangoWhiteNoise(application)
{% elif cookiecutter.use_white_red_noise == 'red' %}
# Use Whitenoise to serve static files
# See: https://whitenoise.readthedocs.org/
application = DjangoRedNoise(application)
{% endif %}

