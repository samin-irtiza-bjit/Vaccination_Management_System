from django.contrib import admin
from django.apps import apps

frontend_models = apps.get_app_config('frontend').get_models()

for model in frontend_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass