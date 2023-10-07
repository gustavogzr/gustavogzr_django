from django.contrib import admin

# Register your models here.
from .models import responsavel_tarefa, tarefa

admin.site.register(responsavel_tarefa)
admin.site.register(tarefa)
