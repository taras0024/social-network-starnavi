import os

import django
from django.core.management.color import color_style
from django_extensions.management import shells

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

imported_items = shells.import_objects({}, color_style())
for k, v in imported_items.items():
    globals()[k] = v
