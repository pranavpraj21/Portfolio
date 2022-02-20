from django.contrib import admin
from .models import Project,reviewed

admin.site.register(reviewed)
admin.site.register(Project)
