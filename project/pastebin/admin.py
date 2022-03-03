from django.contrib import admin
from django.apps import apps
from project.pastebin.models.admin import *

def autoregister(*app_list : str) -> None: 
    """
    register all databse models in the admin dashboard
    """
    for app in app_list :
        for model_name, model in apps.get_app_config(app).models.items() :
            if '_' not in model_name:
                if globals().get(model.__name__+'Admin')   :
                    admin.site.register(model, globals().get(model.__name__+'Admin'))
                else :
                    admin.site.register(model)
autoregister('pastebin')