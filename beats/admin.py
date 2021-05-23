from django.contrib import admin
from .models import Instrumental, Producer

models = [
    Instrumental,
    Producer
    ]

for model in models: 
    admin.site.register(model)