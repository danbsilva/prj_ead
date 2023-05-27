import os
from importlib import import_module


def init_app(app):
    app.config.from_pyfile('config/settings.py')
    load_configs(app)


def load_configs(app):
    for extension in app.config['EXTENSIONS']:
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext, factory)(app)

    for resource in app.config['RESOURCES']:
        module_name, factory = resource.split(":")
        ext = import_module(module_name)
        getattr(ext, factory)(app)
