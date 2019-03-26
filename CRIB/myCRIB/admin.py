from django.contrib import admin
from .models import Rooms
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Rooms)
class ViewAdmin(ImportExportModelAdmin):
    pass