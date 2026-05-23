import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pelec_ho3.settings')

application = get_wsgi_application()

def handler(event, context):
    return application(event, context)